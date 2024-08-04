import cv2 
import numpy as np

#color_pallette=[[53,249,242],[250,116,44],[170, 255, 0],[252,97,211],[255,208,11],[28,26,40]] #neon_color_pallette
# color_pallette = [[ 34, 9, 44],[ 135, 35, 65],[ 190, 49, 68],[ 240, 89, 65],[ 53, 47, 68],[ 92, 84, 112],[ 185, 180, 199],[ 250, 240, 230]] #red punk color pallette
#color_pallette =[[172,231,240],[131,232,167],[172,232,51],[222,255,28],[55,217,102]]#Boardwalk, l.#green blue
#color_pallette = [[154, 3, 30],[95, 15, 64],[251, 139, 36],[251, 139, 36],[227, 100, 20],[154, 3, 30]]#orangeish

def loadImage(imagePath):
    i= cv2.imread(imagePath)

    # print(i)
    return i 

def saveImage(imageObject, savePath):
    cv2.imwrite(savePath, imageObject)

def GTAifyImage(inputImageObject, color_pallette, Quality=10):

    # color palette post processing, RGB to BGR conversion for cv2
    color_pallette = [ i[::-1] for i in color_pallette]
    reshapedImage =inputImageObject.reshape((-1,3))
    reshapedImage = np.float32(reshapedImage)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    colorAmount = len(color_pallette)
    _ ,label,center=cv2.kmeans(reshapedImage,colorAmount,None,criteria,Quality,cv2.KMEANS_RANDOM_CENTERS)#30 attempts

    labeldict={}
    for i in label:
        if i[0] in labeldict:
            labeldict[i[0]]+=1
        else:
            labeldict[i[0]]=1

    labeldict=sorted(labeldict.items(), key=lambda x: x[1], reverse=True)
    #print(labeldict)


    temp_color_pallette= color_pallette.copy()
    color_pallette=[]
    for i in labeldict:
        # print(i)
        color_pallette.append(temp_color_pallette[::-1][i[0]])

    center = temp_color_pallette

    center = np.uint8(center)
    
    return  center[label.flatten()].reshape((inputImageObject.shape))


if __name__ == "__main__":
    #tests
    a = loadImage("../tests/inputs/lena.png")
    # print(a)
    b = GTAifyImage(a, [[ 34, 9, 44],[ 135, 35, 65],[ 190, 49, 68],[ 240, 89, 65],[ 53, 47, 68],[ 92, 84, 112],[ 185, 180, 199],[ 250, 240, 230]], Quality=20 )
    
    # print(b)
    saveImage(b, "../tests/outputs/lena.png")