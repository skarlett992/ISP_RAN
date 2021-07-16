# ISP_RAN
ECG
### скрин работающей программы: 
![alt text](https://github.com/skarlett992/ISP_RAN/blob/main/model_ecg_without_pqrst.png)

### Задача заключается в оценке значимости использования алгоритма/алгоритмов преобработки pqrst-комплексов при построении классификации ЭКГ.
Необходимо построить две модели: без учета обработанных qrst-комплексов в качестве признаков и с ними и оценить значимость признаков qrst-комплексов.
Нарушения ритма, которые стоит выбрать: синусовый ритм, аритмия, брадикардия, тахикардия, фибрилляция предсердий. 
Для сравнения моделей на одном и том же тестовом наборе в качестве метрик оценки качества стоит взять F1-score, Sensitivity, Specisifity, ROC-AUC для каждой патологии по отдельности и среднее значение по всем патологиям.

Дано:
1) два датасета (около 21000 ЭКГ в целевом) с аннотациями и метаданными по пациентам, которые включают в себя описание заболеваний данных пациентов по ЭкГ.
2) ЭКГ пациентов в файлах, каждый файл имеет ссылку, которая указана в метаданных пациента.


# Запуск работы


## Предобработка входных данных:

1) иметь локально сохраненные файлы, указанные в описании к задаче по ссылке https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1.zip
2) запустить код по ссылке https://www.kaggle.com/natalyayurina/ptb-xl-dataset-wrangling, получить на выходе датасеты, локально сохранить
3) иметь локально сохраненные файлы target_dict.ipynb и Natalya_Iurina_task.ipynb из текущего репозитория
4) запустить код в jupyter Natalya_Iurina_task.ipynb и в нем использовать датасеты-признаки из п.2
5) получить на выходе датасеты-признаки, которые будем подавать на вход в модель https://www.kaggle.com/natalyayurina/ecg-heartbeat-categorization-neural-network

## Запуск: 
6) Для запуска и реализации работы необходимо перейти по ссылке https://www.kaggle.com/natalyayurina/ecg-heartbeat-categorization-neural-network 


# Модель требует доработки: 
https://github.com/skarlett992/ISP_RAN/issues/1 


