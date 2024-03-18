import streamlit as st
import pickle
import numpy as np
import sklearn


st.title("Wine Quality Predictor")
winetype = st.selectbox("Choose Wine Type:", ("red", "white"))

if winetype == "red":
    loaded_model_red = pickle.load(open("wine_red.sav", 'rb'))



    def red_predictor(input_data_red):
        prediction_red = loaded_model_red.predict([input_data_red])
        return prediction_red


    def main():
        fixedacidity = st.text_input("fixed acidity of wine:")
        volatileacidity = st.text_input("volatile acidity of wine:")
        citricacid = st.text_input("citric acid content of wine:")
        residualsugar = st.text_input("residual sugar:")
        chlorides = st.text_input("chloride content:")
        freesulfurdioxide = st.text_input("free sulfur dioxide content:")
        totalsulfurdioxide = st.text_input("total sulfur dioxide content:")
        density = st.text_input("density of wine:")
        pH = st.text_input("PH of wine:")
        sulphates = st.text_input("total sulphate content:")
        alcohol = st.text_input("alcohol content of wine:")

        if st.button('Quality of Wine:'):
            if all([fixedacidity, volatileacidity, citricacid, residualsugar, chlorides,
                    freesulfurdioxide, totalsulfurdioxide, density, pH, sulphates, alcohol]):
                Quality = red_predictor([fixedacidity, volatileacidity, citricacid, residualsugar, chlorides,
                                         freesulfurdioxide, totalsulfurdioxide, density, pH, sulphates, alcohol])
                st.success(Quality)
            else:
                st.error("Please fill in all input fields.")


    if __name__ == '__main__':
        main()

else:
    loaded_model_white = pickle.load(open("wine_white.sav", 'rb'))


    def white_predictor(input_data_white):
        prediction_white = loaded_model_white.predict([input_data_white])
        return prediction_white


    def main():
        fixedacidity = st.text_input("fixed acidity of wine:")
        volatileacidity = st.text_input("volatile acidity of wine:")
        citricacid = st.text_input("citric acid content of wine:")
        residualsugar = st.text_input("residual sugar:")
        chlorides = st.text_input("chloride content:")
        freesulfurdioxide = st.text_input("free sulfur dioxide content:")
        totalsulfurdioxide = st.text_input("total sulfur dioxide content:")
        density = st.text_input("density of wine:")
        pH = st.text_input("PH of wine:")
        sulphates = st.text_input("total sulphate content:")
        alcohol = st.text_input("alcohol content of wine:")

        if st.button('Quality of Wine:'):
            if all([fixedacidity, volatileacidity, citricacid, residualsugar, chlorides,
                    freesulfurdioxide, totalsulfurdioxide, density, pH, sulphates, alcohol]):
                Quality = white_predictor(
                    [fixedacidity, volatileacidity, citricacid, residualsugar, chlorides, freesulfurdioxide,
                     totalsulfurdioxide, density, pH, sulphates, alcohol])
                st.success(Quality)
            else:
                st.error("Please fill in all input fields.")


    if __name__ == '__main__':
        main()

