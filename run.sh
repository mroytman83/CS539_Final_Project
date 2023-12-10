#!/bin/bash
python -m venv rock_env
source rock_env/bin/activate
pip install -r requirements.txt
mkdir augmented_datasets
mkdir datasets
cd augmented_datasets
curl -L "https://app.roboflow.com/ds/3N2nm6FqDM?key=4yp5OWCWzd" --output roboflow.zip; unzip roboflow.zip; rm roboflow.zip
cd datasets
curl -L "https://universe.roboflow.com/ds/rTSnBOdeq6?key=9TGU3dYlZ2" --output roboflow.zip; unzip roboflow.zip; rm roboflow.zip
python augmented_train.py
python train.py
