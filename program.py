import serial
import csv
import time

ser = serial.Serial('COM15', 9600)  

csv_file = open("balkirat2.csv", mode="w", newline="")
writer = csv.writer(csv_file)
writer.writerow(["Temperature (°C)", "Humidity (%)"])  

start_time = time.time()  
duration = 30 * 60  

try:
    while time.time() - start_time < duration:
        data = ser.readline().decode().strip()
        if "Temperature" in data and "Humidity" in data:
            values = data.replace("Temperature: ", "").replace("°C, Humidity: ", "").replace(" %", "").split(",")
            writer.writerow(values)
            print(data)
except KeyboardInterrupt:
    print("Data collection stopped manually.")
finally:
    csv_file.close()
    ser.close()
    print("CSV file saved and serial connection closed.")