import logging
import os
import joblib
import cv2
import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile, File

app = FastAPI(docs_url='/', title="VC MASTER - PUC-Rio")


def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image_clahe = clahe.apply(image)
    return image_clahe


def normalize_data(image):
    return image.astype('float32') / 255.0


def flatten_data(image):
    return image.flatten().reshape(1, -1)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Carregar pipeline de inferência
    pipeline = joblib.load('pipeline.pkl')

    # Ler a imagem
    image = Image.open(file.file).convert("L")
    img_array = np.array(image)

    # Pré-processamento
    image = apply_clahe(img_array)
    image = normalize_data(image)
    image = flatten_data(image)

    # Fazer a predição
    predictions = pipeline.predict(image)

    return {"Prediction": predictions.tolist()}
