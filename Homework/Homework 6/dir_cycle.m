%% cycle through all PNG files in a given directory
%% (and in this case display them)

%% change '*.png' in code below for other image types

cd INSERT_DIRECTORY_NAME;

list = dir('*.png');
number_of_files = size(list);




for i= 3: number_of_files(1,1)
    filename = list(i).name;
    I = imread(filename);
    imshow(I);
end