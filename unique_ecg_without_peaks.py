# функция, возвращающая фрейм только по указанному экг
def get_unfiltered_ecg(df, ecg_id, cut_target_data=True):
    ecg_unique = df[df['ecg_id'] == ecg_id]

    return ecg_unique[ecg_unique.columns[1:-1]] if cut_target_data else ecg_unique