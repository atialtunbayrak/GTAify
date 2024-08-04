import json
import random

def loadPalleteList(paletteSize):

    if paletteSize in ["1","2","3","4"]:
        converted = {'1':'100','2':'200','3':'500','4':'1000'}[paletteSize]
        # print(f"{'/'.join(__file__.split('/')[:-1] )}/ColorPalettes/{str(paletteSize)}.json")
        with open(f"{'/'.join(__file__.split('/')[:-1] )}/ColorPalettes/{ converted }.json", 'r') as file:
            return json.load(file)
        
    else:
        raise ValueError("Invalid pallete randomness, must be \ndefault = \"1\"")

def chooseRandomPalette(paletteSize="200") -> list:
    palletesList = loadPalleteList(paletteSize)
    pallete =  random.choice(palletesList)

    finalchoice = []

    #for conversion from hex to rgb
    for hexcolor in pallete:
        finalchoice.append( list(int(hexcolor.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
    print(f"Used color palette: {finalchoice}")
    return finalchoice


if __name__ == "__main__":
    print(chooseRandomPalette())