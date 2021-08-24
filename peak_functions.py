from unique_ecg_without_peaks import get_unfiltered_ecg
import matplotlib.pyplot as plt
from ecgdetectors import Detectors
import pandas as pd
import numpy as np

def detect(unfiltered_ecg, fs=250):
    detectors = Detectors(fs)
    r_peaks = []
    # r_peaks_two_average = detectors.two_average_detector(unfiltered_ecg)
    # r_peaks = detectors.matched_filter_detector(unfiltered_ecg,"templates/template_250hz.csv")
    # r_peaks_swt = detectors.swt_detector(unfiltered_ecg)
    # r_peaks_engzee = detectors.engzee_detector(unfiltered_ecg)
    # r_peaks_christ = detectors.christov_detector(unfiltered_ecg)
    # r_peaks_ham = detectors.hamilton_detector(unfiltered_ecg)
    r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg)
    # r_peaks.append(sum(r_peaks_two_average, r_peaks_swt, r_peaks_engzee, \
    #               r_peaks_christ, r_peaks_ham, r_peaks_pan_tom)/(r_peaks_two_average, \
    #               r_peaks_swt, r_peaks_engzee, \
    #               r_peaks_christ, r_peaks_ham, r_peaks_pan_tom).count())

    return r_peaks
def visualize(unfiltered_ecg, r_peaks):
    plt.figure()
    plt.plot(unfiltered_ecg)
    plt.plot(r_peaks, unfiltered_ecg[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.show()

# функция, возвращающая словарь из пиков к конкретному экг
def get_peaks(df, ecg_id):
    list_of_peaks = []
    num_channels = []
    ecg_unique = get_unfiltered_ecg(df, ecg_id)
    ecg_data = ecg_unique.to_numpy()

    # подавать несколько каналов (пики попеременно)
    for num_channel in range(ecg_data.shape[1]):
        unfiltered_ecg = ecg_data[:, num_channel]
        r_peaks = detect(unfiltered_ecg, 100)
        # visualize(unfiltered_ecg, r_peaks)
        list_of_peaks.append(r_peaks)
        num_channels.append(f'channel-{num_channel}')

        dict_peaks = dict(list(zip(num_channels, list_of_peaks)))
    #     dict_peaks_list[ecg_id_data] = dict_peaks

    #     peaks_data = pd.DataFrame(dict_peaks_list).T
    return dict_peaks


# функция, возвращающая фрейм из пиков для дальнейшего слияния с общими данными по этому экг
def pad_nan_peaks(dict_peaks, pad_value=9999):
    len_max = 0
    for channel, list_peaks in dict_peaks.items():
        if len_max < len(list_peaks):
            len_max = len(list_peaks)

    for channel, list_peaks in dict_peaks.items():
        dict_peaks[channel] = np.pad(list_peaks, (0, len_max - len(list_peaks)), 'constant',
                                     constant_values=pad_value)

    peaks_df = pd.DataFrame(dict_peaks)

    return peaks_df