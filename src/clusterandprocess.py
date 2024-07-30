
#try all you want, looks bad 
import cv2 
import numpy as np
import cv2 as cv
import os



img = cv2.imread("/Users/atillaaltunbayrak/Desktop/Code/Python/GTAify/tests/inputs/lena.jpeg")

#color_pallette=[[53,249,242],[250,116,44],[170, 255, 0],[252,97,211],[255,208,11],[28,26,40]] #neon_color_pallette

color_pallette = [[ 34, 9, 44],[ 135, 35, 65],[ 190, 49, 68],[ 240, 89, 65],[ 53, 47, 68],[ 92, 84, 112],[ 185, 180, 199],[ 250, 240, 230]] #red punk color pallette

#color_pallette =[[172,231,240],[131,232,167],[172,232,51],[222,255,28],[55,217,102]]#Boardwalk, l. green blue

color_pallette = [ i[::-1] for i in color_pallette]
#orangeish
#color_pallette = [[154, 3, 30],[95, 15, 64],[251, 139, 36],[251, 139, 36],[227, 100, 20],[154, 3, 30]]

def centertoclosestcolor(center):
    #this function will take a label and return the closest color from the color pallette
    
    retcenter=[]
    color_pallette_=color_pallette.copy()
    print(color_pallette_[::-1])
    for pallettecolor in center[::-1]:
        
        #mincolor = min(color_pallette_, key=lambda i:abs(pallettecolor[0]-i[0])+abs(pallettecolor[1]-i[1])+abs(pallettecolor[2]-i[2]) )
        mincolor = min(color_pallette_, key=lambda i:abs(sum(pallettecolor)-sum(i)))
        retcenter.append(mincolor)
        color_pallette_.remove(mincolor)
    print(retcenter)
    return retcenter


#Z = edgedetectedwithcolor.reshape((-1,3))
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = len(color_pallette)
ret,label,center=cv.kmeans(Z,K,None,criteria,50,cv.KMEANS_RANDOM_CENTERS)#30 attempts

print(center)
#center= centertoclosestcolor(center)

#turn label into a dictionary containing how many times each label appears
labeldict={}
for i in label:
    if i[0] in labeldict:
        labeldict[i[0]]+=1
    else:
        labeldict[i[0]]=1

#sort the dictionary by value
labeldict=sorted(labeldict.items(), key=lambda x: x[1], reverse=True)
print(labeldict)

#sort the color pallette using the dict 
color_pallette_=color_pallette.copy()
color_pallette=[]
print(color_pallette, color_pallette_)
for i in labeldict:
    print(i)
    color_pallette.append(color_pallette_[::-1][i[0]])

center = color_pallette_

center = np.uint8(center)
res = center[label.flatten()]
cv.imshow('res1',res)
res2 = res.reshape((img.shape))


cv.imshow('res2',res2)
cv.waitKey(0)
cv.destroyAllWindows()

print(color_pallette, color_pallette_)


try:
    cv2.imwrite("processed/" + Path.split('/')[-1], res2)
    print("saved")
except:

    cv2.imwrite(res2,"processed/"+Path.split['/'][-1])


            
"""# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (1,1), 0) 
edgedetected=cv2.Canny(image=img_blur, threshold1=50, threshold2=50) # Canny Edge Detection

#for every  pixel on the image, spread more pixels to adjacent pixels
canvas=np.zeros((edgedetected.shape[0],edgedetected.shape[1]), np.uint8)
for i in range(edgedetected.shape[0]):
    for j in range(edgedetected.shape[1]):
        if edgedetected[i,j]==255:
            canvas[i,j]=255
            if i-1>=0:
                canvas[i-1,j]=255
            if i+1<edgedetected.shape[0]:
                canvas[i+1,j]=255
            if j-1>=0:
                canvas[i,j-1]=255
            if j+1<edgedetected.shape[1]:
                canvas[i,j+1]=255
            if i-1>=0 and j-1>=0:
                canvas[i-1,j-1]=255
            if i+1<edgedetected.shape[0] and j+1<edgedetected.shape[1]:
                canvas[i+1,j+1]=255
            if i+1<edgedetected.shape[0] and j-1>=0:
                canvas[i+1,j-1]=255
            if i-1>=0 and j+1<edgedetected.shape[1]:
                canvas[i-1,j+1]=255

edgedetected=canvas

edgedetectedwithcolor=np.zeros((edgedetected.shape[0],edgedetected.shape[1],3), np.uint8)
#looks at the edgedetected result and gets the color of that pixel from the original image
print(edgedetected.shape, img.shape)
for i in range(edgedetected.shape[0]):
    for j in range(edgedetected.shape[1]):
        if edgedetected[i,j]==255:
            #print(img[i,j])
            edgedetectedwithcolor[i,j]=img[i,j]

cv.imshow('withedge',edgedetectedwithcolor)""" #Edge detected with color