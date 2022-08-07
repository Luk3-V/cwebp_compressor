# --cwebp_compressor.py--

# Fork that includes:
# - Create duplicate of directory
# - Recursivley search through sub directories
# - Remove & replace all non .webp images

# cmd> python cwebp_compressor.py folder-name 80

import sys
import os
from subprocess import call
from glob import glob
from shutil import copytree

# directory-name
path = sys.argv[1]
# quality of produced .webp images [0-100]
quality = sys.argv[2]

if int(quality) < 0 or int(quality) > 100:
	print("image quality out of range[0-100] ;/:/")
	sys.exit(0)

# create duplicate directory
dupePath = path+' (webp)'
copytree(path, dupePath)

# recursivley get paths of images
def getImages(dir_path):
	img_list = []
	for curr_path in glob(dir_path+'/*'):
		# if image, then append full image path
		# can use more image types(bmp,tiff,gif)
		if curr_path.endswith(".jpg") or curr_path.endswith(".png") or curr_path.endswith(".jpeg"):
			img_list.append(curr_path)
		# if directory, then append all image paths inside
		elif os.path.isdir(curr_path):
			img_list.extend(getImages(curr_path))
	return img_list

img_list = getImages(dupePath)

for img_path in img_list:
	# careful when modifying the below code
	cmd='cwebp \"'+img_path+'\" -q '+quality+' -o \"'+(img_path.split('.')[0])+'.webp\"'

	# running the above command
	call(cmd, shell=True)	
	
	# remove non .webp image
	os.remove(img_path)