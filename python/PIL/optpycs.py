from PIL import Image
from base64 import b16encode
import sys
import os


#輝度算出
def  luminance(RGB):
	return 0.299*RGB[0]+0.587*RGB[1]+0.114*RGB[2]
#中央値出力
def median(ls):
	return sorted(ls)[len(ls) // 2]
#クラス
class PixelInfo:
	def __init__(self,x,y,Rgb):
		self.x = x
		self.y = y
		self.rgb = rgb


#画像読み込み
img = Image.open("256.png")
#ピクセルの抽出
img = img.convert("RGB")
pixels = img.load()
rgb = []
classlist = []
for y in range(img.size[1]):
	for x in range(img.size[0]):
		rgb.append(pixels[x,y])
		classlist.append(classlist(x,y,pixels[x,y]))
#再配置
for y in range(img.size[1]):
	for x in range(img.size[0]):
		i = x  + y * img.size[0]
		pixels[x,y] = rgb[i]
img.save("256out.png");
