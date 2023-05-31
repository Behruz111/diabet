import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle


m = pickle.load(open("diabet4.pkl",'rb'))

st.title("Bemorlar kamida 21 yoshli ayollari.")



st.title("Pregnancies: homilador bo'lish soni")
st.title("Glucose: glyukozaga test natijasi")
st.title("BloodPressure: diastolik qon bosimi (mm Hg)")
st.title("SkinThickness: Triceps teri burmasining qalinligi (mm)")
st.title("Insulin: 2 soatlik sarum insulini (mu U/ml)")
st.title("BMI: Tana massasi indeksi (vazn kg / (m bo'yi) ^ 2)")
st.title("DiabetesPedigreeFunction: diabetning naslchilik funktsiyasi")
st.title("Age: Yosh (yil)")
st.title("Outcome: Class (0 - diabet yo'q, 1 - diabet)")
                

def pre(kiruvchidata):
    i = np.array(kiruvchidata)

    ir = i.reshape(1, -1)
    p = m.predict(ir)

    if p == 1:
        return  "Diabet kassaligiga chalingan"
    else:
        return  "Diabet kassaligiga chalinmagan"    

    
    

def main():
    
    p = st.text_input("Pregnancies:")
    g = st.text_input("Glucose:")
    bl = st.text_input("BloodPressure:")
    s = st.text_input("SkinThickness:")
    i = st.text_input("Insulin:")
    bm = st.text_input("BMI:")
    d = st.text_input("DiabetesPedigreeFunction:")
    a = st.text_input("Age:")

    pred = ''

    if st.button("Yakuniy natija"):
        p = float(p)
        g = float(g)
        bl = float(bl)
        s = float(s)
        i = float(i)
        bm = float(bm)
        d = float(d)
        a = float(a)

        pred = pre([p,g,bl,s,i,bm,d,a])
        

        st.success(pred)


if __name__ == '__main__':
    main()



