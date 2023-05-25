import cv2
import numpy as np
import os

# load cascade classifier
face_cascade = cv2.CascadeClassifier(os.path.join(
    os.path.dirname(__file__), 'haarcascade_frontalface_alt.xml'))

# load source video
video_source = cv2.VideoCapture(os.path.join(
    os.path.dirname(__file__), 'sleepy.mp4'))

# Set the upper bound and lower bound of face in HSV
skin_upper_bound = np.array([0, 50, 50], dtype=np.uint8)
skin_lower_bound = np.array([80, 180, 220], dtype=np.uint8)

# set font
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2

# read parameter about the video
v_h = video_source.get(cv2.CAP_PROP_FRAME_HEIGHT)
v_w = video_source.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = video_source.get(cv2.CAP_PROP_FPS)
frame_cnt = video_source.get(cv2.CAP_PROP_FRAME_COUNT)

# frame count & effect info
frame_cnt = 0
effect_index = 0
effect_name = ["Default", "Grayscale", "Bilevel",
               "Mosaic", "Negative", "Edge", "Mask"]
effect_border = 5

while True:
    ret, frame = video_source.read()
    if ret:
        frame_cnt += 1

        roi = frame[int(v_h * 0.25):int(v_h * 0.75),
                    int(v_h * 0.25):int(v_h * 0.75)]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, skin_upper_bound, skin_lower_bound)
        skin_area_ratio = np.count_nonzero(
            mask) / (mask.shape[0] * mask.shape[1])
        skin_mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        cv2.putText(skin_mask_colored, f"area= {skin_area_ratio:.2f}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), font_thickness)

        bg = np.ones_like(frame) * 128
        dx = (bg.shape[1] - skin_mask_colored.shape[1]) // 2
        dy = (bg.shape[0] - skin_mask_colored.shape[0]) // 2
        bg[dy:dy + skin_mask_colored.shape[0],
           dx:dx + skin_mask_colored.shape[1]] = skin_mask_colored

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, 1.2, 7)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                roi = frame[y-effect_border:y+h+effect_border,
                            x-effect_border:x+w+effect_border]
                if effect_index == 0:
                    pass

                elif effect_index == 1:
                    # Gray scale
                    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                    frame[y-effect_border:y+h+effect_border, x-effect_border:x+w +
                          effect_border] = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

                elif effect_index == 2:
                    # Bilevel
                    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                    _, binary_roi = cv2.threshold(
                        gray, 127, 255, cv2.THRESH_BINARY)
                    frame[y-effect_border:y+h+effect_border, x-effect_border:x+w +
                          effect_border] = cv2.cvtColor(binary_roi, cv2.COLOR_GRAY2BGR)

                elif effect_index == 3:
                    # Mosaic
                    mosaic_level = 15
                    mosaic = cv2.resize(
                        roi, ((w+2*effect_border)//mosaic_level, (h+2*effect_border)//mosaic_level), interpolation=cv2.INTER_LINEAR)
                    resized_mosaic = cv2.resize(
                        mosaic, ((w+2*effect_border), (h+2*effect_border)), interpolation=cv2.INTER_NEAREST)
                    frame[y-effect_border:y+h+effect_border, x -
                          effect_border:x+w+effect_border] = resized_mosaic

                elif effect_index == 4:
                    # Negative
                    negative = -roi
                    frame[y-effect_border:y+h+effect_border, x -
                          effect_border:x+w+effect_border] = negative

                elif effect_index == 5:
                    # Edge
                    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray, 40, 100)
                    frame[y-effect_border:y+h+effect_border, x-effect_border:x + w +
                          effect_border][edges != 0] = (255, 255, 255)
                    frame[y-effect_border:y+h+effect_border, x -
                          effect_border:x+w+effect_border][edges == 0] = (0, 0, 0)

                elif effect_index == 6:
                    # Mask
                    mask_img = cv2.imread(os.path.join(os.path.dirname(
                        __file__), "mask.jpg"), cv2.IMREAD_UNCHANGED)
                    mask_filter = cv2.resize(
                        mask_img, (w+2*effect_border, h+2*effect_border))
                    b, g, r = cv2.split(mask_filter)
                    mask_px = (b > 5) & (g > 5) & (r > 5)
                    frame[y-effect_border:y+h+effect_border, x-effect_border:x+w +
                          effect_border][mask_px] = mask_filter[mask_px]
                cv2.rectangle(frame, (x-effect_border, y -
                              effect_border), (x+w+effect_border, y+h+effect_border), (255, 0, 0), 2)
                center = (x-effect_border + (w+effect_border) //
                          2, (y-effect_border) + (h+effect_border)//2)
                axes_length = ((w+2*effect_border)//2, (h+2*effect_border)//2)
                # display frame & Text
                cv2.ellipse(frame, center, axes_length,
                            0, 0, 360, (0, 255, 255), 2)
                cv2.putText(frame, "B11705009", (x, y-3*effect_border), font,
                            font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)
                cv2.putText(frame, f"Effect {effect_index+1}:{effect_name[effect_index]}", (x, y+h+6*effect_border), font,
                            font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

        if skin_area_ratio > 0.05 and len(faces) == 0:
            if frame_cnt % 10 < 5:
                # Flash text
                cv2.putText(frame, "Wake Up!", (50, 50), font, font_scale,
                            (0, 255, 255), font_thickness, cv2.LINE_AA)
        elif skin_area_ratio <= 0.07 and len(faces) == 0:
            cv2.putText(frame, "Nobody", (50, 50), font, font_scale,
                        (0, 0, 255), font_thickness, cv2.LINE_AA)

        output = np.hstack((bg, frame))
        cv2.imshow('Detect Sleepiness', output)
        # wait for 10 ms
        key = cv2.waitKey(10) & 0xFF
        if key == 27:
            break
        # check input
        for i in range(1, 8):
            if key == ord(str(i)):
                effect_index = i-1
                break

    else:
        break

# close windows
video_source.release()
cv2.destroyAllWindows()
