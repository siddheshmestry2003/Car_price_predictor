# 🚗 Car Price Predictor Web App

This project is a **Car Price Prediction Web Application** built using **Python (Flask)** and **Machine Learning**. It allows users to estimate the resale value of a used car based on key features like company, model, year, fuel type, and kilometers driven.

## 🔍 Overview

Are you planning to sell your car and want to know its market value?

This application predicts the **resale price** of your car using a trained **Linear Regression model**. Users can interact through a clean and user-friendly web interface built with **HTML, CSS, JavaScript**, and **Bootstrap**.

## 📸 Demo

![App Screenshot](static/images/demo-screenshot.png) <!-- Replace with actual image path -->

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-Learn (Linear Regression)
- **Libraries:** Pandas, NumPy, Pickle

## 📂 Project Structure
Car-Price-Predictor/
│
├── static/
│ └── css/
│ └── style.css
├── templates/
│ └── index.html
├── LinearRegressionModel.pkl
├── clean_car_1.csv
├── app.py
└── README.md



## ⚙️ Features

✅ Predict resale price of a used car  
✅ User-friendly interface with dropdowns  
✅ Dynamic model loading and real-time prediction   
✅ Clean and responsive UI

## 🧠 Machine Learning Details

- **Algorithm:** Linear Regression
- **Target Variable:** Selling price of the car
- **Features Used:**  
  - Car Brand & Model  
  - Year of Purchase  
  - Fuel Type  
  - Kilometers Driven

The model was trained on cleaned and preprocessed dataset using `clean_car_1.csv`.

## 🚀 How to Run Locally

### Prerequisites:

- Python 3.x installed
- pip installed

### Steps:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Car-Price-Predictor.git

# 2. Navigate to project directory
cd Car-Price-Predictor

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
