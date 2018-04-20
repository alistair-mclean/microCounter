# microCounter
Welcome to the microCounter repository!

microCounter is a tool designed to assist with analysis of MicroBiological organisms. 
This project is deep in its early development stages, be prepared for significant overhauls in the near future. 
What you see here is merely a prototype of functionality, and things to come. 

# Installation
Follow these steps in order to install microCounter on your machine. 

## 1.) Install Python 
Go to https://www.python.org/downloads/ and download the latest version of Python for your machine. 

### Validate Python install
After Python has finished installing - open a terminal (or command prompt on Windows), type "pip --version", and press enter. If you see a response like 
PUT THE IMAGE HERE!!!
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

## Start microCounter
Assuming microCounter has been downloaded and extracted(or cloned) properly. And the installation requirement have been fulfilled. 
Open a command prompt and traverse to the microCounter directory. 

DIRECTORY PICTURE!!!!!!!!!

Type python main.py 


## Load an image an analyze

### Press load and select the image
LOAD PICTURE!!!
#### KNOWN ISSUE!! The application will not work properly if you load something besides an image. There isn't a validation step, yet. 

### Set the organism parameters
#### Organism Name 
The name of the organism - used for output files.
#### Color Thresholds 
The low and high of the color values which represent a potential organism. Used for filtering, and counting organisms. 

1.) Press either the low or high color button. 
2.) Hover over the image, and click on the pixel you wish to use as either the low or high threshold value. 
3.) Press enter. 
4.) Repeat for the other color. 

#### Size Range
Enter in the size range of the organism (in pixels). 


## Results
After analyzing, results can be found under microCounter/results/. 
The results of each analysis are recorded in a directory of the DATE_TIME the analysis was recorded at. 


### Images
The resulting images from the filtering, and post procesing can be found under microCounter/results/DATE_TIME/images. 
Here are some examples: 

EXAMPLE OUTPUT1 IMAGE!!

EXAMPLE OUTPUT2 IMAGE!!

EXAMPLE OUTPUT3 IMAGE!!


Included is a text file which includes the results about the analysis. Here's an example: 
>-----------------------------------------------------------------------
> Source file: C:/Users/alist/Documents/GitHub/microCounter/samples/sample1.tif
> Recorded on : 2018-04-20 at 13:05:53
> Organism: pseudomonas aeruginosa
>=============================== RESULTS ===============================
> Area of image: 624100 pixels.
> Population range of pseudomonas aeruginosa within 13123 and 4374 organisms.
> Size Range: [ 4px , 12px ]
> Based on the count of : 52493 pixels resulting from the given thresholds: [ 38 255   8] - [ 59 255 234]. 
> Percentage of area covered by pseudomonas aeruginosa is: 8.410991828232655%



# In the works
- microCounter is currently being redesigned to exist as a web service.
- Analysis setup will eventually be automatic. Providing more convenience with analyzing large amounts of data. 
- Manual analysis setup will be drastically improved. 
- 

# Usage
This software is free to use for anybody. Please do not redistribute copies of this software.  

