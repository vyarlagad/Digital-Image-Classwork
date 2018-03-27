import cv2
import numpy as np
import matplotlib.pyplot as plt


# Convert to Frequency Domain
def frequency_conv(img):
    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)
    return f_shift

def spatial_conv(f_shift):
    # Convert back to Spatial
    f_ishift = np.fft.ifftshift(f_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def appy_sobel(img):
    # Horizontal and Vertical Edges
    VE = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
    HE = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)
    return (VE, HE)

def edge_to_Freq(edges):
    # Vertical Edges Converted to Frequency Domain
    ve = np.fft.fft2(edges[0])
    ve_shift = np.fft.fftshift(ve)
    magn_ve_shift = np.log(np.abs(ve_shift)) + 1
    ve_shift_phase = np.angle(ve_shift)
    # Horizontal Edges Converted to Frequency Domain
    he = np.fft.fft2(edges[1])
    he_shift = np.fft.fftshift(he)
    magn_he_shift = np.log(np.abs(he_shift)) + 1
    he_shift_phase = np.angle(he_shift)
    return (ve_shift, he_shift)

def edge_to_spatial(shifted_edge):
    # Vertical Edges converted back to Spatial Domain
    ve_ishift = np.fft.ifftshift(shifted_edge[0])
    ve_ifft = np.fft.ifft2(ve_ishift)
    ve_ifft = ve_ifft.real
    # Horizontal Edges converted back to Spatial Domain
    he_ishift = np.fft.ifftshift(shifted_edge[1])
    he_ifft = np.fft.ifft2(he_ishift)
    he_ifft = he_ifft.real
    return (ve_ifft, he_ifft)
