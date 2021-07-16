# ISP_RAN
ECG
### Задача заключается в оценке значимости использования алгоритма/алгоритмов преобработки pqrst-комплексов при построении классификации ЭКГ.
Необходимо построить две модели: без учета обработанных qrst-комплексов в качестве признаков и с ними и оценить значимость признаков qrst-комплексов.
Нарушения ритма, которые стоит выбрать: синусовый ритм, аритмия, брадикардия, тахикардия, фибрилляция предсердий. 
Для сравнения моделей на одном и том же тестовом наборе в качестве метрик оценки качества стоит взять F1-score, Sensitivity, Specisifity, ROC-AUC для каждой патологии по отдельности и среднее значение по всем патологиям.

Дано:
1) два датасета (около 21000 ЭКГ в целевом) с аннотациями и метаданными по пациентам, которые включают в себя описание заболеваний данных пациентов по ЭкГ.
2) ЭКГ пациентов в файлах, каждый файл имеет ссылку, которая указана в метаданных пациента.

Решение:
Для решения задачи необходимо 
#### Вариант1: 

Иметь доступ к предобработанным датасетам на вход на kaggle по ссылке:
https://www.kaggle.com/natalyayurina/ecg-heartbeat-categorization-neural-network 
(работа адаптирована из кода https://www.kaggle.com/basharalkuwaiti/ecg-heartbeat-categorization-neural-network) 


# Модель требует доработки!
В данный момент она использует только первый из таргетов (синусовый ритм), расходует слишком много памяти, работает медленно.
Также этот код является первым вариантом модели (без использования признаков pqrst-комплексов). 

Для запуска модели с признаками pqrst-комплексов необходимо предобработать промежуточные файлы csv ЭКГ любым из предложенных в коде https://github.com/berndporr/py-ecg-detectors.git алгоритмов,
склеить с файлами на вход для модели https://www.kaggle.com/natalyayurina/ecg-heartbeat-categorization-neural-network 
Затем методом p-value посчитать статистичекую значимость (на основании посчитанных метрик и признаков pqrst)

Также необходимо добавить алгоритм, позволяющий работать с меньшим объемом данных на вход либо увеличить мощность  (в репозитории скрин, где модель обрабатывалась несколько часов и не прошла все эпохи)

#### Вариант2: 

Чтобы получить датасеты, которые подаем на вход по ссылке https://www.kaggle.com/natalyayurina/ecg-heartbeat-categorization-neural-network, необходимо:

1) иметь локально сохраненные файлы, указанные в описании к задаче по ссылке https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1.zip
2) запустить код по ссылке https://www.kaggle.com/natalyayurina/ptb-xl-dataset-wrangling, получить на выходе датасеты, локально сохранить
3) иметь локально сохраненный файл (вспомогательный) target_dict.ipynb и Natalya_Iurina_task.ipynb
4) запустить код в jupyter Natalya_Iurina_task.ipynb и в нем использовать датасеты-признаки из п.2
5) получить на выходе датасеты-признаки, которые будем подавать на вход в модель https://www.kaggle.com/natalyayurina/ecg-heartbeat-categorization-neural-network


