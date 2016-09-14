# coding: UTF-8
from PIL import Image,ImageFont,ImageDraw,TgaImagePlugin
import os
from glob import glob
#画像に自分のファイル名を書き込む
def FileNamePrint(filepath):
    img = Image.open(filepath)
    font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 12)
    draw = ImageDraw.Draw(img)
    draw.text((10,10),filepath,font=font,fill='#F00')
    img.save(filepath)

#複数の拡張子に対応できるようにする
def AnyFileMatch(*ext):
    for ex in ext:
        files = glob(ex)
        for f in files:
            print(f)
            FileNamePrint(f)

#メイン処理
if __name__ == '__main__':
    AnyFileMatch('*.jpg','*.png','*.tga')#TGAだとエラー
