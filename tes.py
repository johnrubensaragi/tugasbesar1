import cv2
import time
img = cv2.imread(".\\simbol\\50000.png", cv2.IMREAD_ANYCOLOR)
 
N = 25
for i in range(N):
    cv2.imshow(f"Duit {i+1}", img)
cv2.waitKey(0)
