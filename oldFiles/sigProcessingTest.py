import numpy as np
import matplotlib.pyplot as plt

#function to generate a sine wave signal

def make_signal(Hz,sample_rate):
	#input Hz - frequency of signal, sample rate of data


	#values for the time (on the x axis) - run from t=0 to t=1 second
	time_series  = (np.linspace(0, 2*np.pi*Hz, sample_rate))


	#Amplitude is the sine 
	amp = np.sin(time_series)

	return(list(amp))

#define a sampling rate of the time series
sample_rate = 400

#generate two signals of different frequency
sig_1 = (make_signal(500,sample_rate))
sig_2 = (make_signal(300,sample_rate))

#find the superposition - make arrays to add, not concatenate
combined_sig = np.array(sig_1) + np.array(sig_2)

combined_sig = list(combined_sig)

total_time = len(combined_sig)/sample_rate
#plot the total signal in time domain
print("The total time series length = {} sec (N points = {}) ".format(total_time, len(combined_sig)))

plt.figure(figsize=(20,3))

plt.plot(combined_sig)
plt.xticks(np.arange(0,total_time,step=0.01))
plt.ylabel("Amplitude")
plt.xlabel("Time (seconds)")

plt.show()
