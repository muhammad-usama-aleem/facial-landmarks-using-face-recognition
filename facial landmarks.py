import os
import numpy as np
import cv2
import face_recognition as fg



os.chdir("C:/Users/abdul/OneDrive/Pictures/New folder")
img = cv2.imread("test.jpg")
location = fg.face_locations(img)
landmark = fg.face_landmarks(img, location)


print(landmark)

test = []
for a in landmark[0]:
    test.append(landmark[0][a])

final = []
for a in range(0, 17):
    final.append(test[0][a])

for b in range(1, 3):
    for a in range(0, 5):
        final.append(test[b][a])

for a in range(0, 4):
    final.append(test[3][a])

for a in range(0, 5):
    final.append(test[4][a])

for b in range(5, 7):
    for a in range(0, 6):
        final.append(test[b][a])

for b in range(7, 9):
    for a in range(0, 12):
        final.append(test[b][a])

length = len(final)
print(final)
for l in range(0, length):
    cv2.circle(img, final[l], 3, (255, 255, 255), 2)

cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
