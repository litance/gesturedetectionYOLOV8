from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 加载预训练模型
model.train(data="", #.yaml datapath
            epochs=50,
            batch=32,
            workers=0,
            device="cuda")  # 训练模型
