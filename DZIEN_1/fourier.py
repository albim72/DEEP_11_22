import numpy as np
import matplotlib.pyplot as plt

#opiszemy 2 funkcje falowe oparte na różnych częstotliwościach
#dokonamy złożenia tych 2 funkcji w 1 funkcję falową
#wykonamy transformatę Fouriera na tym złożeniu
#wykonamy wykres prezentujący wszystkie 4 wyniki( 4 wykresy na jednej figurze)

samplingFrequency = 100
samplingInterval = 1/samplingFrequency

beginTime=0
endTime = 10

#cześtotliwość dwóch sygnałów w [Hz]
siglnal1Frequency = 4
siglnal2Frequency = 7

time = np.arange(beginTime,endTime,samplingInterval)

#deklaracja funkcji falowych
amplitude1 = np.sin(2*np.pi*siglnal1Frequency*time)
amplitude2 = np.sin(2*np.pi*siglnal2Frequency*time)

#tworzymy wykresy wewnętrzne
figure,axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)

#pierwszy wykres funkcja [4Hz]

axis[0].set_title('funkcja falowa o częstotliwości 4 Hz')
axis[0].plot(time,amplitude1)
axis[0].set_xlabel('Czas')
axis[0].set_ylabel('Amplituda')

#drugi wykres funkcja [7Hz]

axis[1].set_title('funkcja falowa o częstotliwości 7 Hz')
axis[1].plot(time,amplitude2)
axis[1].set_xlabel('Czas')
axis[1].set_ylabel('Amplituda')

#złożenie obu funckji falowych

amplitude = amplitude1 + amplitude2

#trzeci wykres złożenie funkcji

axis[2].set_title('złożenie dwóch funkcji falowych o częstotliwości 4Hz i 7 Hz')
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas')
axis[2].set_ylabel('Amplituda')

#Transformata Fouriera -> normalizacja amplitudy
tpCount = len(amplitude)
fourierTransform = np.fft.fft(amplitude)/tpCount

fourierTransform = fourierTransform[range(int(tpCount/2))]
values = np.arange(int(tpCount/2))
timePeriod = tpCount/samplingFrequency
frequencies = values/timePeriod

#czwarty wykres Transformata Fouriera

axis[3].set_title('Transformata Fouriera obrazująca złożenie funkcji falowych')
axis[3].plot(frequencies,abs(fourierTransform))
axis[3].set_xlabel('Częstotliwość')
axis[3].set_ylabel('Amplituda')

plt.show()
