from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import os 
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from PIL import Image


# os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
api_key=st.secrets["GOOGLE_API_KEY"]
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=api_key)


def get_response(input_prompt,image):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input_prompt,image[0]])
    return response.text


def image(file):
    if file is not None:
        bytes= file.getvalue()

        image_parts=[
                {
                "mime_type":file.type,
                "data":bytes
                }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not found")
    

st.set_page_config("CalorieLens")
st.header("CalorieLens: The Ultimate Calorie Tracker")


uploaded_file=st.file_uploader("Please upload the image",type=['jpeg','png','jpg'])
if uploaded_file is not None:
    img= Image.open(uploaded_file)
    st.image(img,caption="Uploaded Image",use_container_width=True)

prompt='''You are a food and nutrition assistant. Analyze the given image of food to identify the items present, estimate portion sizes, and calculate the approximate calorie count. Respond with a structured breakdown of nutritional information for each item and a total summary. Ensure your output is formatted as shown below:
Detected Food Items:  
1. Grilled Chicken Breast (150g)  
   - Calories: 165 kcal  
   - Protein: 31g  
   - Fat: 3.6g  
   - Carbohydrates: 0g  
   _ Fibres: 2g

2. Steamed Broccoli (100g)  
   - Calories: 35 kcal  
   - Protein: 2.8g  
   - Fat: 0.4g  
   - Carbohydrates: 7g
   - Fibres: 2g  

3. Mashed Potatoes with Butter (200g)  
   - Calories: 180 kcal  
   - Protein: 3.5g  
   - Fat: 8g  
   - Carbohydrates: 26g
   - Fibres: 2g  

**Total Nutritional Summary:**  
- Calories: 380 kcal  
- Protein: 37.3g  
- Fat: 12g  
- Carbohydrates: 33g 
- Fibres: 2g 

provide total calories and percentage of carbohydrates,fibres,protein,fat
'''


if st.button("Calculate Calories"):
    if uploaded_file is not None:
        try:
            uploaded = image(uploaded_file)
            response = get_response(prompt, uploaded)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image.")
