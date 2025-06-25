import streamlit as st

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

with col1:
   cam1 = st.text_input('cam #1', 'http://10.0.0.6::81/stream',key="cam1",label_visibility="collapsed",placeholder="cam #1 url")
   try:
      cam1_feed = st.image(cam1,use_column_width =True)
   except:
      st.image("Original-colour-bar.png")
with col2:
   cam2 = st.text_input('cam #2', 'http://192.168.1.101:81/stream',key="cam2",label_visibility="collapsed",placeholder="cam #2 url")
   try:
      st.image(cam2,use_column_width =True)
   except:
      st.image("Original-colour-bar.png")

with col3:
   cam3 = st.text_input('cam #3', 'http://192.168.1.101:81/stream',key="cam3",label_visibility="collapsed",placeholder="cam #3 url")
   try:
      st.image(cam3,use_column_width =True)
   except:
      st.image("Original-colour-bar.png")
with col4:
   cam4 = st.text_input('cam #4', 'http://192.168.1.101:81/stream',key="cam4",label_visibility="collapsed",placeholder="cam #4 url")
   try:
      st.image(cam4,use_column_width =True)
   except:
      st.image("Original-colour-bar.png")



https://github.com/athulaugustine/Live-cctv-feed-using-Streamlit