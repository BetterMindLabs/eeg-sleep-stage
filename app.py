import streamlit as st
import google.generativeai as genai

# === Configure Gemini ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Streamlit UI ===
st.set_page_config(page_title="EEG Sleep Stage Classifier")
st.title("EEG Sleep Stage Classifier")
st.write("Adjust EEG features using the sliders. The system will classify the likely sleep stage.")

# === Sliders for EEG features ===
alpha = st.slider("Alpha Wave Dominance", 0, 10, 4)
delta = st.slider("Delta Wave Presence", 0, 10, 6)
spindles = st.slider("Spindle Activity", 0, 10, 3)
rem_markers = st.slider("REM Markers (Eye Movement)", 0, 10, 2)
muscle_tone = st.slider("Muscle Tone", 0, 10, 5)
noise = st.slider("Signal Noise/Artifacts", 0, 10, 1)

# === Predict Button ===
if st.button("Classify Sleep Stage"):
    with st.spinner("Analyzing EEG signals..."):
        prompt = f"""
You are a sleep stage classification model that predicts stages from EEG features.

Given the values below, predict the most likely sleep stage from:
[Wake, N1, N2, N3, REM]

EEG Feature Scores (0–10 scale):
- Alpha Wave Dominance: {alpha}
- Delta Wave Presence: {delta}
- Spindle Activity: {spindles}
- REM Indicators (Eye Movement): {rem_markers}
- Muscle Tone: {muscle_tone}
- Noise/Artifacts: {noise}

Respond strictly in the format:
Stage: <Predicted Stage>  
Confidence: <Score>% (between 0 and 95)
"""

        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("Prediction Result")
        st.text(result)
