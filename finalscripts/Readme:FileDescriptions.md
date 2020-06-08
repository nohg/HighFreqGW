Readme:File descriptions

1:Detector_data_PSD_final.ipynb
Calculate and plot one- and two-sided power spectral density of input detector data.

2:Detector_data_coincidence_analysis_Final.ipynb
Coincidence analysis on real detector data. Initial spectrogram calculations are made to produce necessary arrays. Time shift analysis is performed to calculate the background coincidences between two detection windows.

3:Noise_coincidence_analysis-Final.ipyn
Same coincidence analysis steps as taken in 2. using generated gaussian noise. Additionally, cross-correlation analysis techniques are performed on gaussian noise signal

4.Detector_data_specanalysis_cells_Final.ipynb
This notebook includes spectrogram analysis of both data streams from a single detector data file. We pick out a frequency range at the detector's resonant frequency and a reference range far from the resonant mode. The data is 'differenced' and the (un)differenced data is histogrammed. The steps in this notebook are written in individual cells

5.Detector_data_specanalysis_chunks_Final.ipynb
Spectrogram analysis mirrors that of 4. but is formatted into a function in a single cell, so that smaller 'chunks' of data can be operated upon and recombined later to form overall histograms.

6.Noise_specanalysis_chunks_Final.ipynb
Mirrors 5. but generates and analyses random gaussian noise data.
