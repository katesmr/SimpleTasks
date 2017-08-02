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
colors = im.convert('RGB').getcolors()
width, height = im.size
pix_val = list(im.getdata())

lest = im.getcolors(width*height)
print(pix_val)
print(lest)

print(create_hex_color_list(create_rgb_list(im)))
# print(create_color_list(create_rgb_list(im)))
rgb = [(255, 0, 0), (255, 255, 255), (0, 0, 0)]
print(create_color_list(rgb))


def sss(arr):
    length = len(arr)
    for i in range(1, length):
        el = arr[i]
        j = i
        while j > 0 and arr[j-1][0] < el[0]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = el

print(sss(lest))
print(lest)

