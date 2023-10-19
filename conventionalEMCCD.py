#conventional CCD
px = 4
readnoise = 7 * np.sqrt(px) 
QE = 0.48
dark_current = 0.5 * px
exposure_time = 0.000144
sensitivity = 1
iterations = 10000
for phph in np.arange(1,51,1):
    Signal = np.zeros(iterations)
    Background = np.zeros(iterations)
    for i in range(iterations):
        pelectrons =  np.random.poisson(QE*phph+exposure_time*dark_current)
        Signal[i] = np.round((pelectrons + np.random.normal(scale = readnoise))/sensitivity)
        Background[i] = np.round((np.random.poisson(exposure_time*dark_current) + np.random.normal(scale = readnoise))/sensitivity)
    np.savez("Amplitudes_optimal/Amplitudes_Reference_CCD" + str(phph), CCD_Signal = Signal, CCD_Background = Background)    
