import streamlit as st
import pickle as pkl

# -------------------- LOAD MODEL --------------------
final_model = pkl.load(open('model.pkl', 'rb'))

# -------------------- MAPPINGS --------------------
d1 = {'Comprehensive': 0, 'Third Party insurance': 1, 'Third Party': 1, 'Zero Dep': 2, 'Not Available': 3}
d2 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
d3 = {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Forth Owner': 4, 'Fifth Owner': 5}
d4 = {'Manual': 0, 'Automatic': 1}

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #7f8c8d;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="title">🚗 Car Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict your car resale value instantly</div>', unsafe_allow_html=True)
st.write("")

# -------------------- FORM --------------------
with st.container():

    st.subheader("📋 Basic Details")
    col1, col2 = st.columns(2)

    with col1:
        val1 = st.selectbox('Insurance Validity', options=list(d1.keys()))
        val2 = st.selectbox('Fuel Type', options=list(d2.keys()))
        val4 = st.selectbox('Ownership', options=list(d3.keys()))

    with col2:
        val5 = st.radio('Transmission', options=list(d4.keys()), horizontal=True)
        val_seats = st.selectbox('Seats', options=[4, 5, 6, 7, 8])
        val_year = st.number_input('Manufacturing Year', min_value=2000, max_value=2025, value=2019)

    st.markdown("---")

    st.subheader("🔧 Performance & Usage")
    col3, col4 = st.columns(2)

    with col3:
        val3 = st.slider('KMs Driven', 0, 200000, 30000, step=500)
        val_mileage = st.slider('Mileage (kmpl)', 5.0, 35.0, 17.0)

    with col4:
        val_engine = st.slider('Engine (cc)', 500, 6000, 1500, step=50)
        val_power = st.slider('Max Power (bhp)', 50.0, 600.0, 120.0)

# -------------------- PREDICTION --------------------
st.markdown("")

if st.button('🔍 Predict Price'):

    test = [[
        d1[val1],
        d2[val2],
        val3,
        d3[val4],
        d4[val5],
        val_seats,
        val_mileage,
        val_engine,
        val_power,
        val_year
    ]]

    yp = final_model.predict(test)[0]
    yp = round(float(yp), 2)

    st.markdown("---")

    # RESULT DISPLAY (MODERN STYLE)
    st.success(f"💰 Estimated Price: ₹ {yp} Lakhs")

    st.markdown(f"""
        <div style="background-color:#ecf0f1;padding:20px;border-radius:10px;text-align:center;">
            <h3>Approx Value</h3>
            <h2 style="color:#27ae60;">₹ {int(yp * 100000):,}</h2>
        </div>
    """, unsafe_allow_html=True)

# -------------------- FOOTER --------------------
st.markdown("""
---
<center>Made with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)