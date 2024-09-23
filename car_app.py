import joblib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Car Price Prediction App",
    page_icon=":car:",
    layout="wide"
)

# หัวข้อหลัก
st.title("Car Price Prediction")
st.write("Predict the price of a used car based on various features.")

# Sidebar สำหรับการป้อนข้อมูลผู้ใช้
st.sidebar.header("User Input")
st.sidebar.text("Adjust the settings below to predict the price of the car.")

# ตัวควบคุมการป้อนข้อมูลใน Sidebar
brands = ['Isuzu', 'Honda', 'Ford', 'Mitsubishi', 'MG','Toyota','Suzuki']
car_types = ['Pickup', 'Van/MPV', 'Sedan', 'SUV']
Brand = st.sidebar.selectbox("Brand", brands)
year = st.sidebar.slider("Year", min_value=2020, max_value=2023, value=2021)
price = st.sidebar.slider("Price (in ฿)", min_value=0, max_value=1000000, value=200000)
car_type = st.sidebar.selectbox("Type", car_types)

# สร้าง DataFrame สำหรับฟีเจอร์ที่ป้อนเข้ามา
input_data = pd.DataFrame({
    'Year': [year],
    'Brand': [Brand],
    'Type': [car_type],
    'Price': [price],
})

# สร้างข้อมูลสุ่มสำหรับกราฟ
random_data = {
    'Type': np.random.choice(car_types, size=100),
    'Price': np.random.randint(200000, 800000, size=100)
}

df = pd.DataFrame(random_data)

# โหลดโมเดล
model_path = r"C:\65024311\model.pkl"
with open(model_path, 'rb') as file:
    model = joblib.load(file)

# เข้ารหัสฟีเจอร์ Brand และ Type
label_encoder_brand = LabelEncoder()
label_encoder_type = LabelEncoder()

# ฟิต LabelEncoder ตามข้อมูลที่มี
input_data['Brand_encoded'] = label_encoder_brand.fit_transform(input_data['Brand'])
input_data['Type_encoded'] = label_encoder_type.fit_transform(input_data['Type'])

# เตรียมข้อมูลสำหรับการทำนาย
X = input_data[['Year', 'Brand_encoded', 'Type_encoded', 'Price']]

# การทำนาย
if st.sidebar.button('Predict'):
    prediction = model.predict(X)
    st.subheader("Prediction Result")
    st.write(f"The car is classified in group: **{prediction[0]}**")

# แสดงกราฟเพื่อการมองเห็นข้อมูลที่ดีขึ้น
st.subheader("Feature Distribution")

# สร้าง Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Type', y='Price', data=df)
plt.title('Price Distribution by Vehicle Type')
plt.xlabel('Vehicle Type')
plt.ylabel('Price (Baht)')
plt.xticks(rotation=45)

# แสดงกราฟใน Streamlit
st.pyplot(plt)

# ข้อมูลเพิ่มเติม
st.markdown("This application predicts the price of a used car based on its make, year, and price.")
