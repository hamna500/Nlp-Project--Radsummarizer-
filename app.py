import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# Load model and tokenizer once
@st.cache_resource
def load_model():
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    return tokenizer, model

tokenizer, model = load_model()

# Streamlit UI
st.title("🩺 Radiology Report Summarizer")

st.write("Paste a full radiology report below and click **Submit** to generate a concise summary.")

# Input box
user_input = st.text_area("Enter Radiology Report", height=200)

# Submit button
if st.button("Submit") and user_input.strip() != "":
    with st.spinner("Generating summary..."):
        inputs = tokenizer([user_input], return_tensors="pt", max_length=1024, truncation=True)
        with torch.no_grad():
            summary_ids = model.generate(
                inputs['input_ids'],
                num_beams=4,
                length_penalty=2.0,
                max_length=100,
                min_length=20,
                no_repeat_ngram_size=3
            )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Output section
    st.subheader("📄 Generated Summary")
    st.success(summary)
