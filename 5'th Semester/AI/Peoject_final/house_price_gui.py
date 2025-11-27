import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import urllib.request

print("Loading dataset and training model...")
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
urllib.request.urlretrieve(url, "house_data.csv")

df = pd.read_csv("house_data.csv")
df = df.dropna()
df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True, dtype=float)

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

print("Model trained successfully!")

root = tk.Tk()
root.title("House Price Prediction")
root.geometry("500x650")
root.configure(bg='#f0f0f0')

title_label = tk.Label(root, text="California House Price Predictor", 
                       font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#333')
title_label.pack(pady=20)

main_frame = tk.Frame(root, bg='#f0f0f0')
main_frame.pack(padx=20, pady=10)

fields = {
    'Longitude': '-122.23',
    'Latitude': '37.88',
    'House Age (years)': '41',
    'Total Rooms': '880',
    'Total Bedrooms': '129',
    'Population': '322',
    'Households': '126',
    'Median Income (x10k)': '8.3252'
}

entries = {}

for i, (label, default) in enumerate(fields.items()):
    tk.Label(main_frame, text=label + ":", font=("Arial", 11), 
             bg='#f0f0f0', anchor='w', width=20).grid(row=i, column=0, pady=8, sticky='w')
    
    entry = tk.Entry(main_frame, font=("Arial", 11), width=15)
    entry.insert(0, default)
    entry.grid(row=i, column=1, pady=8, padx=10)
    entries[label] = entry

tk.Label(main_frame, text="Ocean Proximity:", font=("Arial", 11), 
         bg='#f0f0f0', anchor='w', width=20).grid(row=len(fields), column=0, pady=8, sticky='w')

ocean_var = tk.StringVar()
ocean_dropdown = ttk.Combobox(main_frame, textvariable=ocean_var, 
                              values=['NEAR BAY', 'NEAR OCEAN', 'INLAND', 'ISLAND'], 
                              state='readonly', font=("Arial", 11), width=13)
ocean_dropdown.set('NEAR BAY')
ocean_dropdown.grid(row=len(fields), column=1, pady=8, padx=10)

result_frame = tk.Frame(root, bg='#e8f4f8', relief=tk.RAISED, borderwidth=2)
result_frame.pack(pady=20, padx=20, fill='x')

result_label = tk.Label(result_frame, text="", font=("Arial", 14, "bold"), 
                       bg='#e8f4f8', fg='#0066cc', pady=15)
result_label.pack()

def predict_price():
    try:
        custom_house = {
            'longitude': float(entries['Longitude'].get()),
            'latitude': float(entries['Latitude'].get()),
            'housing_median_age': float(entries['House Age (years)'].get()),
            'total_rooms': float(entries['Total Rooms'].get()),
            'total_bedrooms': float(entries['Total Bedrooms'].get()),
            'population': float(entries['Population'].get()),
            'households': float(entries['Households'].get()),
            'median_income': float(entries['Median Income (x10k)'].get()),
            'ocean_proximity_INLAND': 1.0 if ocean_var.get() == 'INLAND' else 0.0,
            'ocean_proximity_ISLAND': 1.0 if ocean_var.get() == 'ISLAND' else 0.0,
            'ocean_proximity_NEAR BAY': 1.0 if ocean_var.get() == 'NEAR BAY' else 0.0,
            'ocean_proximity_NEAR OCEAN': 1.0 if ocean_var.get() == 'NEAR OCEAN' else 0.0
        }
        
        custom_df = pd.DataFrame([custom_house])
        custom_df = custom_df[X.columns]
        custom_scaled = scaler.transform(custom_df)
        predicted_price = model.predict(custom_scaled)[0]
        
        result_label.config(text=f"Predicted Price: ${predicted_price:,.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values!")

predict_btn = tk.Button(root, text="PREDICT PRICE", command=predict_price,
                       font=("Arial", 12, "bold"), bg='#0066cc', fg='white',
                       padx=30, pady=10, cursor='hand2')
predict_btn.pack(pady=10)

info_label = tk.Label(root, text="Enter house features and click 'Predict Price'", 
                     font=("Arial", 9), bg='#f0f0f0', fg='#666')
info_label.pack(pady=5)

root.mainloop()
