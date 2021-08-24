import pandas as pd
from target_ills_data import target_cols

path = '~/Downloads/ISP_RAN_ECG/'


signal_files = ['train_signal.csv',
                'test_signal.csv',
                'valid_signal.csv']

target_files = ['train_multi.csv', 'test_multi.csv', 'valid_multi.csv']

def join_data_to_ill(path, dataset):
    ill_data = pd.read_csv(path + 'package/ill_data.csv')
    ill_data = ill_data[['ecg_id']+target_cols]
    df_signal = pd.read_csv(path + dataset)
    out_df = df_signal.join(ill_data.set_index('ecg_id'), on='ecg_id')
    return out_df

def save_target_datasets(signal_files, target_files):
    joined_datasets = []
    for i in range(len(signal_files)):
        join_df = join_data_to_ill(path, signal_files[i])
        # обязательно NaN исключить (неясно, к каким заболеваниям относились
        # и были удалены, поэтому стали нанами при join)
        join_df_multi = join_df[~join_df['sinus_rythm'].isnull()]
        join_df_multi.to_csv(target_files[i], index=False)
        joined_datasets.append(join_df_multi)

    return joined_datasets

joined_datasets = save_target_datasets(
    signal_files, target_files
    )

print(joined_datasets)
train_df = joined_datasets[0]
test_df = joined_datasets[1]
valid_df = joined_datasets[2]
print(train_df)





