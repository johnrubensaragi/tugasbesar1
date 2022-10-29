import cv2
img = cv2.imread(".\\simbol\\50000.png", cv2.IMREAD_ANYCOLOR)
 
for i in range(5):
    cv2.imshow(f"Duit {i+1}", img)
cv2.waitKey(0)
