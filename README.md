# ISP_RAN
ECG
### Задача заключается в оценке значимости использования алгоритма/алгоритмов преобработки pqrst-комплексов при построении классификации ЭКГ.
Необходимо построить две модели: без учета обработанных qrst-комплексов в качестве признаков и с ними и оценить значимость признаков qrst-комплексов.
Нарушения ритма, которые стоит выбрать: синусовый ритм, аритмия, брадикардия, тахикардия, фибрилляция предсердий. 
Для сравнения моделей на одном и том же тестовом наборе в качестве метрик оценки качества стоит взять F1-score, Sensitivity, Specisifity, ROC-AUC для каждой патологии по отдельности и среднее значение по всем патологиям.
__________________________________________________________________________________________________________________________________
### The task is to assess the significance of using the algorithm / algorithms for processing pqrst-complexes when constructing an ECG classification.It is necessary to build two models: without taking into account the processed qrst-complexes as features and with them, and to assess the significance of the qrst-complexes features.
Rhythm disorders to choose from: sinus rhythm, arrhythmia, bradycardia, tachycardia, atrial fibrillation.
To compare models on the same test set, F1-score, Sensitivity, Specisifity, ROC-AUC for each pathology separately and the average value for all pathologies should be taken as quality assessment metrics.

Дано:
1) два датасета (около 21000 ЭКГ в целевом) с аннотациями и метаданными по пациентам, которые включают в себя описание заболеваний данных пациентов по ЭкГ.
2) ЭКГ пациентов в файлах, каждый файл имеет ссылку, которая указана в метаданных пациента.
__________________________________________________________________________________________________________________________________
Given:
1) two datasets (about 21000 ECGs in the target) with annotations and metadata for patients, which include a description of the diseases of these patients by ECG.
2) ECG of patients in files, each file has a link that is indicated in the patient's metadata.


# Запуск работы/ Run code
установить версию/  install version Python 3.7.7 
```
virtualenv venv --python=python3.7.7
```
установить зависимости/  install dependencies
```
pip install -r requirements.txt
```
ссылки на некоторые файлы .csv для запуска программы:
1. основные, - обработанные сигналы ЭКГ, приведенные с помощью специальной библиотеки в датасет.
Их можно получить, запустив код по ссылке https://www.kaggle.com/natalyayurina/ptb-xl-dataset-wrangling
__________________________________________________________________________________________________________________________________

links to some .csv files to run the program:
1. main, - processed ECG signals, given using a special library in a dataset.
They can be obtained by running the code at the link https://www.kaggle.com/natalyayurina/ptb-xl-dataset-wrangling

1) 'train_signal.csv'
https://drive.google.com/file/d/1gzUcPSQyrhLeMta-i79LGupPHueAiL9T/view?usp=sharing
2) 'test_signal.csv'
https://drive.google.com/file/d/1J70RMXu--lNVr4O7WBjxhjUyMS8M-Bmp/view?usp=sharing
3) 'valid_signal.csv'
https://drive.google.com/file/d/1EQbiR4SSlfnviqswYY43BrUT_luf2bdy/view?usp=sharing

2. датасеты с данными по заболеваниям (бинарные по каждому таргету)/ datasets with data on diseases (binary for each target): 

'train_multi.csv' (https://drive.google.com/file/d/18Hi0sNR8VI-dDANQ6e1EW0IKBmodyRX3/view?usp=sharing)
'test_multi.csv' (https://drive.google.com/file/d/1iUz15UEa6rg70E4CZWGZyJcMU81HRM_j/view?usp=sharing)
'valid_multi.csv' (https://drive.google.com/file/d/1OGITCFHiK0zcdSrkeOK3m6YRMpyjJhXN/view?usp=sharing)

Датасеты с данными по заболеваниям также можно получить:
1) запустив файл 'get_multidatas_ill.py' и
Имея файл 'ill_data.csv' (https://drive.google.com/file/d/102WQIVH5zrdRvG0BTfKY51wClV9_J3gx/view?usp=sharing),
который формируется 
из 'ptbxl_database.csv' (https://drive.google.com/file/d/1AIKKPeJVrtXuGKiHWhNQSF3ClJ5Tc812/view?usp=sharing), 
в столбце 'report' которого хранятся таргеты по заболеваниям и номера ЭКГ, соответствующие им
 и файла 'target_ills_data.py'
 __________________________________________________________________________________________________________________________________
 Datasets with data on diseases can also be obtained:
1) by running the file 'get_multidatas_ill.py' and
Having the file 'ill_data.csv' (https://drive.google.com/file/d/102WQIVH5zrdRvG0BTfKY51wClV9_J3gx/view?usp=sharing),
which is formed
from 'ptbxl_database.csv' (https://drive.google.com/file/d/1AIKKPeJVrtXuGKiHWhNQSF3ClJ5Tc812/view?usp=sharing),
in the 'report' column of which disease targets and ECG numbers corresponding to them are stored
  and the file 'target_ills_data.py'

запустить проект/ run code
```
python main.py
```
