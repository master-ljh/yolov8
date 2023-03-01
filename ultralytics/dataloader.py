# !pip install roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="2Z4xx14CjNYGh4ZCzrf4")
project = rf.workspace("monash-h8dbx").project("tumor-egzxx")
dataset = project.version(1).download("yolov8")
