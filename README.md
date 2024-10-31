# GTAify
 A command line util for converting images into stylistic menu-like photographs by using k-means clustering and color appriximation algorithms.

The predefined color palettes are thanks to [this github page](https://github.com/Experience-Monks/nice-color-palettes/tree/master), the color palettes used are redefinable in the json files.

# Examples
<img width="600" alt="image" src="https://github.com/user-attachments/assets/04fc024a-b410-401a-b320-31242f3ca1f6">
<img width="400" alt="image" src="https://github.com/user-attachments/assets/9227dc0b-d38a-4b3f-b997-4ad468e60424">
<img width="400" alt="image" src="https://github.com/user-attachments/assets/8949d7a4-2a9c-4f20-bbf6-a332b3726fcc">



## Installation
Download the repository and run the following command in the root directory:
```bash
pip install -r requirements.txt
```
After that, you are ready to go!

## Usage 

```bash
python gtaify.py <input_image> <output_image> -q <quality> -r <palette randomness> -p "<custom palette>"
```

### Arguments
- `input_image` - The path to the image you want to convert.
- `output_image` - The path to the output image.
- `-r` - The randomness of the color palette which ranges from intigers 1 to 4. Default is 1.
- `-q` - The quality of the output image. The higher the quality, the more time it takes to process. Default is 50. Going above 100 often increases wait times substantialy. 
- `-p` - A custom palette that you can provide in the form of a list of RGB lists. For example: `[[255, 255, 255], [0, 0, 0]]`. Cannot be used with the randomness argument since a plette is specified.

## Lisance 
This project is lisanced under MIT and can be used via any reason given credit is acreddited.

