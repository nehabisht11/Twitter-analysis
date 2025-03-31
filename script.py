import os
import pandas as pd

def convert_xlsx_to_csv(input_folder, output_folder):
    """Convert all XLSX files in a folder to CSV files."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in os.listdir(input_folder):
        if file.endswith(".xlsx"):
            file_path = os.path.join(input_folder, file)
            df = pd.read_excel(file_path)
            csv_filename = os.path.splitext(file)[0] + ".csv"
            csv_path = os.path.join(output_folder, csv_filename)
            df.to_csv(csv_path, index=False)
            print(f"Converted: {file} -> {csv_filename}")

if __name__ == "_main_":
    input_folder = "C:/Users/NEHA/OneDrive/Desktop/NullClass Asingment"  # Change to your actual input folder
    output_folder = "C:/Users/NEHA/OneDrive/Desktop/NullClass Asingment/output_csv"  # Change to your actual output folder
    convert_xlsx_to_csv(input_folder, output_folder)
