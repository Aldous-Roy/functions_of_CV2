Image Processing with OpenCV

This program demonstrates various image processing techniques using OpenCV. It performs operations such as converting an image to grayscale, applying Gaussian blur, detecting edges, and performing morphological operations like dilation and erosion. Additionally, it resizes the image to a specified size.

Requirements

	•	Python 3.x
	•	OpenCV (cv2)
	•	NumPy

You can install the required packages using pip:
pip install opencv-python-headless numpy
Program Overview

The program performs the following operations on an input image:

	1.	Load and Display Image: Reads and displays the original image.
	2.	Convert to Grayscale: Converts the image to grayscale and displays it.
	3.	Apply Gaussian Blur: Applies Gaussian blur to the image and displays it.
	4.	Edge Detection: Uses Canny edge detection on the blurred image and displays the result.
	5.	Dilation: Performs dilation on the original image and displays it.
	6.	Erosion: Performs erosion on the original image and displays it.
	7.	Resize: Resizes the image to a new dimension and displays it.

	•	Load and Display Image:
	•	cv.imread("./photos/cat.jpeg"): Reads the image from the specified path.
	•	cv.imshow("Normal", img): Displays the original image.
	•	Convert to Grayscale:
	•	cv.cvtColor(img, cv.COLOR_BGR2GRAY): Converts the image to grayscale.
	•	cv.imshow("Grayscale", gray): Displays the grayscale image.
	•	Apply Gaussian Blur:
	•	cv.GaussianBlur(img, (15, 15), 2): Applies Gaussian blur with a kernel size of 15x15 and a standard deviation of 2.
	•	cv.imshow("Blurring", blur): Displays the blurred image.
	•	Edge Detection:
	•	cv.Canny(blur, 125, 175): Detects edges in the blurred image with specified thresholds.
	•	cv.imshow("Edges", edges): Displays the edges.
	•	Dilation:
	•	cv.dilate(img, kernel_dilate, iterations=8): Performs dilation using a 3x3 kernel for 8 iterations.
	•	cv.imshow("Dilated", dilated): Displays the dilated image.
	•	Erosion:
	•	cv.erode(img, kernel_erode, iterations=5): Performs erosion using a 5x5 kernel for 5 iterations.
	•	cv.imshow("Eroding", eroded): Displays the eroded image.
	•	Resize:
	•	cv.resize(img, (100, 100)): Resizes the image to 100x100 pixels.
	•	cv.imshow("Resized", resize): Displays the resized image.
kindly change the path according to your system so that it works perfectly
