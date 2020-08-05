import wave
from PIL import Image
from textwrap import wrap
import math
def main():
    name = input("Name: ")
    w = wave.open(f"{name}.wav", "rb")
    binary_data = w.readframes(w.getnframes())
    w.close()
    #
    # g = wrap(str(bin(int(binary_data.hex(), base=16)).lstrip('0b')), 8).remove('0')
    rgbVals = []
    tempA = []
    t = 0
    for i in binary_data:
        if t == 3:
            rgbVals.append(tempA)
            tempA = []
            t = 0

        tempA.append(i)
        t+=1
    size = int(math.sqrt(len(rgbVals)))
    img = Image.new('RGB', (size, size), "black")  # create a new black image
    pixels = img.load()  # create the pixel map
    pixelNum = 0
    print(size)
    print(len(rgbVals))
    for x in range(size):
        for y in range(size):
            pixels[x,y] = (rgbVals[pixelNum][0], rgbVals[pixelNum][1], rgbVals[pixelNum][2])
            pixelNum += 1
    img.save(f"./{name}.png")

main()
