import streamlit as st
import google.generativeai as genai

# Configure Gemini
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="EEG Sleep Stage Classifier")
st.title("EEG Sleep Stage Classifier")
st.write("Paste EEG signal features or textual interpretation. The system will classify the likely sleep stage.")

# Input
eeg_features = st.text_area(
    "Enter EEG Feature Summary",
    height=250,
    placeholder="Example: Alpha waves dominant, high-frequency bursts, low delta activity..."
)

# Button
if st.button("Classify Sleep Stage") and eeg_features.strip():
    with st.spinner("Classifying..."):
        prompt = f"""
You are a trained EEG analysis model for sleep stage classification. Given the EEG signal features below, classify the most probable sleep stage:

Possible classes:
- Wake
- N1 (light sleep)
- N2 (moderate sleep)
- N3 (deep sleep)
- REM (rapid eye movement)

EEG Features:
\"\"\"{eeg_features}\"\"\"

Respond with:
Stage: <Predicted Stage>  
Confidence: <Score>% (0–95)
"""

        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("Prediction Result")
        st.text(result)
