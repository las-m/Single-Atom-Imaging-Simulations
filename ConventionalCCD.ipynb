import numpy as np

# Estimate signal on a conventional CCD
px = 4  # How many pixels is the signal distributed over
readnoise = 7 * np.sqrt(px) # Readout noise per pixel
QE = 0.48 # Quantum efficiency
dark_current = 0.5 # Dark current per pixel and second (not very important)
dark_current = dark_current * px
exposure_time = 0.000144 # Exposure time (not very important)
sensitivity = 1 # camera sensitvity (electrons to ADU conversion)
iterations = 10000
for phph in np.arange(1,51,1):
    Signal = np.zeros(iterations)
    Background = np.zeros(iterations)
    for i in range(iterations):
        pelectrons =  np.random.poisson(QE*phph+exposure_time*dark_current) # primary electrons
        Signal[i] = np.round((pelectrons + np.random.normal(scale = readnoise))/sensitivity) # electron to ADU conversion
        Background[i] = np.round((np.random.poisson(exposure_time*dark_current) + np.random.normal(scale = readnoise))/sensitivity) # Calculate the Background Signal
    np.savez("Amplitudes_optimal/Amplitudes_Reference_CCD" + str(phph), CCD_Signal = Signal, CCD_Background = Background) # Save background and signal brightnesses for later analysis
