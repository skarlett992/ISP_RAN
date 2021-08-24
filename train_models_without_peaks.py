import numpy as np
from choose_model import choose_model
from build_model import summary_model
from fit_model import history_model
from load_weights import load_weights

def train_models_without_peaks(names_models, input_shape, class_weight,
                               x_train_ptb, y_train_ptb,
                               x_valid_ptb, y_valid_ptb,
                               x_test_ptb, y_test_ptb):
        # for name_model in names_models:
        model_conv1d_ptb, checkpoint_cb, earlystop_cb = choose_model(
                names_models[0], input_shape)

        summary_model(model_conv1d_ptb)
        history_conv1d_ptb, model_conv1d_ptb = history_model(
                model_conv1d_ptb, checkpoint_cb, earlystop_cb, class_weight,
                x_train_ptb, y_train_ptb, x_valid_ptb, y_valid_ptb
                )
        model_conv1d_ptb.load_weights(load_weights(names_models[0]))
        # model_conv1d_ptb.evaluate(x_test_ptb,y_test_ptb)
        conv1d_pred_proba_ptb = model_conv1d_ptb.predict(x_test_ptb)
        conv1d_pred_ptb = np.argmax(conv1d_pred_proba_ptb, axis=1)

        return model_conv1d_ptb.evaluate(x_test_ptb,y_test_ptb), conv1d_pred_ptb
