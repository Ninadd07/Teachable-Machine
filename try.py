import streamlit as st
import cv2
import shutil
import os


class1 = st.text_input(label= "Input class 1 : ")
run = st.checkbox(label = "Run", key = "cb")
img_inp_c1 = st.button("Click Image")
frame_window = st.image([])

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

img_counter1 = 0

while run :
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_window.image(frame)
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)


    while img_inp_c1 :
        img_name = "opencv_frame_{}.png".format(img_counter1)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        path1 = r"C:\Users\harshad\Desktop\Python\ntuproject\{0}".format(img_name)
        path2 = r"C:\Users\harshad\Desktop\Python\ntuproject\data\class1"
        shutil.move(path1, path2)
        img_counter1 += 1

cam.release()

cv2.destroyAllWindows()


try :
    initial = r"C:/Users/harshad/Desktop/Python/ntuproject/data/class1"
    final = r"C:/Users/harshad/Desktop/Python/ntuproject/data/{0}".format(class1)
    os.rename(initial, final)
except :
    pass