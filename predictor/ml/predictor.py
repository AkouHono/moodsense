from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

MODEL_PATH = os.environ["MODEL_PATH"]
HF_TOKEN = os.environ["HF_TOKEN"]

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    token=HF_TOKEN
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    token=HF_TOKEN
)

model.eval()

id2label = {
    0: "anger",
    1: "fear",
    2: "joy",
    3: "love",
    4: "sadness",
    5: "surprise"
}


def predict_emotion(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    prediction = torch.argmax(outputs.logits, dim=1).item()

    return id2label[prediction]