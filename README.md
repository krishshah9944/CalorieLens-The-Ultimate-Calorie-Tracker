# 🍽️ CalorieLens: The Ultimate Calorie Tracker

## 🚀 Overview

CalorieLens is an AI-powered calorie tracker that analyzes food images to estimate calorie intake and provide detailed nutritional information. Using **Google Gemini AI** and **Streamlit**, this application helps users track their dietary habits effortlessly by identifying food items, estimating portion sizes, and calculating nutritional values.

## ✨ Features

- 📷 **Image-Based Calorie Estimation**: Upload an image of your meal, and the AI will identify food items and estimate their nutritional values.
- 🏷️ **Detailed Nutritional Breakdown**: Get a structured breakdown of calories, protein, fat, carbohydrates, and fiber for each food item.
- 🤖 **Powered by Google Gemini AI**: Utilizes **Google's Gemini 1.5-Flash** model for accurate food recognition and analysis.
- ⚡ **Fast & User-Friendly Interface**: Built with Streamlit for a seamless user experience.

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **LLM Model**: Google Gemini 1.5-Flash
- **AI Framework**: LangChain
- **Image Processing**: PIL (Python Imaging Library)

## 🔧 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/krishshah9944/CalorieLens-The-Ultimate-Calorie-Tracker.git
cd CalorieLens-The-Ultimate-Calorie-Tracker
```

### 2️⃣ Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key

Create a `secrets.toml` file inside the `.streamlit` directory and add your Google API key:

```toml
[secrets]
GOOGLE_API_KEY="your_google_api_key_here"
```

Alternatively, you can configure the key in your environment variables.

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

## 🌍 Live Demo

Try out the application here: [CalorieLens Demo](https://calorielens-the-ultimate-calorie-tracker.streamlit.app/)

## 📌 Usage

1️⃣ **Upload a food image** through the Streamlit interface.

2️⃣ Click **"Calculate Calories"** to process the image.

3️⃣ The AI will analyze the image and provide a **detailed nutritional breakdown**, including calorie count and macronutrient percentages.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements and bug fixes.

## 📧 Contact

For inquiries, please reach out via:

- **LinkedIn**: [Krish Shah](https://www.linkedin.com/in/krishshah9944/)
- **Email**: [krishshah9944@gmail.com](mailto:krishshah9944@gmail.com)


