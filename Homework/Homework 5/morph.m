
% Reads in the image and converts to grayscale
img = rgb2gray(imread('cloth.jpg'));


% Disk structuring element
struct_element = strel('disk',10);

% Morphological Closed Image
closed_img = imclose(img,struct_element);


% Creates a threshold from the original image
level = graythresh(img);

% Generates the binary image from the closed image
% and the threshold of the original image
BW = imbinarize(closed_img,level);


% Takes in the perimeter of the defects in the binary image
perim = bwperim(BW);

% Generates the color used for contouring the defects
red = BW;
green = BW;
blue = BW;

% generate only one color and concatinate the rgb space
red(perim) = 0;
green(perim) = 0;
contour = 255*uint8(cat(3, red, green, blue));

% Overlay the contour with the original image
overlay = rgb2gray(imfuse(img,contour,'Scaling','joint'));

% Plots the images for comparison
figure;
subplot(141),imshow(img),title('Original Image')
subplot(142),imshow(closed_img),title('Closed Morph')
subplot(143),imshow(contour),title('Binary Image')
subplot(144),imshow(overlay),title('Overlay')
