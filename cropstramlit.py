
import pandas as pd
import streamlit as st
import pickle


pickle_in= open("crop2.pkl","rb")
classifier = pickle.load(pickle_in)


def predict_note_authentication(N,P,K,temperature,humidity,ph,rainfall):
    prediction = classifier.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    print(prediction)
    return prediction


def main():
    #st.title("crop analyzer")


    html_temp = """
    
        <style>body {
        background-image: url("https://unsplash.com/photos/2oYMwuFgnTg");
        background_size:cover
        </body>
        </style>
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit crops Analyzer ML App </h2>
        </div>
        
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.write("""
    # Crop Prediction App
    This app predicts the **crop ** species to be grown!
    Data obtained from the [Indian village](https://github.com/animeesh/crop-field-prediction/blob/main/data1.csv) in python by Animesh Nayak.
    """)

    st.sidebar.header('User Input Features')

    st.sidebar.markdown("""
    [Example CSV input file](https://github.com/animeesh/crop-field-prediction/blob/main/indiancrop.csv)
    """)

    # Collects user input features into dataframe
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        input = pd.read_csv(uploaded_file)
    else:


        N = st.sidebar.slider('Nitrogen (ppm)', 0, 140, 70)
        P = st.sidebar.slider('phosphorus (ppm)', 5, 150, 100)
        K = st.sidebar.slider('Potassium (ppm)', 5, 215, 170)
        temperature = st.sidebar.slider('temperature(degrees)', 7.00, 45.00, 28.00)
        humidity = st.sidebar.slider('humidity', 10.00, 100.00, 50.00)
        ph = st.sidebar.slider('ph', 3.00, 10.00, 5.00)
        rainfall = st.sidebar.slider('rainfall (mm)', 20.00, 300.00, 200.00)
        result = ""

        data = {'N': N,
                'P': P,
                'K': K,
                'temperature': temperature,
                'humidity': humidity,
                'ph': ph,
                'rainfall': rainfall}

        features = pd.DataFrame(data, index=[0])

        st.subheader('User Input features')

        if uploaded_file is not None:
            st.write(features)
        else:
            st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
            st.write(features)




        if st.button("Predict"):
            result = predict_note_authentication(N,P,K,temperature,humidity,ph,rainfall)
        st.success('The output is {}'.format(result))
        if st.button("About"):
            st.text("Lets LEarn")
            st.write("""
                ## Hi there 👋
                ## 👋 Hi, I’m @Animesh Nayak
                ## 👀 I’m interested in @machine learning in python
                ## 🌱 I’m currently learning @deep learning & computer vision
                ## 💞️ I’m looking to collaborate on [@github](https://github.com/animeesh) repos
                ## 📫 How to reach me [linkedin] (www.linkedin.com/in/animeshnayak)
                
                 
                """)

            st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
