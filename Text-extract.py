
import cv2 
import pytesseract 

#location of Tesseract-OCR in my system 
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Read the input image
img = cv2.imread("a.jpeg") 
# Image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Finding Thershold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))

# Appplying dilation and finding contours
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 
im2 = img.copy() 

for i in contours: 
	x, y, w, h = cv2.boundingRect(i) 

	# Draw a rectangle
	rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
	 
	# Crop the image by its real size
	cropped = im2[y:y + h, x:x + w] 
		
	# Exracting text by using Ocr
	text = pytesseract.image_to_string(cropped) 

	file1 = open('output.txt', 'a') 
	file1.writelines(text) 
	file1.writelines("\n") 
	file1.close() 

file1.close() 

