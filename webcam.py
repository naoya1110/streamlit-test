import cv2
import streamlit as st
import time
from PIL import Image

st.markdown("# Webcam App")

device = user_input = st.text_input("input your video/camera device", "0")

if device.isnumeric():
    device = int(device)
    
cap = cv2.VideoCapture(device)

image_loc = st.empty()
fps_loc = st.empty()
stop_button = st.button("Stop Webcam")

t_old = time.time()
while cap.isOpened:
    ret, img = cap.read()
    time.sleep(0.01)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image_loc.image(img)
    
    t_new = time.time()
    dt = t_new - t_old
    t_old = t_new
    fps = 1/dt
    fps_loc.text(f"{fps:.1f}")
    
    
    if stop_button:
        break
    
cap.release()