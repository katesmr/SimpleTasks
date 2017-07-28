from PIL import Image
from webcolors import rgb_to_name


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def create_rgb_list(image):
    res = []
    pixels = list(image.getdata())
    for pixel in pixels:
        if pixel not in res:
            res.append(pixel)
    return res


def create_hex_color_list(rgb_list):
    res = []
    for pixel in rgb_list:
        res.append(rgb_to_hex(pixel))
    return res


def create_color_list(rgb_list):
    res = []
    for pixel in rgb_list:
        res.append(rgb_to_name(pixel))
    return res


im = Image.open('/home/kate/Pictures/Untitled.png')
# colors = img.convert('RGB', colors=5).getcolors()
width, height = im.size
pix_val = list(im.getdata())

lest = im.getcolors(width*height)
print(pix_val)
print(lest)

print(create_hex_color_list(create_rgb_list(im)))
# print(create_color_list(create_rgb_list(im)))
rgb = [(255, 0, 0), (255, 255, 255), (0, 0, 0)]
print(create_color_list(rgb))

"""
px=ImageGrab.grab().load()
for y in range(0,100,10):
    for x in range(0,100,10):
        color=px[x,y]
"""