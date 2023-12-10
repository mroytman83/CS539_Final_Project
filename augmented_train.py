from ultralytics import YOLO
from PIL import Image
import torch
import inspect

device: str = "cuda" if torch.cuda.is_available() else "mps"

print(device)

yolo_augmented = YOLO('yolov5n.pt')
yolo_augmented.to(device)
path="./augmented_datasets/data.yaml"

yolo_augmented.train(data=path, epochs=40)#, batch=64, cache=True)

def run_yolo(yolo, image_url, conf=0.25, iou=0.7):
    results = yolo(image_url, conf=conf, iou=iou)
    res = results[0].plot()[:, :, [2,1,0]]
    return Image.fromarray(res)

yolo_augmented_final = YOLO('./runs/detect/train/weights/best.pt')

image_url = './augmented_datasets/test/images/20231009_132947_jpg.rf.be0ad1a865cb92c1389a0a9922832661.jpg'

image_augmented_train=run_yolo(yolo_augmented_final, image_url)

image_augmented_train.save("augmented_train.jpeg")