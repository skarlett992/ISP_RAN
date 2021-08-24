import pandas as pd
from build_model import build_conv1d_model, build_conv1d_res_model

# используемые модели
names_models = [build_conv1d_model, build_conv1d_res_model]

# датасеты, уже разбиты
path = '/Users/yuriybiznigaev/Downloads/ISP_RAN/py-ecg-detectors-1.0.2/'
target_files = ['package/train_multi.csv', 'package/test_multi.csv', 'package/valid_multi.csv']


# data_train = pd.read_csv(path + target_files[0])
# data_test = pd.read_csv(path + target_files[1])
data_valid = pd.read_csv(path + target_files[2])

database = pd.read_csv(path + 'example_data/ptbxl_database.csv')


list_train_1 = data_valid[data_valid.bradykardie == 'bradykardie']['ecg_id'].unique().tolist()
for i in list_train_1:
    if 'NORM' in database[database['ecg_id'] == i].scp_codes.keys():
        print(database[database['ecg_id'] == i].report)



