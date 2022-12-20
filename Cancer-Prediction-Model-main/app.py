import os
import streamlit as st
import pickle
import numpy as np

mydir = 'C:/Users/jathi/PycharmProjects/RTA/Cancer-Prediction-Model-main'
myfile = 'CancerPredictonModel.pkl'
filename = os.path.join(mydir, myfile)
model = pickle.load(open(filename,'rb'))

def predict_diabetes(age,drycough,smoking,balanceddiet,alcohol,obesity):
    input = np.array([[age,drycough,smoking,balanceddiet,alcohol,obesity]]).astype(np.float64)
    prediction = model.predict(input)
    return float(prediction)

def main():
    st.title("Cancer Prediction ")
    html_temp = """
    <div style="background-color= #EEEEE ;padding:10px">
    <h2 style="color:black;text-align:center;">Cancer Prediction Application</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("Age", " ")
    drycough = st.text_input("Dry Cough level", " ")
    fatigue = st.text_input("Smoking Level", " ")
    balanceddiet = st.text_input("Balanced Diet level", " ")
    alcohol = st.text_input("Alcohol Consumption", " ")
    obesity = st.text_input("Obesity", " ")
    safe_html = """
    <div style="background-color:#F4D03F;padding:10px >
    <h2 style="color:white;text-align:center;">You are safe.Lead a healthy Lifestyle!!</h2>
    </div>
    """
    danger_html= """
    <div style="background-color:#F00000;padding:10px >
    <h2 style="color:white;text-align:center;">You are not safe,get checked OUT!!</h2>
    </div>
    """

    if st.button("Predict"):
        output=predict_diabetes(age,drycough,fatigue,balanceddiet,alcohol,obesity)
        if not output >0.5:
            a ="Low probability for Cancer"
        else:
            a="High probability for Cancer"
        st.success("{}".format(a))

        if output <=0.7:
            st.markdown(safe_html,unsafe_allow_html=True)
        else:
            st.markdown(danger_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()