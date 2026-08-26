import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Student Success Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD MODEL
# =========================================================
MODEL_PATH = Path(__file__).parent / "model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("❌ Could not load model.pkl")
    st.exception(e)
    st.stop()

# =========================================================
# PREMIUM DARK BLUE + PURPLE THEME
# =========================================================
st.markdown("""
<style>

/* =====================================================
   MAIN BACKGROUND
===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(99, 102, 241, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 95% 10%,
            rgba(168, 85, 247, 0.15),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #070b17 0%,
            #0f172a 48%,
            #17123b 100%
        );

    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* =====================================================
   GENERAL TEXT
===================================================== */

.stApp p {
    color: #cbd5e1 !important;
}

.stApp label {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
}

/* =====================================================
   SIDEBAR
===================================================== */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #080d1c 0%,
            #111827 55%,
            #17133b 100%
        ) !important;

    border-right: 1px solid rgba(139, 92, 246, 0.28);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4 {
    color: #ffffff !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #cbd5e1 !important;
}

/* Sidebar metrics */

[data-testid="stSidebar"] [data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.90),
            rgba(15, 23, 42, 0.90)
        ) !important;

    border: 1px solid rgba(129, 140, 248, 0.20) !important;
    border-radius: 16px !important;
    padding: 15px !important;
}

/* =====================================================
   HERO CONTAINER
===================================================== */

.hero-box {
    background:
        linear-gradient(
            135deg,
            rgba(79, 70, 229, 0.30),
            rgba(124, 58, 237, 0.18)
        );

    border: 1px solid rgba(139, 92, 246, 0.38);

    border-radius: 24px;

    padding: 32px 38px;

    margin-bottom: 30px;

    box-shadow:
        0 20px 55px rgba(0, 0, 0, 0.30);
}

/* =====================================================
   SECTION BOX
===================================================== */

.section-box {
    background:
        rgba(30, 41, 59, 0.62);

    border: 1px solid rgba(129, 140, 248, 0.16);

    border-left: 5px solid #8b5cf6;

    border-radius: 16px;

    padding: 17px 22px;

    margin-top: 30px;
    margin-bottom: 20px;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.15);
}

/* =====================================================
   SLIDERS
===================================================== */

[data-testid="stSlider"] {
    background: rgba(15, 23, 42, 0.60);

    padding: 15px;

    border-radius: 15px;

    border: 1px solid rgba(148, 163, 184, 0.12);
}

/* Slider numbers */

[data-testid="stSlider"] span {
    color: #cbd5e1 !important;
}

/* =====================================================
   SELECT BOX
===================================================== */

[data-baseweb="select"] > div {
    background-color: #111827 !important;

    border: 1px solid #334155 !important;

    border-radius: 11px !important;
}

[data-baseweb="select"] * {
    color: #f8fafc !important;
}

[data-baseweb="popover"] {
    background-color: #111827 !important;
}

[data-baseweb="menu"] {
    background-color: #111827 !important;
}

[role="option"] {
    background-color: #111827 !important;
    color: #f8fafc !important;
}

[role="option"]:hover {
    background-color: #312e81 !important;
}

/* =====================================================
   PREDICTION BUTTON
===================================================== */

.stButton > button {
    width: 100%;

    min-height: 58px;

    border-radius: 15px;

    border: 1px solid rgba(167, 139, 250, 0.50);

    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #7c3aed,
            #8b5cf6
        );

    color: #ffffff !important;

    font-size: 18px;

    font-weight: 800;

    box-shadow:
        0 12px 32px rgba(99, 102, 241, 0.25);

    transition: 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 18px 40px rgba(139, 92, 246, 0.35);

    border-color: #c4b5fd;
}

/* =====================================================
   METRIC CARDS
===================================================== */

[data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.92),
            rgba(15, 23, 42, 0.92)
        ) !important;

    border: 1px solid rgba(129, 140, 248, 0.22) !important;

    border-radius: 18px !important;

    padding: 20px !important;

    box-shadow:
        0 12px 30px rgba(0, 0, 0, 0.22);
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;

    font-weight: 800 !important;
}

/* =====================================================
   RESULT BOX
===================================================== */

.result-box {
    background:
        linear-gradient(
            135deg,
            rgba(79, 70, 229, 0.25),
            rgba(30, 41, 59, 0.85)
        );

    border: 1px solid rgba(139, 92, 246, 0.35);

    border-radius: 22px;

    padding: 30px;

    text-align: center;

    margin-bottom: 25px;

    box-shadow:
        0 20px 50px rgba(0, 0, 0, 0.28);
}

/* =====================================================
   TABLE
===================================================== */

[data-testid="stDataFrame"] {
    border-radius: 15px;

    overflow: hidden;

    border: 1px solid #334155;
}

/* =====================================================
   PROGRESS
===================================================== */

[data-testid="stProgressBar"] {
    background-color: #1e293b !important;
}

[data-testid="stProgressBar"] > div > div {
    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #8b5cf6
        );
}

/* =====================================================
   ALERTS
===================================================== */

.stAlert {
    border-radius: 15px !important;
}

/* =====================================================
   DIVIDERS
===================================================== */

hr {
    border-color: rgba(148, 163, 184, 0.15) !important;
}

/* =====================================================
   FOOTER
===================================================== */

.footer-text {
    text-align: center;

    padding: 25px;

    margin-top: 30px;

    color: #64748b !important;

    border-top: 1px solid rgba(148, 163, 184, 0.12);
}

/* =====================================================
   HIDE STREAMLIT BRANDING
===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🎓 Student Success")

    st.caption(
        "End-to-End Machine Learning Product"
    )

    st.divider()

    st.markdown("### 🧠 Model")

    st.markdown("**Ridge Regression**")

    st.caption(
        "Selected after comparing multiple regression algorithms."
    )

    st.divider()

    st.markdown("### 📊 Model Performance")

    st.metric(
        "R² Score",
        "0.770"
    )

    st.metric(
        "MAE",
        "0.454"
    )

    st.metric(
        "RMSE",
        "1.803"
    )

    st.divider()

    st.markdown("### 🛠️ Tech Stack")

    st.write("🐍 Python")
    st.write("🐼 Pandas / NumPy")
    st.write("🤖 Scikit-learn")
    st.write("🎨 Streamlit")
    st.write("💾 Joblib")

    st.divider()

    st.info(
        "Built as an End-to-End ML Capstone project."
    )


# =========================================================
# MAIN HERO
# =========================================================

st.markdown("""
<div class="hero-box">
    <h1>🎓 Student Success Predictor</h1>
    <h2>End-to-End Machine Learning Capstone</h2>
    <p>
        Predict expected student exam performance using academic,
        learning, family, and school-related factors.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# ACADEMIC PROFILE
# =========================================================

st.markdown("""
<div class="section-box">
    <h2>📚 Academic Profile</h2>
    <p>Enter the student's academic and daily learning information.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:

    hours = st.slider(
        "📚 Hours Studied / Week",
        0,
        50,
        20
    )

with c2:

    attendance = st.slider(
        "📅 Attendance (%)",
        0,
        100,
        80
    )

with c3:

    previous = st.slider(
        "🎯 Previous Scores",
        40,
        100,
        70
    )

with c4:

    sleep = st.slider(
        "😴 Sleep Hours",
        1,
        12,
        7
    )


# =========================================================
# LEARNING ENVIRONMENT
# =========================================================

st.markdown("""
<div class="section-box">
    <h2>🏫 Learning Environment</h2>
    <p>Information about learning habits and available resources.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:

    tutoring = st.slider(
        "👨‍🏫 Tutoring Sessions",
        0,
        10,
        2
    )

with c2:

    physical = st.slider(
        "🏃 Physical Activity (Hours)",
        0,
        10,
        3
    )

with c3:

    motivation = st.selectbox(
        "🔥 Motivation Level",
        ["Low", "Medium", "High"]
    )

with c4:

    resources = st.selectbox(
        "📖 Access to Resources",
        ["Low", "Medium", "High"]
    )


# =========================================================
# SUPPORT & BACKGROUND
# =========================================================

st.markdown("""
<div class="section-box">
    <h2>👨‍👩‍👧 Support & Background</h2>
    <p>Family support and background information.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:

    parental = st.selectbox(
        "👪 Parental Involvement",
        ["Low", "Medium", "High"]
    )

with c2:

    education = st.selectbox(
        "🎓 Parental Education",
        [
            "High School",
            "College",
            "Postgraduate"
        ]
    )

with c3:

    income = st.selectbox(
        "💰 Family Income",
        ["Low", "Medium", "High"]
    )

with c4:

    peer = st.selectbox(
        "👥 Peer Influence",
        [
            "Negative",
            "Neutral",
            "Positive"
        ]
    )


# =========================================================
# SCHOOL & PERSONAL FACTORS
# =========================================================

st.markdown("""
<div class="section-box">
    <h2>🌐 School & Personal Factors</h2>
    <p>School environment, technology access, and personal factors.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:

    teacher = st.selectbox(
        "👨‍🏫 Teacher Quality",
        ["Low", "Medium", "High"]
    )

with c2:

    school = st.selectbox(
        "🏫 School Type",
        ["Public", "Private"]
    )

with c3:

    internet = st.selectbox(
        "🌐 Internet Access",
        ["No", "Yes"]
    )

with c4:

    extracurricular = st.selectbox(
        "⚽ Extracurricular Activities",
        ["No", "Yes"]
    )

c1, c2, c3 = st.columns(3)

with c1:

    disability = st.selectbox(
        "🧩 Learning Disabilities",
        ["No", "Yes"]
    )

with c2:

    distance = st.selectbox(
        "🏠 Distance from Home",
        [
            "Near",
            "Moderate",
            "Far"
        ]
    )

with c3:

    gender = st.selectbox(
        "👤 Gender",
        ["Male", "Female"]
    )


# =========================================================
# PREDICTION SECTION
# =========================================================

st.divider()

st.markdown("""
<div class="section-box">
    <h2>🚀 Generate Prediction</h2>
    <p>Review the student profile and generate an estimated exam score.</p>
</div>
""", unsafe_allow_html=True)

predict = st.button(
    "🚀 Predict Expected Exam Score",
    type="primary",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict:

    row = pd.DataFrame([{

        "Hours_Studied": hours,

        "Attendance": attendance,

        "Parental_Involvement": parental,

        "Access_to_Resources": resources,

        "Extracurricular_Activities": extracurricular,

        "Sleep_Hours": sleep,

        "Previous_Scores": previous,

        "Motivation_Level": motivation,

        "Internet_Access": internet,

        "Tutoring_Sessions": tutoring,

        "Family_Income": income,

        "Teacher_Quality": teacher,

        "School_Type": school,

        "Peer_Influence": peer,

        "Physical_Activity": physical,

        "Learning_Disabilities": disability,

        "Parental_Education_Level": education,

        "Distance_from_Home": distance,

        "Gender": gender

    }])


    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    row["Study_Attendance_Index"] = (
        row["Hours_Studied"]
        * row["Attendance"]
        / 100
    )

    row["Academic_Consistency"] = (
        row["Previous_Scores"]
        + row["Attendance"]
    ) / 2

    row["Study_Sleep_Index"] = (
        row["Hours_Studied"]
        * row["Sleep_Hours"]
    )


    # =====================================================
    # MODEL PREDICTION
    # =====================================================

    try:

        prediction = float(
            model.predict(row)[0]
        )

        prediction = float(
            np.clip(
                prediction,
                0,
                100
            )
        )

    except Exception as e:

        st.error(
            "❌ Prediction failed. Check that model.pkl was trained "
            "with the same feature names and preprocessing."
        )

        st.exception(e)

        st.stop()


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.markdown("""
    <div class="section-box">
        <h2>📊 Prediction Result</h2>
        <p>Machine learning estimate based on the entered student profile.</p>
    </div>
    """, unsafe_allow_html=True)


    # Result card

    st.markdown(f"""
    <div class="result-box">
        <h3>🎯 Predicted Exam Score</h3>
        <div style="font-size:48px;font-weight:800;color:#ffffff;">
            {prediction:.1f}%
        </div>
        <p>Expected Student Performance</p>
    </div>
    """, unsafe_allow_html=True)


    # =====================================================
    # RESULT METRICS
    # =====================================================

    r1, r2, r3, r4 = st.columns(4)

    with r1:

        st.metric(
            "🎯 Predicted Score",
            f"{prediction:.1f} / 100"
        )

    with r2:

        st.metric(
            "📅 Attendance",
            f"{attendance}%"
        )

    with r3:

        st.metric(
            "📚 Previous Score",
            f"{previous}"
        )

    with r4:

        st.metric(
            "⏱️ Study Hours",
            f"{hours}"
        )


    # =====================================================
    # PERFORMANCE INDICATOR
    # =====================================================

    st.subheader("📈 Performance Indicator")

    st.progress(
        int(round(prediction)),
        text=f"Predicted Score: {prediction:.1f}%"
    )


    # =====================================================
    # INTERPRETATION
    # =====================================================

    if prediction >= 80:

        st.success(
            "🌟 Strong predicted performance — the current profile "
            "shows several positive academic indicators."
        )

    elif prediction >= 70:

        st.info(
            "👍 Good predicted performance — maintaining consistent "
            "attendance and study habits may support further improvement."
        )

    elif prediction >= 60:

        st.warning(
            "📌 Moderate predicted performance — stronger study "
            "consistency or additional academic support may help."
        )

    else:

        st.warning(
            "📚 Additional academic support may be useful based on "
            "the model's estimate."
        )


    # =====================================================
    # PROFILE + ENGINEERED FEATURES
    # =====================================================

    left, right = st.columns(2)


    # =====================================================
    # PROFILE SUMMARY
    # =====================================================

    with left:

        st.subheader("📋 Student Profile Summary")

        summary = pd.DataFrame({

            "Factor": [

                "Hours Studied / Week",

                "Attendance",

                "Previous Score",

                "Sleep Hours",

                "Tutoring Sessions",

                "Physical Activity",

                "Motivation",

                "Access to Resources",

                "Parental Involvement",

                "Teacher Quality",

                "School Type"

            ],

            "Value": [

                hours,

                f"{attendance}%",

                previous,

                sleep,

                tutoring,

                physical,

                motivation,

                resources,

                parental,

                teacher,

                school

            ]

        })

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )


    # =====================================================
    # ENGINEERED FEATURES
    # =====================================================

    with right:

        st.subheader("🔍 Engineered Features")

        engineered = pd.DataFrame({

            "Feature": [

                "Study × Attendance Index",

                "Academic Consistency",

                "Study × Sleep Index"

            ],

            "Value": [

                round(
                    float(
                        row[
                            "Study_Attendance_Index"
                        ].iloc[0]
                    ),
                    2
                ),

                round(
                    float(
                        row[
                            "Academic_Consistency"
                        ].iloc[0]
                    ),
                    2
                ),

                round(
                    float(
                        row[
                            "Study_Sleep_Index"
                        ].iloc[0]
                    ),
                    2
                )

            ]

        })

        st.dataframe(
            engineered,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            "These engineered indicators combine multiple student "
            "factors for the prediction model."
        )


    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.divider()

    st.caption(
        "⚠️ This is an ML-based estimate for educational and "
        "demonstration purposes. It should not be used as the sole "
        "basis for grading, admission, discipline, or other "
        "high-impact academic decisions."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer-text">
        🎓 Student Success Predictor<br><br>
        End-to-End Machine Learning Capstone<br><br>
        Python • Pandas • NumPy • Scikit-learn • Streamlit • Joblib
    </div>
    """,
    unsafe_allow_html=True
)