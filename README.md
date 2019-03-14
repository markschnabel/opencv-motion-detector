# opencv-motion-detector
A home made motion detector built with Python and OpenCV. 

![MotionDetector](https://user-images.githubusercontent.com/36283037/54394894-94590480-4684-11e9-918c-3553e29f7601.jpg)

### Usage
This program can be used to detect motion in a video. It can utilize video that is live streamed or pre-recorded.

*NOTE*: The program utilizes a background subtraction algorithm to detect motion. This means that the ideal use case is with a fixed camera mounted somewhere. Under these circumstances it would be best put to use by powering something like a security camera.

### Running the program
If you would like to run this program you can do so by following the following steps:

#### Prerequisites

These steps assume that you have the following software installed on your computer:
```
Python3.7
virtualenv
```
Run the following commands from a new terminal or CMD window in the directory you want to create the project in:
```
git clone https://github.com/markschnabel/opencv-motion-detector
cd opencv-motion-detector
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
python main.py
```
The steps above will clone the project into a directory "opencv-motion-detector", create a new python virtual environment, use it to install the requirements and run the program.

Upon execution the program will automatically try to access your default capture device unless you specify a path to a video file to use the program with. To use a video run the program with the command:
 ```
 python main.py -v [YOUR PATH HERE]
 ```

#### Arguments
The program is controlled via CMD line arguments. To see the list of available
arguments at any time run `python main.py --help`. 

Upon execution you should see this output:
```
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Amount of time in seconds to delay the program before
                        starting.
  -m MIN_AREA, --min-area MIN_AREA
                        Minimum area in pixels difference to be considered
                        actual motion.
  -t THRESH, --thresh THRESH
                        Level of threshold intensity.
  -v VIDEO_PATH, --video-path VIDEO_PATH
                        Path to video file. If not provided the default video
                        recording device on your system will be used.
```

**Reference**
* **Delay** - Amount of time in seconds to delay the program before starting. This is useful for if you need to set up the camera and get out of the way before execution.
* **Min Area** - Minimum area in pixels difference to be considered actual motion. This effects the overall sensitivity of the motion detector. Lowering the area will make the program much more likely to detect motion. Should be used with caution as setting it too low will have the camera become overly sensitive to things such as background noise or scratches.
* **Thresh** - The level of threshold intensity. This can be useful for tweaking the program to run under different lighting conditions. Increasing it will help it to run in particularly bright conditions, howeverleaving it as is should be sufficient for most use cases.
* **Video Path** - Path to a video file you would like to run the program with. Program defaults to using your device's default capture device.

## Authors
* **Mark Schnabel** - *Sole contributor* 
    * GitHub - [markschnabel](https://github.com/markschnabel)
    * Linked In - [mark-j-schnabel](https://github.com/markschnabel)
    * [mark.schnabel@markschnabel.com](mailto:mark.schnabel@markschnabel.com)

## License
 
The MIT License (MIT)

Copyright (c) 2019 Mark Schnabel <mark.schnabel@markschnabel.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
