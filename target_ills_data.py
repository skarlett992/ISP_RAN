from target_dict import target_dict

target_cols = ['sinus_rythm', 'arithmia', 'bradykardie', 'tahicardia', 'fibrillation']

def target_ills_data(Y):
    Y['sinus_rythm'] = Y.report
    Y['arithmia'] = Y.report
    Y['bradykardie'] = Y.report
    Y['tahicardia'] = Y.report
    Y['fibrillation'] = Y.report

    for ind, row in enumerate(Y.scp_codes):
        if 'NORM' in row.keys() and row['NORM'] >= 80:
            for col in target_cols:
                Y[col][ind] = 'normal'
        else:
            for ill, variables in target_dict.items():
                for var in variables:
                    if var in Y.report[ind]:
                        Y[ill][ind] = ill

    Y.to_csv('ill_data.csv', index=False)

    return Y, target_cols

def another_ill_or_delete(target_ills_data, target_cols):
    another_ills = []
    rows_to_delete = []

    df_abnormal = target_ills_data[(target_ills_data['sinus_rythm'] != 'normal') \
                                   & (target_ills_data['arithmia'] != 'normal') & \
                                    (target_ills_data['bradykardie'] != 'normal') \
                                   & (target_ills_data['tahicardia'] != 'normal') & \
                                   (target_ills_data['fibrillation'] != 'normal')]
    for ecg_id in df_abnormal.ecg_id:
        list_rows = df_abnormal[df_abnormal['ecg_id']==ecg_id]\
            [target_cols].to_numpy().tolist()[0]
        ind = target_ills_data[target_ills_data['ecg_id'] == ecg_id].index.tolist()[0]
        # if any(target_cols) in list_rows:
        if target_cols[0] in list_rows or target_cols[1] in list_rows\
        or target_cols[2] in list_rows or target_cols[3] in list_rows\
        or target_cols[4] in list_rows:
            if ind not in another_ills:
                another_ills.append(ind)

        else:
            if ind not in rows_to_delete:
                rows_to_delete.append(ind)

    return another_ills, rows_to_delete, df_abnormal

def delete_some_rows(df, rows_to_delete):
    # df = df.drop(index=[rows_to_delete])
    df = df.drop(df.index[rows_to_delete])
    return df

def another_ill(target_ills_data, target_cols, another_ills, df_abnormal):
    # another_ill_data = target_ills_data.iloc[another_ills, :]
    for ind in df_abnormal.index.tolist():
        if ind in another_ills:
            for col in target_cols:
                if target_ills_data[col][ind] not in target_dict.keys():
                    target_ills_data[col][ind] = 'normal'
    return target_ills_data




