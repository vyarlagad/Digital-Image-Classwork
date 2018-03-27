# Part 3

# Magnitude and Phase Spectrum of Image 1
magn_spectrum = np.log(np.abs(f_shift))
f_phase = np.angle(f_shift)

# Magnitude and Phase Spectrum of Image 2
magn_spectrum3 = np.log(np.abs(f_shift3))
f_phase3 = np.angle(f_shift3)

plt.subplot(221),plt.imshow(magn_spectrum, cmap = 'gray'),plt.title('Magnitude Spectrum'),plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(f_phase, cmap = 'gray'),plt.title('Phase Spectrum'),plt.xticks([]), plt.yticks([])
plt.subplot(221),plt.imshow(magn_spectrum3, cmap = 'gray'),plt.title('Magnitude Spectrum'),plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(f_phase3, cmap = 'gray'),plt.title('Phase Spectrum'),plt.xticks([]), plt.yticks([])
