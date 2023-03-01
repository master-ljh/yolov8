from ultralytics import YOLO

# 成功运行了，找不到coco128，就自己下载了一个数据集
# # Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# # Use the model
# model.train(data="coco128.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("/home/ljh/yolov8/ultralytics/bus.jpg")  # predict on an image
# success = model.export(format="onnx")  # export the model to ONNX format

model = YOLO("/home/ljh/yolov8/ultralytics/yolov5_seg_best.pt")
print(model())
