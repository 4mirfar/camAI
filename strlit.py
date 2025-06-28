import streamlit as st
import numpy as np

from detect import run

from vid_maker import vid_mkr

st.set_page_config(
    page_title="Live CCTV Feed",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# video_file = open('myvideo.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)
THRESHOLD = 10
frames = []
with col1:
   # cam1 = st.text_input('cam #1', 'http://192.168.100.11:4747/video',key="cam1",label_visibility="collapsed",placeholder="cam #1 url")
   cam1 = st.text_input('cam #1', 'http://192.168.100.16:4747/video',key="cam1",label_visibility="collapsed",placeholder="cam #1 url")
   # try:
   frame = st.image(cam1)
   frames.append(frame)
   fire_det = None
   if len(frames) == THRESHOLD:
      vid_mkr(frames=frames)
      fire_det = run(weights="model/yolov5s_best.pt", source="saves/output.mp4", data="fire.yaml", conf_thres=0.2)
      frames = []
   
   loaded_frames = st.image(fire_det)
   

   cam1_feed = loaded_frames
      # cam1_feed = st.image(cam1,use_column_width =True)
   # except:
      # st.image("Original-colour-bar.png")
# with col2:
#    cam2 = st.text_input('cam #2', 'http://192.168.1.101:81/stream',key="cam2",label_visibility="collapsed",placeholder="cam #2 url")
#    try:
#       st.image(cam2,use_column_width =True)
#    except:
#       st.image("Original-colour-bar.png")

# with col3:
#    cam3 = st.text_input('cam #3', 'http://192.168.1.101:81/stream',key="cam3",label_visibility="collapsed",placeholder="cam #3 url")
#    try:
#       st.image(cam3,use_column_width =True)
#    except:
#       st.image("Original-colour-bar.png")
# with col4:
#    cam4 = st.text_input('cam #4', 'http://192.168.1.101:81/stream',key="cam4",label_visibility="collapsed",placeholder="cam #4 url")
#    try:
#       st.image(cam4,use_column_width =True)
#    except:
#       st.image("Original-colour-bar.png")



# https://github.com/athulaugustine/Live-cctv-feed-using-Streamlit