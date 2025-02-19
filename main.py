import cv2
import time
import winsound
from sympy.physics.units import frequency
from ultralytics import YOLO
import numpy as np
import cv2
import pyautogui

# 加载训练好的模型
model = YOLO("") #best.pt file path

# 初始化摄像头
cap = cv2.VideoCapture(0)

last_A_time = 0  # 记录 A 动作出现的时间
A_detected = False  # A 是否发生

A_to_B_timeout = 3  # 设定 A 发生后最多 3 秒内要发生 B，否则重置

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)  # 目标检测
    current_time = time.time()

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()  # 目标框
        labels = result.boxes.cls.cpu().numpy()  # 目标类别

        for box, label in zip(boxes, labels):
            x1, y1, x2, y2 = map(int, box)
            class_name = model.names[int(label)]

            # 识别 A 动作
            if class_name == "A":
                A_detected = True
                last_A_time = current_time  # 记录 A 发生时间
                print("A 动作识别成功！")

            # 识别 B 动作（必须 A 先发生）
            if class_name == "B" and A_detected:
                if current_time - last_A_time <= A_to_B_timeout:  # B 在 A 之后发生
                    print("B 动作识别成功！触发操作！")
                    frequency=2500
                    duration=1000
                    winsound.Beep(frequency, duration)
                    image = pyautogui.screenshot("image1.png")
                    A_detected = False  # 重置状态
                else:
                    print("B 发生太迟，忽略！")

    cv2.imshow("Action Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
