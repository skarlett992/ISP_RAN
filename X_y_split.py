import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize, LabelEncoder
le = LabelEncoder()

from tensorflow.keras.utils import to_categorical


# функция тренировки первой модели
def train_first_model(datas):

    datas_sinus = []
    for data in datas:
        data = data[data.columns[1:-4]]
        data['sinus_rythm'] = le.fit_transform(data['sinus_rythm'])
        datas_sinus.append(data)
    data_train = datas_sinus[0]
    data_test = datas_sinus[1]
    data_valid = datas_sinus[2]

    ptb_full = pd.concat([data_train, data_test, data_valid], axis=0).reset_index()
    ptb_full.drop(columns='index', inplace=True)
    ptb_full = ptb_full.sample(ptb_full.shape[0], random_state=42)

    normal, sinus_rythm = np.bincount(ptb_full.loc[:, 'sinus_rythm'])
    norm_weight = (1 / normal) * ((normal + sinus_rythm) / 2)
    sinus_rythm_weight = (1 / sinus_rythm) * ((normal + sinus_rythm) / 2)
    class_weight = {0: norm_weight, 1: sinus_rythm_weight}

    PTB_Outcome = {0.: 'normal',
                   1.: 'sinus_rythm'}

    train_ptb = data_train.sample(data_train.shape[0], random_state=42)
    out_train_ptb = train_ptb['sinus_rythm']
    train_ptb = train_ptb[train_ptb.columns[:-1]]

    test_ptb = data_test.sample(data_test.shape[0], random_state=42)
    out_test_ptb = test_ptb['sinus_rythm']
    test_ptb = test_ptb[test_ptb.columns[:-1]]

    valid_ptb = data_valid.sample(data_valid.shape[0], random_state=42)
    out_valid_ptb = valid_ptb['sinus_rythm']
    valid_ptb = valid_ptb[valid_ptb.columns[:-1]]

    #
    print("Traing dataset size: ", train_ptb.shape)
    print("Validation dataset size: ", valid_ptb.shape)
    print("Test dataset size: ", test_ptb.shape)
    #

    # Normalizing the training, validation & test data
    train_ptb = normalize(train_ptb, axis=0, norm='max')
    valid_ptb = normalize(valid_ptb, axis=0, norm='max')
    test_ptb = normalize(test_ptb, axis=0, norm='max')
    # Reshaping the dataframe into a 3-D Numpy array (batch, Time Period, Value)
    x_train_ptb = train_ptb.reshape(len(train_ptb), train_ptb.shape[1], 1)
    x_valid_ptb = valid_ptb.reshape(len(valid_ptb), valid_ptb.shape[1], 1)
    x_test_ptb = test_ptb.reshape(len(test_ptb), test_ptb.shape[1], 1)

    # Converting the output into a categorical array
    y_train_ptb = to_categorical(out_train_ptb, num_classes=2)
    y_valid_ptb = to_categorical(out_valid_ptb, num_classes=2)
    y_test_ptb = to_categorical(out_test_ptb, num_classes=2)

    print("Traing dataset size: ", x_train_ptb.shape, " -- Y size: ", y_train_ptb.shape)
    print("Validation dataset size: ", x_valid_ptb.shape, " -- Y size: ", y_valid_ptb.shape)
    print("Test dataset size: ", x_test_ptb.shape, " -- Y size: ", y_test_ptb.shape)

    return x_train_ptb, y_train_ptb, \
           x_test_ptb, y_test_ptb, \
           x_valid_ptb, y_valid_ptb, \
           class_weight, PTB_Outcome

# data_test = pd.read_csv('../example_data/new_test_df.csv')[:100000]
# data_train = pd.read_csv('../example_data/new_train_df.csv')[:100000]
# data_valid = pd.read_csv('../example_data/new_valid_df.csv')[:100000]

# x_train_ptb, y_train_ptb, \
# x_test_ptb, y_test_ptb, \
# x_valid_ptb, y_valid_ptb = train_first_model(data_train, data_test, data_valid)
