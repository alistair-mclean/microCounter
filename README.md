# microCounter

![microCounter](https://github.com/alistair-mclean/microCounter/blob/master/res/main.png?raw=true)

Welcome to the microCounter repository!

microCounter is a tool designed to assist with analysis of images of microorganisms. 
This project is deep in its early development stages, be prepared for significant overhauls in the near future. 
What you see here is merely a prototype of functionality, and things to come. 

## Features
- Filtering of organisms within an image. 
- Population estimates of the selected organism.
- Post processes the image to detect images (FAR TOO SENSITIVE).
- Outputs results in text and image format. 

# Installation
Follow these steps in order to install microCounter on your machine. 

## 1.) Install Python 
Go to https://www.python.org/downloads/ and download the latest version of Python for your machine. 

### Validate Python install
After Python has finished installing - open a terminal (or command prompt on Windows), type "pip --version", and press enter. If you see a response like 

![pip install](https://github.com/alistair-mclean/microCounter/blob/master/res/pipVersion.png?raw=true)


If you get an error, Python or pip may not be installed properly and you may have to do some further troubleshooting depending upon your issue. 

You may need to update pip. 
For Mac and Linux users type: 
> pip install --upgrade pip
For Windows users type: 
> python -m pip install --upgrade pip

## 2.) Install Python packages

### OpenCV
Type the following command into the command line:
>pip install opencv-python

### Kivy 
Install Kivy for your machine by following this installation reference: https://kivy.org/docs/installation/installation.html

### Tkinter
Type the following command into the command line:
>pip install tkinter

# Using microCounter
The following are instructions on how to properly use micrCounter in its current state. 

## Start microCounter
Assuming microCounter has been downloaded and extracted(or cloned) properly. And the installation requirement have been fulfilled. 
Open a command prompt and traverse to the microCounter directory. 
![Root Directory](https://github.com/alistair-mclean/microCounter/blob/master/res/rootDirectory.png?raw=true)

Enter into the command line: 
> python main.py 


## Load an image and analyze

### 1.) Press load and select the image
Load the image
![Load Dialog](https://github.com/alistair-mclean/microCounter/blob/master/res/loadImage.png?raw=true)

After the image has been loaded, you should see it appear in the interface. 
![Loaded Image](https://github.com/alistair-mclean/microCounter/blob/master/res/loadedImage.png?raw=true)

#### KNOWN ISSUE!! The application will not work properly if you load something besides an image. There isn't a validation step, yet. 

## 2.) Set the organism parameters
![Organism Parameters](https://github.com/alistair-mclean/microCounter/blob/master/res/organismParameters.png?raw=true)

### Organism Name 
The name of the organism - used for output files.

### Color Thresholds 
The low and high of the color values which represent a potential organism. Used for filtering, and counting organisms. THIS IS CURRENTLY BEING REDISGNED - DON'T WORRY!

#### 1. Press either the low or high color button.  (Seen highlighted in blue)
![Color Select](https://github.com/alistair-mclean/microCounter/blob/master/res/selectColor.png?raw=true)

#### 2. Hover over the image, and click on the pixel you wish to use as either the low or high threshold value. 
![Selection](https://github.com/alistair-mclean/microCounter/blob/master/res/colorSelection.png?raw=true)
#### 3. Press enter. 
#### 4. Repeat for the other color. 



### Size Range
Enter in the size range of the organism (in pixels). 

## 3.) Analyze 
If you have successfully completed steps 1 and 2, then you are ready to Analyze!
![Ready to Analyze](https://github.com/alistair-mclean/microCounter/blob/master/res/readyToAnalyze.png?raw=true)

## 4.) Results
After analyzing, results can be found under microCounter/results/. 
The results of each analysis are recorded in a directory of the DATE_TIME the analysis was recorded at. 


### Images
The resulting images from the filtering, and post procesing can be found under microCounter/results/DATE_TIME/images. 
Here are some examples: 

#### Original
![Original](https://github.com/alistair-mclean/microCounter/blob/master/results/20180420_130553/images/original.jpg?raw=true)

#### Mask
![Mask](https://github.com/alistair-mclean/microCounter/blob/master/results/20180420_130553/images/pseudomonas%20aeruginosa_Mask.jpg?raw=true)

#### Result
![Result](https://github.com/alistair-mclean/microCounter/blob/master/results/20180420_130553/images/pseudomonas%20aeruginosa_Result.jpg?raw=true)

#### Post processed
![Post Processed](https://github.com/alistair-mclean/microCounter/blob/master/results/20180420_130553/images/pseudomonas%20aeruginosa_PostProcessed.jpg?raw=true)


Included is a text file which includes the results about the analysis. Here's an example: 
```
-----------------------------------------------------------------------
Source file: C:/Users/alist/Documents/GitHub/microCounter/samples/sample1.tif
 Recorded on : 2018-04-20 at 13:05:53
 Organism: pseudomonas aeruginosa
=============================== RESULTS ===============================
 Area of image: 624100 pixels.
 Population range of pseudomonas aeruginosa within 13123 and 4374 organisms.
 Size Range: [ 4px , 12px ]
 Based on the count of : 52493 pixels resulting from the given thresholds: [ 38 255   8] - [ 59 255 234]. 
 Percentage of area covered by pseudomonas aeruginosa is: 8.410991828232655%
```


# In the works
- microCounter is currently being redesigned to exist as a web service.
- Analysis setup will eventually be automatic. Providing more convenience with analyzing large amounts of data. 
- Manual analysis setup will be drastically improved. 
- 

# Usage
This software is free to use for anybody. Please do not redistribute copies of this software.  

