# coding: utf-8

import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageFont, ImageDraw

# ------------------------------------------------------------------------
##
# @brief 
# ------------------------------------------------------------------------
class CreateBarcodeImage:

    _font_size = 10
    _font_color = (0, 0, 0)

    # ------------------------------------------------------------------------
    ##
    # @brief バーコードの作成
    #
    # @param input_code
    #
    # @return 
    # ------------------------------------------------------------------------
    @staticmethod
    def create_image(input_code, text):
        code_format = 'code128'
        code = barcode.get_barcode(code_format, input_code, writer=ImageWriter())
        filename = code.save(code)
        image = Image.open(filename)

        # メッセージ追加
        CreateBarcodeImage.add_text(image, text, (CreateBarcodeImage._font_size, 210))

        # 保存
        image.save(filename)
        print u'保存しました。' + filename
        return filename

    # ------------------------------------------------------------------------
    ##
    # @brief テキストを追加
    #
    # @param image
    # @param text
    # @param pos
    #
    # @return 
    # ------------------------------------------------------------------------
    @staticmethod
    def add_text(image, text, pos):
        font_path = 'C:/Windows/Fonts/msgothic.ttc'
        draw = ImageDraw.Draw(image)
        draw.font = ImageFont.truetype(font_path, CreateBarcodeImage._font_size)
        draw.text(pos, text, CreateBarcodeImage._font_color)

# ------------------------------------------------------------------------
##
# @brief メイン
# ------------------------------------------------------------------------
if __name__ == '__main__':
    print barcode.PROVIDED_BARCODES
    CreateBarcodeImage.create_image(u'AT2RCGN3B', u'')
    CreateBarcodeImage.create_image(u'AT3RCGN3B', u'')
