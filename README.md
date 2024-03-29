# OpenCV Haar cascade with Non-Maxima Suppression
This simple project provides a `Detector` class extending the opencv `CascadeDetector`class with a new function: `detectAndFilter`.  
This function performs the detection using the cascade and filter the detections based on the score and their overlap to yield the best detections that do not overlap above the selected `overlap-threshold`.

For more details about Non-Maxima Suppression, you can refer to my [article](https://doi.org/10.1186/s12859-020-3363-7) about Multi-Template Matching, which uses a similar strategy (or other online resources).  
I also described/experimented with cascade deectors as part of my [PhD thesis](https://doi.org/10.11588/heidok.00030804).  
Here the NMS shipped with OpenCV is used.

# Installation
Using pip:  
`pip install haar-cascade-nms`

Then to use in your scripts:  
```python
from haarcascade import Detector
myDetector = Detector(filepathToCascade)
myDetector.detectAndFilter(image, etc...)
```

See the tutorial notebook for a more detailed documentation.  
