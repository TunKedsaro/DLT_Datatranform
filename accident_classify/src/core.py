import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
import pickle
print("Import done")

# Define tokenizer
tokenizer = AutoTokenizer.from_pretrained("airesearch/wangchanberta-base-att-spm-uncased")
model = AutoModel.from_pretrained("airesearch/wangchanberta-base-att-spm-uncased")

# Define embeding
def get_sentence_embedding(sentence):
    try:
        inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True,max_length=512) # Limit token
        with torch.no_grad():
            outputs = model(**inputs)
        vector = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    except:
        print("error")
        inputs = tokenizer("Unknow", return_tensors="pt", padding=True, truncation=True,max_length=512) # Limit token
        with torch.no_grad():
            outputs = model(**inputs)
        vector = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return vector

# open model
with open("/app/models/200225_1318_accident_classify_model.pkl","rb") as f:
    model_loaded = pickle.load(f)

# Endode & Decode
accident_encode = {
    "อุบัติเหตุเกิดจากรถ":0,
    "อุบัติเหตุเกิดจากคน":1,
    "อุบัติเหตุเกิดจากสิ่งแวดล้อม":2
}

accident_decode = {
    0:"อุบัติเหตุเกิดจากรถ",
    1:"อุบัติเหตุเกิดจากคน",
    2:"อุบัติเหตุเกิดจากสิ่งแวดล้อม"
    }

encode = lambda ip : accident_encode[ip]
decode = lambda ip : accident_decode[ip]

# main
def main(sentence = "นาย A ขับรถชนนาย B"):
    vector = get_sentence_embedding(sentence)
    y_pred = model_loaded.predict([vector])
    argmax = np.argmax(y_pred)
    dc = decode(argmax)
    return str(y_pred),str(argmax),dc




