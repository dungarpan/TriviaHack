from PIL import ImageGrab,ImageOps,Image,ImageEnhance, ImageFilter
import pytesseract
import time
from numpy import *
from search_script import search
 
def imageGrab():
	boxques = (48,370,410,430)
	boxop1	= (48,505,400,535)
	boxop2	= (48,595,400,625)
	boxop3	= (48,688,400,715)
	imgques   = ImageGrab.grab(boxques)
	imgques.save('imgques.jpeg')
	imgques = imgques.filter(ImageFilter.MedianFilter())
	imgques = ImageEnhance.Contrast(imgques)
	imgop1   = ImageGrab.grab(boxop1)
	imgop1.save('imgop1.jpeg')
	imgop2   = ImageGrab.grab(boxop2)
	imgop2.save('imgop2.jpeg')
	imgop3   = ImageGrab.grab(boxop3)
	imgop3.save('imgop3.jpeg')
	#time.sleep(1)
	text_ques = pytesseract.image_to_string(Image.open('imgques.jpeg'))
	print(text_ques)
	text_op1 = pytesseract.image_to_string(Image.open('imgop1.jpeg'))
	print(text_op1)
	text_op2= pytesseract.image_to_string(Image.open('imgop2.jpeg'))
	print(text_op2)
	text_op3 = pytesseract.image_to_string(Image.open('imgop3.jpeg'))
	print(text_op3)
	url='https://www.bing.com/search?q='
	url+=text_ques
	print(url)
	search(url)

def main():
	print("start")
	imageGrab()


main()