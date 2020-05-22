# Image-Analysis
## By Parth Doshi
Image Processing using Python PIL Library to check for Cracks, Corrosion and Deformities on different surfaces of the structure.
</br>
# Description of Image Analysis Module
ImageChops.difference() function from PIL Library is used to check for difference in two images.
This program is designed for image processing for the purpose of crack detection by comparing two different images.
Our idea is to take images from a particular site on the bridge over a certain time interval and the feeding it into the developed system in order to understand the change that it has gone through.
The program also computes a numerical value for the percentage difference in the two images. 
Pre-processing done on images converts them to greyscale first in order to reduce the requirement for computational resources.
A threshold can be set which, when surpassed, will require the respective authority being notified.
We are also sending the Percentage Difference Data to Cloud and to our Output App and sending it along with timestamps and input and result images to the specified EMail Address. 
</br>
# Modules
- [PIL](https://pypi.org/project/Pillow/)
- [cv2](https://pypi.org/project/opencv-python/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [firebase](https://pypi.org/project/firebase/)
- [email](https://pypi.org/project/email/)
- [stmplib](https://docs.python.org/3/library/smtplib.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [datetime](https://docs.python.org/3/library/time.html?highlight=time#module-time)

# Screenshots of GUI

## Basic Screen
![BasicScreen](https://github.com/Bridge-Health-Monitoring-System/Image-Analysis/blob/master/Outputs/Basic%20Screen.png)
<br/>
## First Spectrogram
![FirstSpectrogram](https://github.com/Bridge-Health-Monitoring-System/Image-Analysis/blob/master/Outputs/First%20Image.png)
<br/>
## Second Spectrogram
![SecondSpectrogram](https://github.com/Bridge-Health-Monitoring-System/Image-Analysis/blob/master/Outputs/Second%20Image.png)
<br/>
## Result
![Result](https://github.com/Bridge-Health-Monitoring-System/Image-Analysis/blob/master/Outputs/Result.png)
<br/>
