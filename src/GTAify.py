import argparse
from palettes import chooseRandomPalette
from imageTools import GTAifyImage, loadImage, saveImage
import re
import json
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="GTAify an image")
    parser.add_argument("image", help="The path to the image to process, Accepts most common types")
    parser.add_argument("output", help="The path to save the processed image")
    parser.add_argument("-q", "--quality", type=int, default=50, help="Adjusts the accuracy of colors in the image. Setting it higher than 50 gets performance intensive. Default:50.")
    parser.add_argument("-r", "--palette_randomness", choices=["1","2","3","4"],  help="The randomness of chosen palette colors. 4 is most random and 1 is the most common/classic palettes", default="1")
    parser.add_argument("-p", "--palette", help="The color palette to use ont he image, is a list of rgb values. if used, -r is ignored. Ex: [[125,257,273],[265,378,111]]")
    args = parser.parse_args()

    palette = []
    if args.palette:
        if any([not i in "1234567890[] ," for i in args.palette]):

            raise("Invalid palette format, must be a list of rgb values. Ex: [[125,257,273],[265,378,111]]")

        else:
            #parse the pallete string
            print("in else")
            palette= json.loads(args.palette)
            print(palette)

    else:
        palette = chooseRandomPalette(args.palette_randomness)
    
    img = loadImage(args.image)
    processedImage = GTAifyImage(img, palette, Quality=args.quality)
    saveImage(processedImage, args.output)
        
if __name__ == "__main__":
    main()