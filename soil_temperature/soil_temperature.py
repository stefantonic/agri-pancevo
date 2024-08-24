import csv
import pyexcel as pe

# Paths
input_ods_file = '/home/stefan/Desktop/atlas-klime-pa/dataset/dataset.ods'
output_csv_file = '/home/stefan/Desktop/atlas-klime-pa/soil_temperature/soil_temperature.csv'

# Load the ODS file
sheet = pe.get_sheet(file_name=input_ods_file)

# Define the range to extract
start_data_row = 1730  # 0-based index for row 1731
end_data_row = 2702    # 0-based index for row 2703
col_for_date_time = 0  # 0-based index for column A
cols_for_data = [30, 31, 32]  # 0-based index for columns AE, AF, AG

# Read header row from A2 and AE2:AG2
header_date_time = sheet.cell_value(1, col_for_date_time)  # Value at A2
header_data = [sheet.cell_value(1, col) for col in cols_for_data]  # Values at AE2:AG2

# Prepare to write to CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Date/Time', 'avg', 'max', 'min'])

    # Iterate over rows in the specified range
    for i in range(start_data_row, end_data_row + 1):
        date_time_value = sheet.cell_value(i, col_for_date_time)
        avg_value = sheet.cell_value(i, cols_for_data[0])
        max_value = sheet.cell_value(i, cols_for_data[1])
        min_value = sheet.cell_value(i, cols_for_data[2])
        writer.writerow([date_time_value, avg_value, max_value, min_value])

print(f"Data extracted and saved to {output_csv_file}")
