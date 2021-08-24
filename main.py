import pandas as pd
import tensorflow as tf
from X_y_split import train_first_model
from build_model import build_conv1d_model, build_conv1d_res_model
from train_models_without_peaks import train_models_without_peaks
from train_models_with_peaks import train_models_with_peaks

# используемые модели
names_models = [build_conv1d_model, build_conv1d_res_model]

# датасеты, уже разбиты
path = '~/Downloads/ISP_RAN_ECG/'
target_files = ['train_multi.csv', 'test_multi.csv', 'valid_multi.csv']

data_train = pd.read_csv(path + target_files[0])
data_test = pd.read_csv(path + target_files[1])
data_valid = pd.read_csv(path + target_files[2])
datas = [data_train, data_test, data_valid]


# тестовая и валидационные X и y, а также веса для модели
x_train_ptb, y_train_ptb, \
x_test_ptb, y_test_ptb, \
x_valid_ptb, y_valid_ptb, \
class_weight, PTB_Outcome = train_first_model(datas)

# размер для модели
input_shape = (x_train_ptb.shape[1], x_train_ptb.shape[2])
tf.keras.backend.clear_session()

# тренировка моделей без пик
train_models_without_peaks(names_models, input_shape, class_weight,
                               x_train_ptb, y_train_ptb,
                               x_valid_ptb, y_valid_ptb,
                               x_test_ptb, y_test_ptb)


# тренировка моделей с пиками
tf.keras.backend.clear_session()

names_models = [build_conv1d_model, build_conv1d_res_model]
# sinus:
data_train = data_train[data_train.columns[:-4]]

train_models_with_peaks(
        data_train, class_weight, x_test_ptb, y_test_ptb,
        x_valid_ptb, y_valid_ptb, names_models[0])

# train_models_with_peaks(
#         data_train, class_weight, x_test_ptb, y_test_ptb,
#         x_valid_ptb, y_valid_ptb, names_models[1])






