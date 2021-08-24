import numpy as np
from train_model import train_model_on_one_ecg
from build_model import build_conv1d_res_model, build_conv1d_model
from load_weights import load_weights

# используемые модели
names_models = [build_conv1d_model, build_conv1d_res_model]


def train_models_with_peaks(data_train, class_weight, x_test_ptb, y_test_ptb,
                            x_valid_ptb, y_valid_ptb, name_model):
    # размер для модели
    input_shape = (x_test_ptb.shape[1], x_test_ptb.shape[2])

    history_conv1d_ptb, model_conv1d_ptb = train_model_on_one_ecg(
        data_train, class_weight, x_valid_ptb, y_valid_ptb,
        name_model, input_shape)

    model_conv1d_ptb.load_weights(load_weights(name_model))
    # model_conv1d_ptb.evaluate(x_test_ptb,y_test_ptb)
    conv1d_pred_proba_ptb = model_conv1d_ptb.predict(x_test_ptb)
    conv1d_pred_ptb = np.argmax(conv1d_pred_proba_ptb, axis=1)

    return model_conv1d_ptb.evaluate(x_test_ptb,y_test_ptb), conv1d_pred_ptb
