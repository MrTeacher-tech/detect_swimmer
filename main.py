from ultralytics import YOLO
import torch

torch.set_num_threads(8)

model = YOLO("yolov8n.pt")  # Load a pretrained model
results = model.train(data="config.yaml", epochs=350)