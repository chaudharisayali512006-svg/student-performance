import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Marks Prediction System",
    page_icon="🎓",
    layout="wide"
)

# ---------------- GRADIENT BACKGROUND ----------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #e3f2fd, #fce4ec);
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #1a237e;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;
    }

    .stButton>button {
        background: linear-gradient(to right, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #5a67d8, #6b46c1);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🎓 Student Marks Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Based Academic Performance Predictor</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📘 About System")
st.sidebar.write("This system predicts student marks using Random Forest Machine Learning model.")
st.sidebar.write("Developed by Sayali Chaudhari")

if st.button("🚀 Predict Marks"):

    model = pickle.load(open("model.pkl", "rb"))

    gender_val = 0 if gender == "male" else 1

    course_map = {
        "b.tech": 0, "b.sc": 1, "bca": 2,
        "ba": 3, "bba": 4, "diploma": 5
    }
    course_val = course_map[course]

    difficulty_map = {
        "easy": 0, "moderate": 1, "hard": 2
    }
    exam_val = difficulty_map[exam_difficulty]

    input_data = pd.DataFrame([[ 
        age, gender_val, course_val,
        study_hours, attendance,
        sleep_hours, exam_val
    ]], columns=[
        "age", "gender", "course", "study_hours",
        "attendance", "sleep_hours", "exam_difficulty"
    ])

    predicted_marks = model.predict(input_data)[0]

    st.markdown(f"""
        <div style="
            background: linear-gradient(to right, #d4fc79, #96e6a1);
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:26px;
            font-weight:bold;
            color:#1b5e20;">
            📊 Predicted Marks: {predicted_marks:.2f}
        </div>
    """, unsafe_allow_html=True)