
# Part 2

# Collects data for rows and columns of the image
rows, cols = img3.shape

# Shifts the image to Frequency Domain
fft = np.fft.fft2(img)
f_shift3 = np.fft.fftshift(fft)

# Collects data to center the rows and columns
crow,ccol = rows//2 , cols//2

# Creates a mask with size of 50x50 with center square is 1 and the remaining are all zeros
mask = np.zeros((rows,cols), np.uint8)
mask[crow-25:crow+25, ccol-25:ccol+25] = 1

# LPF: Low Pass Filter
# Applies a convolution of the Frequency Domain image and the mask to create a Low Pass Filter Image
LPF = f_shift3*mask
f_ishift3 = np.fft.ifftshift(LPF)

# Converts low pass filtered image back into Spatial Domain
img_back3 = np.fft.ifft2(f_ishift3)
img_back3 = np.abs(img_back3)

# Plot the Original Image and Low Pass Filter Image
plt.subplot(121),plt.imshow(img, cmap = 'gray'),plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray'),plt.title('Image after LPF'), plt.xticks([]), plt.yticks([])

# HPF: High Pass Filter
# Applies a window to remove all of the low frequencies to the shifted image
f_shift3[crow-15:crow+15, ccol-15:ccol+15] = 0

# Shifts image back to Spatial Domain passing through a High Pass Filter
f_ishift3 = np.fft.ifftshift(f_shift3)
hpf_img_back = np.fft.ifft2(f_ishift3)
hpf_img_back = hpf_img_back.real

# Plots Image 3 and the image after being filtered
plt.figure()
plt.subplot(121),plt.imshow(img3, cmap = 'gray'),plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(hpf_img_back, cmap = 'gray'),plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.show()
