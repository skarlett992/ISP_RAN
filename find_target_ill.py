from target_dict import target_dict

def target_ill(Y):
    # чтобы определить главные таргеты из report, вынесем все в признаки в отдельный файл
    target_values = []
    target_ill = []

    for ind, target in enumerate(Y[Y['norm_ecg'] == 0].report):
        for key, value in target_dict.items():
            for v in value:
                if v in target:
                    target_values.append([key, ind])
                    target_ill.append(target)

    # наши целевые таргеты

    sinus_rythm = []
    arithmia = []
    bradycardia = []
    tachycardia = []
    fibrillation = []
    nan_ill = []
    questions_ill = []

    for target in target_values:
        if target[0] == 'sinus' and target[1] not in sinus_rythm:
            sinus_rythm.append(target[1])
        elif target[0] == 'arithmia' and target[1] not in arithmia:
            arithmia.append(target[1])
        elif target[0] == 'bradykardie' and target[1] not in bradycardia:
            bradycardia.append(target[1])
        elif target[0] == 'tahicardia' and target[1] not in tachycardia:
            tachycardia.append(target[1])
        elif target[0] == 'fibrillation' and target[1] not in fibrillation:
            fibrillation.append(target[1])
        elif target[0] == 'Nans' and target[1] not in nan_ill:
            nan_ill.append(target[1])
        elif target[0] == 'dont_now' and target[1] not in questions_ill:
            questions_ill.append(target[1])

    Y['sinus_rythm'] = 'normal'
    Y['arithmia'] = 'normal'
    Y['bradycardia'] = 'normal'
    Y['tachycardia'] = 'normal'
    Y['fibrillation'] = 'normal'
    Y['nan_ill'] = 'normal'
    Y['questions_ill'] = 'normal'

    add_col = ['sinus_rythm', 'arithmia', 'bradycardia', 'tachycardia', 'fibrillation', 'nan_ill', 'questions_ill']
    add_values = {'sinus_rythm': sinus_rythm,
                  'arithmia': arithmia,
                  'bradycardia': bradycardia,
                  'tachycardia': tachycardia,
                  'fibrillation': fibrillation,
                  'nan_ill': nan_ill,
                  'questions_ill': questions_ill}

    for ind in sinus_rythm:
        Y['sinus_rythm'][ind] = 'sinus_rythm'
    for ind in arithmia:
        Y['arithmia'][ind] = 'arithmia'
    for ind in bradycardia:
        Y['bradycardia'][ind] = 'bradycardia'
    for ind in tachycardia:
        Y['tachycardia'][ind] = 'tachycardia'
    for ind in fibrillation:
        Y['fibrillation'][ind] = 'fibrillation'
    for ind in questions_ill:
        Y['questions_ill'][ind] = 'questions_ill'
