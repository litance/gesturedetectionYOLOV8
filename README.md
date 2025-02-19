# gesturedetectionYOLOV8
Gesture detection and event generation based on YOLOV8 基于YOLOV8的手势检测及事件发生

### 所需要第三方库 Third-party libraries needed to run this program
- ultralytics
- opencv-python
- numpy
- pyautogui
- sympy
- Pytorch

## 1.首先, 安装第三方库 Install Third-party libraries
```
pip install ultralytics opencv-python numpy pyautogui sympy
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 2.下载模型 Download model
```
git clone https://github.com/litance/gesturedetectionYOLOV8.git
```

## 2.配置好代码 Configure the code

https://app.roboflow.com/try-jtjar
在这个网站，你可以制作你自己的dataset.
> Here you can create your own dataset.

当然，你也可以下载外部的dataset，只需要把文件格式放置成这样.
> Of course, you can also download external datasets, just put the file format like this.

```
dataset/ 
│── images/
│   ├── train/  # 训练集
│   ├── val/    # 验证集
│── labels/
│   ├── train/  # 训练标签（每张图片一个.txt文件）
│   ├── val/    
└── dataset.yaml  # 数据集配置文件

```

### train.py
model(line:3)
```
model = YOLO("yolov8n.pt")
```

Epoch, batch, workers, device(line;5-8)
```
epochs=50,
batch=32,
workers=0,
device="cuda")
```

### main.py
Time after A detected to B(line:19)
```
A_to_B_timeout = 3
```

event generation(line:46-50)

## 3.运行 Run this program(main.py)
按q以结束进程
> Press q to end the process
