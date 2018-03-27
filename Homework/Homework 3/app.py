import cv2
import matplotlib.pyplot as plt
from partOne import *

def main():
    # Creates the image path to be read into a variable
    img_path = "/Users/vyarlaga/Desktop/Digital-Image-Classwork/images/img1"
    img = cv2.imread(img_path,0)

    img2_path = "/Users/vyarlaga/Desktop/Digital-Image-Classwork/Images/"
    img2 = cv2.imread(img2_path,0)

    img3_path = "/Users/vyarlaga/Desktop/Digital-Image-Classwork/Images/"
    img3 = cv2.imread(img3_path)

    f_shift = frequency_conv(img)
    img_back = spatial_conv(f_shift)
    edges = appy_sobel(img)
    shifted_edge = edge_to_Freq(edges)
    edges_ifft = edge_to_spatial(shifted_edge)

    # Horizontal and Vertical Edges merged together to form Image 2
    merged_img = cv2.add(edges_ifft[0],edges_ifft[1])








    # Plotting the Horizontal & Vertical Edges in Spatial Domain & Magnitude and Phase Spectrum in the Frequency Domain, and the Merged Image
    plt.figure(figsize=(20,20))
    plt.subplot(521),plt.imshow(edges[0], cmap = 'gray'),plt.title('Vertical Edges'),plt.xticks([]), plt.yticks([])
    plt.subplot(522),plt.imshow(edges[1], cmap = 'gray'),plt.title('Horizontal Edges'),plt.xticks([]), plt.yticks([])



    plt.subplot(527),plt.imshow(ve_ifft, cmap = 'gray'),plt.title('Converted Back Vertical Edges'),plt.xticks([]), plt.yticks([])
    plt.subplot(528),plt.imshow(he_ifft, cmap = 'gray'),plt.title('Converted Back Horizontal Edges'),plt.xticks([]), plt.yticks([])


    plt.subplot(529),plt.imshow(merged_img, cmap = 'gray'),plt.title('Merged Image'),plt.xticks([]), plt.yticks([])
    plt.subplot(5,2,10),plt.imshow(img2, cmap = 'gray'),plt.title('Image 2'),plt.xticks([]), plt.yticks([])
    plt.show()











if __name__ == '__main__':
    main()


