# Air Quality Prediction using Tkinter & Machine Learning

## Overview

This project is a **Tkinter-based GUI application** that predicts the **Air Quality Index (AQI)** using a **trained machine learning model**. Users can input air quality parameters, and the system will predict AQI based on the provided data.

## Features

✅ User-friendly GUI built with Tkinter\
✅ Takes air quality parameters as input\
✅ Predicts **Air Quality Index (AQI)** using a trained model\
✅ Stores data in a **MySQL database**\
✅ Provides error handling and validation

## Technologies Used

- **Python** (Tkinter for GUI, NumPy for data handling, Pickle for model loading)
- **MySQL** (Database for storing air quality data)
- **Machine Learning Model** (Pre-trained model using Pickle)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/air-quality-prediction.git
cd air-quality-prediction
```

### 2. Install Dependencies

Ensure you have Python installed. Install required dependencies:

```bash
pip install pymysql numpy tkinter
```

### 3. Set Up MySQL Database

1. Open MySQL and create a database:

```sql
CREATE DATABASE air_quality;
USE air_quality;
```

2. The program will automatically create the required table.
3. Update the MySQL connection details in the script:

```python
conn = pymysql.connect(host='localhost', user='root', password='yourpassword')
```

### 4. Load Machine Learning Model

Ensure the required **Pickle** model files are in the project directory:

- `AIQ.pkl` (Trained Model)
- `label_encoder.pkl` (Encoding for cities)
- `city_mapping.pkl` (Mapping of city names to numerical values)

## Usage

Run the Python script:

```bash
python air_quality_gui.py
```

1. Enter air quality parameters such as **PM2.5, PM10, O3, NO2, SO2, CO, Latitude, Longitude**.
2. Click **Submit** to get the predicted AQI.
3. The application will also store the input data in the **MySQL database**.

## Example Input & Output

| City      | PM2.5 | PM10 | O3 | NO2 | SO2 | CO | Latitude | Longitude |
| --------- | ----- | ---- | -- | --- | --- | -- | -------- | --------- |
| Gorakhpur | 85    | 78   | 2  | 85  | 45  | 23 | 12       | 78        |

**Predicted AQI:** `95.01`

## Screenshots
![image](https://github.com/user-attachments/assets/8de5cde4-2c82-4898-ae40-423935ac4463) </br>
![image](https://github.com/user-attachments/assets/dfbd35f6-1a38-4569-873a-496ad2433e4d)



## License

This project is **open-source** under the MIT License.

## Contributing

Feel free to contribute! Fork the repo and submit pull requests.

