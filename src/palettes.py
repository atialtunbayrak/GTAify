import json
import random

def loadPalleteList(paletteSize):

    if paletteSize in ["100","200","500","1000"]:
        # print(f"{'/'.join(__file__.split('/')[:-1] )}/ColorPalettes/{str(paletteSize)}.json")
        with open(f"{'/'.join(__file__.split('/')[:-1] )}/ColorPalettes/{str(paletteSize)}.json", 'r') as file:
            return json.load(file)
        
    else:
        raise ValueError("Invalid pallete size, must be 100,200,500 or 1000\ndefault = 200")

def chooseRandomPalette(paletteSize="200") -> list:
    palletesList = loadPalleteList(paletteSize)
    pallete =  random.choice(palletesList)

    finalchoice = []

    #for conversion from hex to rgb
    for hexcolor in pallete:
        finalchoice.append( list(int(hexcolor.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
    return finalchoice


if __name__ == "__main__":
    print(chooseRandomPalette())