
from detect import run

run(weights="models/yolov5s_best.pt", source="http://10.0.0.1:4747/video", conf_thres=0.2)
run(weights="models/yolov5s_best.pt", source="http://192.168.100.19:4747/video", conf_thres=0.2)
