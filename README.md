# 🏠 ML-Based Real Estate Price Estimator

This is a machine learning project that predicts house prices based on user-provided features such as location, area (sq ft), number of bedrooms, and number of bathrooms. The application is built using **Streamlit** and deployed on **Streamlit Cloud** for real-time predictions.

## 🚀 Live Demo

👉 [Open App](https://real-estate-ml-model-akvtmypd7ypjsusz5b5grr.streamlit.app/)  
👉 [GitHub Repository](https://github.com/Karanbrar12/real-estate-ml-model)

---

## 🔍 Features

- Interactive UI for inputting house details
- Real-time price prediction
- Model trained using:
  - **Linear Regression**
  - **Random Forest Regressor**
- Clean and responsive interface built with Streamlit

---

## 🧠 Machine Learning Models

The application uses two models:
- **Linear Regression** for a baseline prediction
- **Random Forest Regressor** for improved accuracy and performance

The models are trained on a cleaned dataset of real estate prices using common preprocessing techniques like:
- Label encoding for location
- Feature scaling
- Handling categorical variables

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **pandas**
- **NumPy**
- **scikit-learn**
- **matplotlib** (for development)

---

## 📁 File Structure

```
real-estate-ml-model/
├── app.py                # Streamlit application
├── model.pkl             # Trained Random Forest model
├── linear_model.pkl      # Trained Linear Regression model
├── data.csv              # Dataset used for training
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📦 Installation (Local Setup)

```bash
# Clone the repository
git clone https://github.com/Karanbrar12/real-estate-ml-model.git
cd real-estate-ml-model

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📈 Future Improvements

- Add data visualization (e.g., price trends)
- Integrate more advanced models like XGBoost or LightGBM
- Allow location-specific model tuning

---

## 🙋‍♂️ Author

**Karan Inder Singh Brar**  
📧 karanbrarfdk1@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/karan-inder-singh-brar-1286b0349)

---

## 📄 License

This project is licensed under the MIT License.
