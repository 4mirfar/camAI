import cv2


def vid_mkr(frames):
# Assume `frames` is a list or array of 10 RGB frames (shape: HxWx3, dtype=uint8)
    height, width, _ = frames[0].shape
    out = cv2.VideoWriter("saves/output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 24, (width, height))

    for frame in frames:
        # Convert RGB to BGR if needed
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    out.release()
