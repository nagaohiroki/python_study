# coding : utf-8

from PIL import Image, ImageFilter

def main():
    img_path = 'test1.png'
    img = Image.open(img_path)
    img.convert('RGB')
    #resize = img.resize((1600,1600))
    #resize.convert('RGB')
    print img.mode
    result = img.filter(ImageFilter.FIND_EDGES)
    #result.save('up.png', 'png', quality=100)

def filter(img):
    size_x, size_y = img.size
    for y in range(size_y):
        for x in range(size_x):
            img.putpixel( (x,y), (10, 0, 255, 255))

def liner(x, y, pixel):
    return (x, y,10,10)
if __name__ == '__main__':
    main()
