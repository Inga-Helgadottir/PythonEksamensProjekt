import cv2
import matplotlib.pyplot as plt


color = (255, 255, 255)
myThickness = 5
imageCircle = cv2.imread("images/start.jpg", 1)

step1 = cv2.circle(imageCircle, (100, 290), 100, color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step1.jpg", step1)

step2 = cv2.line(step1, (100, 190), (100, 30), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step2.jpg", step2)

step3 = cv2.line(step2, (250, 30), (100, 30), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step3.jpg", step3)

step4 = cv2.line(step3, (250, 60), (250, 30), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step4.jpg", step4)

step5 = cv2.circle(step4, (250, 90), 30, color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step5.jpg", step5)

step6 = cv2.line(step5, (250, 120), (250, 180), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step6.jpg", step6)

step7 = cv2.line(step6, (250, 150), (280, 150), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step7.jpg", step7)

step8 = cv2.line(step7, (250, 150), (220, 150), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step8.jpg", step8)

step9 = cv2.line(step8, (270, 230), (250, 180), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step9.jpg", step9)

step10 = cv2.line(step9, (230, 230), (250, 180), color, thickness=myThickness, lineType=cv2.LINE_AA)
cv2.imwrite("images/step10.jpg", step10)
