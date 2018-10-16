
# https://gist.github.com/iandanforth/0ed987bfddf8205b8a23

# websocketd --port=8080 python imagemaker.py

from PIL import Image
import numpy as np
import sys


imgMat = np.load(sys.argv[1])
#imgMat1 = np.load(sys.argv[1])
#imgMat2 = np.load(sys.argv[2])

#imgMat = imgMat2
"""
for i in range(810 * 810 - 1):
    #for j in range(810):
    count = i + 1
    
    i1 = i/810
    i2 = count/810
    
    j1 = i % 810
    j2 = count % 810
     
    if(imgMat1[i1,j1] != 0 and imgMat2[i2,j2] != 0):
        if(imgMat1[i1,j1] != imgMat2[i2,j2]):
            
                print i1
                print j1
                print imgMat1[i1,j1-5:j1+5]
                print imgMat2[i2,j2-5:j2+5]
                die = 1/0 # mismatch in matrix
        else:
                imgMat[i,j] = imgMat1[i1,j1]
               
    elif(imgMat1[i1,j1] != 0):
            imgMat[i1,j1] = imgMat1[i1,j1]
            
    elif(imgMat2[i1,j1] != 0):
            imgMat[i1,j1] = imgMat2[i2,j2]
   """ 

    
    
    
max = 0
min = 9999999

for i in range(810):
    for j in range(810):
        
        if(imgMat[i,j] > max):
            max = imgMat[i,j]
            
imgMat2 = np.divide(imgMat, max)

imgMat2 = np.multiply(imgMat2, 255)

img = Image.fromarray(np.uint8(imgMat2))

img.save('%s.png' % sys.argv[1])