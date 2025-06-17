
# 🩺 Radiology Report Summarizer

A lightweight web app for summarizing radiology reports using a pre-trained BART model (`facebook/bart-large-cnn`). 
Built with [Streamlit](https://streamlit.io) and [Hugging Face Transformers](https://huggingface.co/docs/transformers).

---

## 📂 Project Structure
```
.
├── app.py                           # Streamlit web app
├── test-train.ipynb                # Jupyter notebook for training/testing
├── synthetic_radiology_reports.csv # Sample dataset (synthetic)
├── rad_summarizer_model/           # (Optional) Fine-tuned model directory
└── README.md                       # Project documentation
```

---

## 🚀 Features

- ✅ User input box for raw radiology report
- ✅ One-click summarization using `facebook/bart-large-cnn`
- ✅ Clean and responsive web interface
- ✅ Ready to deploy on Streamlit Cloud or locally

---

## 💻 Installation

### 1. Clone the repo or copy the files into a folder:
```bash
git clone https://github.com/your-username/radiology-summarizer.git
cd radiology-summarizer
```

### 2. Create a virtual environment (optional but recommended):
```bash
conda create -n rad-nlp python=3.10
conda activate rad-nlp
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install streamlit transformers torch pandas
```

---

## 🧠 Usage

To run the app locally:
```bash
streamlit run app.py
```

Open the browser at: [http://localhost:8501](http://localhost:8501)

---

## 📊 Dataset

A synthetic dataset (`synthetic_radiology_reports.csv`) is provided with 5,000+ report-summary pairs for training or testing. You can extend this with real datasets like:
- [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.0.0/)
- [OpenI Chest X-ray](https://openi.nlm.nih.gov/faq)

---

## 📈 Fine-tuning (Optional)

The notebook `test-train.ipynb` contains code to:
- Fine-tune BART using the synthetic dataset
- Split data into train/test sets
- Generate and compare model summaries

---

## 🌐 Deployment

You can deploy the app to:
- **Streamlit Cloud**: [streamlit.io/cloud](https://streamlit.io/cloud)
- **Hugging Face Spaces** (with `gradio` or `streamlit`)

---

## 📎 Example Input

```
There is a 2.4 x 1.8 cm soft tissue nodule in the right upper lobe. No pleural effusion or pneumothorax. Heart size is normal. Aortic root measures 3.2 cm.
```

### ✅ Example Output

```
2.4 cm nodule in right upper lobe. No effusion or pneumothorax. Normal heart and aortic dimensions.
```

---

## 👨‍⚕️ Authors
- Muhammad Ibrahim Kashif
- Hamna Imran

---

