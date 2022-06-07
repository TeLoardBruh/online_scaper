import streamlit as st
import json

def load_data(title):
    with open(title,encoding='utf-8') as f:
        return json.load(f)
    
loadProductData = load_data("./data/chipmok_store_pirce")

