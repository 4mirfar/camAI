# Brian Joseph Lesko        2/1/24      Robotics Automation Engineer III
# Create a LAN server that hosts a live data feed generated from the host machine 
# Run the app with streamlit run app.py --server.address 0.0.0.0 --server.port 8501
# access the app from another device through the host machine's IP address and the port 8501 ip:port

import streamlit as st
import numpy as np
import time
import cv2 # pip install opencv-python-headless

camera = cv2.VideoCapture("http://10.0.0.1:4747/video") # on a mac you can use either your mac webcam or an iphone camera using continuity camera! for me, my iphone was (1) and my mac webcam was (0)
# Limit the size and FPS to increase speed
camera.set(cv2.CAP_PROP_FPS, 24) # FPS
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # compression method

@st.cache_data(max_entries=5, ttl=10)
def get_frame(time): # we pass in time to make sure the cache is updated every call
    global camera
    try: 
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)  # this line flips the image
        return frame
    except:
        return np.zeros((300, 300, 3))

def main():
    st.set_page_config(layout="wide")
    st.title("Live Camera Feed")
    col1, col2, col3 = st.columns([1,8,1])
    with col2: image_spot = st.image([])
    
    while True:
        data = get_frame(time.time())
        image_spot.image(data)
        
main() 