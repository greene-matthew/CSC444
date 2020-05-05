from PIL import Image
import random

# the images
INPUT_IMAGE = "input.png"
AND_IMAGE = "and.png"
OR_IMAGE = "or.png"
XOR_IMAGE = "xor.png"

# get the input image
img = Image.open(INPUT_IMAGE)
pixels = img.load()

rows, cols = img.size

print(rows, cols)
randomValues = []
for x in range(rows):
    for y in range(cols):
        randomValues.append([random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)])

print(len(randomValues))
def AND(randomValues,pixels):
    for x in range(rows):
        for y in range(cols):
            pixelr,pixelg,pixelb = pixels[x,y]
            randomr,randomg,randomb = randomValues[(x+1)*(y*1)]
            pixels[x,y] = pixelr & randomr,pixelg & randomr, pixelb & randomb

    img.save(AND_IMAGE)
    print("NOW DONE WITH AND")

def OR(randomValues,pixels):
    for x in range(rows):
        for y in range(cols):
            pixelr,pixelg,pixelb = pixels[x,y]
            randomr,randomg,randomb = randomValues[(x+1)*(y*1)]
            pixels[x,y] = pixelr | randomr,pixelg | randomr, pixelb | randomb
    print("NOW DONE WITH OR")
    img.save(OR_IMAGE)

def XOR(randomValues,pixels):
    for x in range(rows):
        for y in range(cols):
            pixelr,pixelg,pixelb = pixels[x,y]
            randomr,randomg,randomb = randomValues[(x+1)*(y*1)]
            pixels[x,y] = pixelr ^ randomr,pixelg ^ randomr, pixelb ^ randomb
    print("NOW DONE WITH XR")
    img.save(XOR_IMAGE)

AND(randomValues,pixels)
img = Image.open(INPUT_IMAGE)
pixels = img.load()
OR(randomValues,pixels)
img = Image.open(INPUT_IMAGE)
pixels = img.load()
XOR(randomValues,pixels)



