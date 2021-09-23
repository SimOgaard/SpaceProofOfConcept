### Concept:
Automatically annotates the SPoC dataset utilizing the fact that images were taken at the same position. Training on data created by this implementation; the model should be able to work on out-of-domain areas where images of the same area are not in the dataset.

### Implementation:
1. Creating an image representing the subtraction between an selected constant ideal image and all other images in the dataset.
    * Ideal image: Image of true ground, no obstructions like: clouds, boats, planes, etc. Is to be selected once for each dataset (agriculture_1_2019, gothenburg_2019, etc).
    * Subtraction is over the median of a given kernel (3x3, 5x5, 9x9...) of each pixel to account for small dissimilarities.
2. Converting subtracted images to binary by a threshold.
3. Refine the data by either:
    * Erosion followed by Dilation of binary image to remove smaller objects
        * Smaller objects: Planes, boats, waves. etc
    * Dilation followed by Erosion into blob detection to remove larger objects
        * Larger objects: Clouds, agriculture, construction. etc
4. Use binary images as a mask to the real images. And then either:
    * Train a model to classify by segmentation.
    * Train a model to detect objects by applying blob detection to binary images to get viable bounding boxes.
    * Apply segmentation to a dataset by extracting each object using the binary image and adding it to random background images. Could then be used to train a model to classify images. Or expand the dataset.

### Results:
Going through the actual implementation we find that more minute things could be extracted from the dataset without the need of neural nets. One minute thing could be extracting routes that boats take, by adding all binary images of smaller objects.

Distinguishing between objects of the same size seems to be difficult. Further implementation that utilizes each channel of the dataset could solve this problem. By using the fact that [different objects react differently by wavelength.](https://gisgeography.com/sentinel-2-bands-combinations/) We could for example utilize this fact to mask out all objects that are in water to distinguish between boats and similarly sized objects

Whether or not this would work it comes down to: how similar the images are.