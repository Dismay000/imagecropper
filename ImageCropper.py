""" 
This is program for cropping A4 images by half (A4 to A5 converter)
All comments are in code

!!!!!!!PIL (pillow) module is required!!!!!!!
"""


from PIL import Image, ImageOps # importing modules
import os
import datetime
import time
import shutil

width = shutil.get_terminal_size().columns # for centering 
print(f"Hello! Current data and time is {datetime.datetime.now()}".center(width))

images = []
names = []

start_lines = ["If you want to crop all photos (A4 -> A5) in current directory", "TYPE 1", "Else if you want to choose files to crop", "TYPE 0"]
# up_or_down_lines = ["If you want to crop all photos (A4 -> A5) in current directory", "TYPE 1", "Else if you want to choose files to crop", "TYPE 0"]

for line in start_lines:
	print(line.center(width)) # printing centered start message

alert_fisrt = input()

while alert_fisrt != "0" and alert_fisrt != "1":
	alert_fisrt = input("Incorrect input! Type 0 or 1 again: ") # choosing working mode - 0 or 1

print()

if alert_fisrt == "0":
	print("Images in current directory: ", end = " ")

	for current_dir, dirs, files in os.walk("."):
	    for i in files:
	    	if i.endswith(".jpg") or i.endswith(".png"):
	    		print(i, end=" | ") # if alert_fist == 0 all images in direcrory are below and user're choosing files that he want to crop
	print()
	

	print("Enter filenames separated by space:", end=" ")
	images = [i for i in input().split()]

	while len(images) < 1:
		print("List is empty! Enter filenames again:", end=" ") # if user entered nothing
		images = [i for i in input().split()]

	print(f"Entered filenames: {images}") # showing entered files


else:
	for current_dir, dirs, files in os.walk("."):
	    for i in files:
	        if i.endswith(".jpg") or i.endswith(".png"):
	            images.append(i)

	if len(images) == 0:
	    print("I don't see a single image. Check .py file location")
	    exit() # if there is nothing in the directiory - exit

	print()
	print(f"All images in directory: {images}") # else just showing all images

print()

# img_open = Image.open(i)
# width, height = img_open.size # detecting width and height

# print("What part of A4 image should I crop? If upper, type 0. If lower, type 1:", end = " ")
# alert_second = input()

# while alert_second != "0" and alert_second != "1":
# 	alert_second = input("Incorrect input! Type 0 or 1 again: ")
# if alert_second == "0":
# 	border = (0, height//2, 0, 0)
# else:
# 	border = (0, 0, 0, height//2)

# for i in range(1, len(images)+1):
#     time_now = datetime.datetime.now().strftime('%Y %b %d %H.%M.%S.%f')
#     name = f"{time_now} - {str(i)}.jpg"
#     names.append(name)

print()

# print(f"Names of cropped and saved images: {names}")

for i in images:
	img_open = Image.open(i)
	width, height = img_open.size # detecting width and height

	print("What part of A4 image should I crop? If upper, type 0. If lower, type 1:", end = " ")
	alert_second = input()

	while alert_second != "0" and alert_second != "1":
		alert_second = input("Incorrect input! Type 0 or 1 again: ")
	if alert_second == "0":
		border = (0, height//2, 0, 0)
	else:
		border = (0, 0, 0, height//2)
	im_crop = ImageOps.crop(img_open, border)
	im_crop.save(names[images.index(i)])
print(f"Names of cropped and saved images: {names}")