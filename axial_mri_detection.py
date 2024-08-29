# --------------- Axial MRI Detection -------------------
import numpy as np
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import pandas as pd
import cv2

model = YOLO(r'D:\Pycharm\Computer Vision Project\axial MRI\axial MRI.pt')
class_list = {0: 'negative', 1: 'positive'}

st.title('Axial MRI Detection🧠')
file_uploader = st.file_uploader('Upload The Image', type=['jpg', 'png'])
if file_uploader:
    image = Image.open(file_uploader)
    image = np.array(image)
    prediction = model.predict(image)[0].boxes.data
    final_pred = pd.DataFrame(prediction).astype(float)
    for index, row in final_pred.iterrows():
        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
        cls = class_list[int(row[5])]
        confidence = row[4]


        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 165), 1)
        cv2.rectangle(image, (x1, y1 - 18), (x1 + 40, y1), (0, 255, 165), -1)

        cv2.putText(image, f'{cls}', (x1, y1 - 10), cv2.FONT_ITALIC, 0.3, (0, 0, 0), 1)
        cv2.putText(image, f'{round(confidence, 2)}%', (x1, y1), cv2.FONT_ITALIC, 0.3, (0, 0, 0), 1)

    st.image(image, caption='Processed Image', use_column_width=True)
