import wfdb
import numpy as np

# для формирования X по ЭКГ (кол-во ЭКГ(не пациентов!), 100 записей в сек, кол-во электродов)
def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path + f) for f in df.filename_lr]
    else:
        data = [wfdb.rdsamp(path + f) for f in df.filename_hr]
    data = np.array([signal for signal, meta in data])

    return data


# для data_X
def load_raw_data_X(df, sampling_rate, path):
    data_X = []
    if sampling_rate == 100:
        for f in df.filename_lr:
            data_X.append([df.filename_lr, wfdb.rdsamp(path + f)])
    else:
        for f in df.filename_hr:
            data_X.append([df.filename_hr, wfdb.rdsamp(path + f)])

    return data_X


# для обозначения суперкласса нормальный/не нормальный (в задаче другие таргеты)
def aggregate_diagnostic(y_dic, agg_df):
    tmp = []
    for key in y_dic.keys():

        if key in agg_df.index:
            diag = agg_df.loc[key].diagnostic_class
            if diag == 'NORM':
                tmp.append(diag)

            else:
                tmp.append('pathology')

    return list(set(tmp))