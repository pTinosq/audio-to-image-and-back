import wave
from PIL import Image
from textwrap import wrap
import math
import struct

def main():
    name = input("Name: ")
    image = Image.open(f"./{name}")
    rgb_image = image.convert('RGB')
    width, height = image.size
    pixels = image.load()  # create the pixel map
    rgbVals = []
    print("Developing RGB data...")
    for x in range(width):
        for y in range(height):
            avgCol = (rgb_image.getpixel((x,y))[0] + rgb_image.getpixel((x,y))[1] + rgb_image.getpixel((x,y))[2])/3
            rgbVals.append(int(avgCol))



    sampleRate = 44400.0 # hertz
    duration = len(rgbVals)      # seconds
    frequency = 1040.0    # hertz

    wavef = wave.open(f'{name.replace(".","_")}.wav','w')
    wavef.setnchannels(1) # mono
    wavef.setsampwidth(2)
    wavef.setframerate(sampleRate)
    print("Developing waveforms")
    for i in range(int(duration)):
        value = rgbVals[i]*100
        data = struct.pack('<h', value)
        wavef.writeframesraw( data )

    # wavef.writeframes('')
    wavef.close()


main()
