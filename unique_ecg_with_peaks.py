from unique_ecg_without_peaks import get_unfiltered_ecg
from peak_functions import pad_nan_peaks
from peak_functions import get_peaks
import pandas as pd
import numpy as np

# функция, объединяющая пики и обычный тренировочный ЭКГ по одному id
def merge_peaks_to_data(df, ecg_id):
    ecg_unique = get_unfiltered_ecg(df, ecg_id)
    peaks_df = pad_nan_peaks(get_peaks(df, ecg_id))
    df_with_peaks = pd.concat([ecg_unique, peaks_df], ignore_index=True)
    df_with_peaks['ecg_id'] = ecg_id
    return df_with_peaks

# функция, дополняющая количество пиков по каналам до равного количества
# (заполнение нанов=9999) и формирование датасета по одному ЭКГ с пиками
def df_with_peaks(df):
    labels = []
    for ecg_id in df['ecg_id'].unique():
        if ecg_id == min(df['ecg_id'].unique()):
            df_with_peaks = merge_peaks_to_data(df, ecg_id)
            label = np.pad([], (0, df_with_peaks.shape[0]), 'constant',
                           constant_values=ecg_id)
            labels.append(label)

        else:
            df_with_peaks = pd.concat([df_with_peaks, merge_peaks_to_data(df, ecg_id)])

            label = np.pad([], (0, merge_peaks_to_data(df, ecg_id).shape[0]), 'constant',
                           constant_values=ecg_id)
            labels.append(label)

    return df_with_peaks