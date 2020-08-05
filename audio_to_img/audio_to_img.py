import wave
from PIL import Image
import math
def main():
    name = input("Name: ")
    w = wave.open(f"{name}.wav", "rb")
    binary_data = w.readframes(w.getnframes())
    w.close()

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
    img = Image.new('RGB', (size, size), "black")
    pixels = img.load()
    pixelNum = 0
    for x in range(size):
        for y in range(size):
            pixels[x,y] = (rgbVals[pixelNum][0], rgbVals[pixelNum][1], rgbVals[pixelNum][2])
            pixelNum += 1
    img.save(f"./{name}.png")

main()
