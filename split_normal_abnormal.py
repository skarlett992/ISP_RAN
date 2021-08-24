# уберем пустые значения суперкласса, а также те, которые будут нас путать (нормальные ЭКГ, смешанные с ненормальными)
# оставим два основных для нас информационных столбца: нормальное/не нормальное ЭКГ и патология/нет
def norm_abnorm(Y):
    norm = []
    pathology = []
    drop = []
    for ind, i in enumerate(Y['diagnostic_superclass']):
        if len(i) == 0:
            drop.append(ind + 1)
        elif len(i) > 1 and 'NORM' in i:
            drop.append(ind + 1)
        elif 'NORM' in i:
            norm.append(ind + 1)
        elif 'pathology' in i:
            pathology.append(ind + 1)

    Y = Y.drop([d for d in drop])
    Y['norm_ecg'] = 'normal'
    Y['pathology'] = 'normal'

    for ind in Y.index:
        if ind in norm:
            Y['norm_ecg'][ind] = 'abnormal'
        elif ind in pathology:
            Y['pathology'][ind] = 'abnormal'

    return Y