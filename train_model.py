from sklearn.preprocessing import normalize
from tensorflow.keras.utils import to_categorical
from unique_ecg_with_peaks import merge_peaks_to_data
from target_with_peak import find_y
from unique_ecg_without_peaks import get_unfiltered_ecg
from fit_model import history_model
from build_model import summary_model
from choose_model import choose_model
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

def train_model_on_one_ecg(data_train, class_weight, x_valid_ptb, y_valid_ptb,
                           name_model, input_shape):
    model_conv1d_ptb, checkpoint_cb, earlystop_cb = choose_model(name_model, input_shape)

    summary_model(model_conv1d_ptb)
    history_conv1d_ptb = None

    for ecg_id in data_train['ecg_id'].unique():
        df_with_peaks = merge_peaks_to_data(data_train, ecg_id)
        y_train_ptb = find_y(
            df_with_peaks,
            get_unfiltered_ecg(
                data_train, ecg_id, False
            )
        )
        y_train_ptb = le.fit_transform(y_train_ptb)
        y_train_ptb = to_categorical(y_train_ptb, num_classes=2)
        train_ptb = normalize(df_with_peaks.drop(['target'], axis=1), axis=0, norm='max')
        x_train_ptb = train_ptb.reshape(len(train_ptb), train_ptb.shape[1], 1)

        history_conv1d_ptb, model_conv1d_ptb = history_model(
            model_conv1d_ptb, checkpoint_cb, earlystop_cb, class_weight,
            x_train_ptb, y_train_ptb, x_valid_ptb, y_valid_ptb)
        print(ecg_id, sep='', end="\r", flush=True)

    return history_conv1d_ptb, model_conv1d_ptb
