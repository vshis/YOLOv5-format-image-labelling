# labelsUnityPython
Code for generating labels for the synthesised black/white greyscale images. Where per overall image, there is a black/white image per object of interest.
Code that outputs the min/max x/y locations of white pixels on the image in YOLOv5 format into txt files. 
This is supplementary code that goes along with the cones generation image generation format of the Unity repo. 

The white pixels on black background represent the visible region of a cone. A label is then drawn as a bounding box of these pixels. The cone colour is passed to the label from the file name originally created by Unity. 
For every image with multiple cones on it, black/white images of individual cones are generated. This code outputs a .txt of all cones file per main image. 
For images with no cones on them, empty .txt files are generated. 
