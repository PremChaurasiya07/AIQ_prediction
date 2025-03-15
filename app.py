import tkinter as tk
from tkinter import messagebox
import pymysql
import pickle
import numpy as np


conn = pymysql.connect(host='localhost', user='root', password='yourpassword')
cursor = conn.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS air_quality")
    cursor.execute("USE air_quality")

  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS air_quality_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            City INT,  
            PM2_5 FLOAT,
            PM10 FLOAT,
            O3 FLOAT,
            NO2 FLOAT,
            SO2 FLOAT,
            CO FLOAT,
            Latitude FLOAT,
            Longitude FLOAT,
            
        )
    """)

    conn.commit()
    print(" Database and table setup completed successfully.")
except Exception as e:
    conn.rollback()
    print(" Error:", e)


with open('AIQ.pkl', 'rb') as file:
    model = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

print("Available Cities:", label_encoder.classes_) 

with open('city_mapping.pkl', 'rb') as file:
    city_mapping = pickle.load(file)

def find_closest_city(city_name):
    city_name_lower = city_name.lower()
    for city in city_mapping.keys():
        if any(word in city.lower() for word in city_name_lower.split()):
            return city_mapping[city] 
    return None 

def submit_data():
    try:
        city_name = city_entry.get().strip()
        city_encoded = find_closest_city(city_name)
     
        if city_encoded is None:
            messagebox.showerror("Error", f"Invalid City Name! Available: {list(city_mapping.keys())}")
            return
        
        pm25 = float(pm25_entry.get())
        pm10 = float(pm10_entry.get())
        o3 = float(o3_entry.get())
        no2 = float(no2_entry.get())
        so2 = float(so2_entry.get())
        co = float(co_entry.get())
        latitude = float(latitude_entry.get())
        longitude = float(longitude_entry.get())
       
        
       
        query = """INSERT INTO air_quality_data (City, PM2_5, PM10, O3, NO2, SO2, CO, Latitude, Longitude) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (city_encoded, pm25, pm10, o3, no2, so2, co, latitude, longitude)
        cursor.execute(query, values)
        conn.commit()
        
        input_data = np.array([[city_encoded, pm25, pm10, o3, no2, so2, co, latitude, longitude]])
        prediction = model.predict(input_data)
        messagebox.showinfo("Prediction", f" Predicted Air Quality Index: {prediction[0]}")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Air Quality Prediction")
root.geometry("400x500")
root.configure(bg="#f0f0f0") 


frame = tk.Frame(root, padx=20, pady=20, bg="white", relief=tk.RIDGE, borderwidth=2)
frame.pack(pady=20)


title_label = tk.Label(frame, text="Air Quality Prediction", font=("Arial", 14, "bold"), fg="black", bg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=10)


def create_entry(label, row):
    lbl = tk.Label(frame, text=label, font=("Arial", 10, "bold"), bg="white")
    lbl.grid(row=row, column=0, pady=5)
    entry = tk.Entry(frame, width=25, font=("Arial", 10))
    entry.grid(row=row, column=1, pady=5)
    return entry

city_entry = create_entry("City:", 1)
pm25_entry = create_entry("PM2.5:", 2)
pm10_entry = create_entry("PM10:", 3)
o3_entry = create_entry("O3:", 4)
no2_entry = create_entry("NO2:", 5)
so2_entry = create_entry("SO2:", 6)
co_entry = create_entry("CO:", 7)
latitude_entry = create_entry("Latitude:", 8)
longitude_entry = create_entry("Longitude:", 9)


submit_button = tk.Button(frame, text="Submit", font=("Arial", 12, "bold"), bg="#007BFF", fg="white", padx=10, pady=5, command=submit_data)
submit_button.grid(row=10, column=0, columnspan=2, pady=15)


root.mainloop()