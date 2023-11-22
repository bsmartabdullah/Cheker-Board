#CHECKER BOARD
import numpy as np
import cv2
bkg = np.zeros((400,400,3))
bkg[0:100,0:100] = 255,255,255
bkg[100:200,100:200] =255,255,255
bkg[200:300,200:300] =255,255,255
bkg[300:400,300:400] =255,255,255
bkg[0:100,200:300] =255,255,255
bkg[100:200,300:400] =255,255,255
bkg[200:300,0:100] = 255,255,255
bkg[300:400,100:200] =255,255,255
cv2.imshow('CHESS BOARD',bkg)
cv2.waitKey(0)
cv2.destroyAllWindows()
           
