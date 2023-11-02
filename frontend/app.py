import streamlit as st
import requests
import joblib

# Load the Categorical Column values to show as option
ohe = joblib.load("artifacts/ohe.pkl")
cat_dict = {}
for idx, category in enumerate(ohe.categories_):
    cat_dict[ohe.feature_names_in_.tolist()[idx]] = category.tolist()

oe = joblib.load("artifacts/oe.pkl")


# URL of your FastAPI application
URL = "http://localhost:8000/api/v1/long_term_deposit/predict"

st.title('Telemarketing Data Input')

# Create form fields for each attribute
age = st.number_input('Age', min_value=0, max_value=100, value=25)
job = st.selectbox('Job', cat_dict['job'])
marital = st.selectbox('Marital', cat_dict['marital'])
education = st.selectbox('Education', oe.categories_[0].tolist())
default = st.selectbox('Default', ["yes", "no"])
balance = st.number_input('Balance', min_value=0, value=0)
housing = st.selectbox('Housing', ["yes", "no"])
loan = st.selectbox('Loan', ["yes", "no"])
contact = st.selectbox('Contact', cat_dict["contact"])
month = st.selectbox('Month', cat_dict["month"])
day = st.number_input('Day', min_value=1, max_value=31, value=1)
duration = st.number_input('Duration', min_value=0, value=0)
campaign = st.number_input('Campaign', min_value=0, value=0)
pdays = st.number_input('Pdays', min_value=-1, value=0)
previous = st.number_input('Previous', min_value=0, value=0)
poutcome = st.selectbox('Poutcome', cat_dict["poutcome"])

if st.button('Submit'):
    # Create a dictionary with the input data
    data = {
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'month': month,
        'day': day,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome
    }

    # Send a POST request to the FastAPI application
    response = requests.post(URL, json=data, timeout=30)

    # Display the response
    if response.status_code == 200:
        st.success('Data submitted successfully')
        st.json(response.json())
    else:
        st.error('An error occurred')
