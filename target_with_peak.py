
# если y с пиками и надо определить длину таргета
def find_y(df_with_peaks, start_df):
    ecg_id = df_with_peaks['ecg_id'][0]
    y_value = start_df['sinus_rythm'].tolist()[0]
    df_with_peaks['target'] = y_value

    return df_with_peaks['target']