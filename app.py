import streamlit as st
import numpy as np
import time
import cv2 # pip install opencv-python-headless

from detect import run

camera = cv2.VideoCapture("http://10.0.0.1:4747/video") # on a mac you can use either your mac webcam or an iphone camera using continuity camera! for me, my iphone was (1) and my mac webcam was (0)
# Limit the size and FPS to increase speed
camera.set(cv2.CAP_PROP_FPS, 24) # FPS
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # compression method

FPS = 10

@st.cache_data(max_entries=5, ttl=10)
def get_frame(time): # we pass in time to make sure the cache is updated every call
    global camera
    try: 
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)  # this line flips the image
        cv2.imwrite("frame.jpg", frame)
        run(weights="models/yolov5s_best.pt", source="http://10.0.0.1:4747/video", conf_thres=0.2)
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



# def main():
#     st.set_page_config(layout="wide")
#     st.title("Live Camera Feed")
#     col1, col2, col3 = st.columns([1,8,1])
#     with col2: image_spot = st.image([])
    
#     frames = []
#     while True:
#         if len(frames) == FPS:
#             height, width = frames[0].shape[:2]
#             fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#             out = cv2.VideoWriter('out.mp4', fourcc, FPS, (width, height))

#             for f in frames:
#                 # تبدیل به uint8 اگر لازم باشه
#                 if f.dtype != np.uint8:
#                     f = (f * 255).clip(0, 255).astype(np.uint8)
                
#                 # اگر تک‌کاناله است، به RGB تبدیلش کن
#                 if len(f.shape) == 2:
#                     f = cv2.cvtColor(f, cv2.COLOR_GRAY2RGB)

#                 bgr = cv2.cvtColor(f, cv2.COLOR_RGB2BGR)
#                 out.write(bgr)

#             out.release()
#             st.success("Saved 10-frame video as out.mp4")
#             frames.clear()

#         # data = get_frame(time.time())
#         # frames.append(data)
#         # image_spot.image(data)
#             with open("out.mp4", "rb") as file:
#                 video_bytes = file.read()
#                 st.video(video_bytes)