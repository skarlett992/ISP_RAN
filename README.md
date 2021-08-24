# ISP_RAN
ECG
### Задача заключается в оценке значимости использования алгоритма/алгоритмов преобработки pqrst-комплексов при построении классификации ЭКГ.
Необходимо построить две модели: без учета обработанных qrst-комплексов в качестве признаков и с ними и оценить значимость признаков qrst-комплексов.
Нарушения ритма, которые стоит выбрать: синусовый ритм, аритмия, брадикардия, тахикардия, фибрилляция предсердий. 
Для сравнения моделей на одном и том же тестовом наборе в качестве метрик оценки качества стоит взять F1-score, Sensitivity, Specisifity, ROC-AUC для каждой патологии по отдельности и среднее значение по всем патологиям.

Дано:
1) два датасета (около 21000 ЭКГ в целевом) с аннотациями и метаданными по пациентам, которые включают в себя описание заболеваний данных пациентов по ЭкГ.
2) ЭКГ пациентов в файлах, каждый файл имеет ссылку, которая указана в метаданных пациента.


# Запуск работы
установить версию Python 3.7.7 
```
virtualenv venv --python=python3.7.7
```
установить зависимости
```
pip install -r requirements.txt
```
ссылки на некоторые файлы .csv для запуска программы:
1. основные, - обработанные сигналы ЭКГ, приведенные с помощью специальной библиотеки в датасет.
Их можно получить, запустив код по ссылке https://www.kaggle.com/natalyayurina/ptb-xl-dataset-wrangling

1) 'train_signal.csv'
https://drive.google.com/file/d/1gzUcPSQyrhLeMta-i79LGupPHueAiL9T/view?usp=sharing
2) 'test_signal.csv'
https://drive.google.com/file/d/1J70RMXu--lNVr4O7WBjxhjUyMS8M-Bmp/view?usp=sharing
3) 'valid_signal.csv'
https://drive.google.com/file/d/1EQbiR4SSlfnviqswYY43BrUT_luf2bdy/view?usp=sharing

2. датасеты с данными по заболеваниям (бинарные по каждому таргету): 

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

запустить проект
```
python main.py
```
