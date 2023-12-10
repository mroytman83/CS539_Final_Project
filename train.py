import torch
from ultralytics import YOLO
import torch.nn
from PIL import Image

device: str = "cuda" if torch.cuda.is_available() else "mps"

print(device)

yolo_train = YOLO('yolov5n.pt')

yolo_train.to(device)

path="./datasets/data.yaml"

yolo_train.train(data=path, epochs=40)

def run_yolo(yolo, image_url, conf=0.25, iou=0.7):
    results = yolo(image_url, conf=conf, iou=iou)
    res = results[0].plot()[:, :, [2,1,0]]
    return Image.fromarray(res)

#not sure how to configure runs to a different directory
yolo_train_final= YOLO('./runs/detect/train/weights/best.pt')

image_url = './datasets/test/images/20231016_174531_jpg.rf.9d1c944ca270dc8c1cd248aa0b2befaa.jpg'

image_train=run_yolo(yolo_train_final, image_url)

image_train.save("train.jpeg")