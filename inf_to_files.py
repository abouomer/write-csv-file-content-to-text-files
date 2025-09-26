
import csv
import os

# Path to your CSV file
csv_path = 'my_data.csv'

# Create a directory to store the text files
output_dir = 'output_txt_files'
os.makedirs(output_dir, exist_ok=True)

# Read CSV and create text files
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if len(row) < 4:
            print(f"Row {i+1} doesn't have enough columns. Skipping...")
            continue
        c_row=[item.replace('/','')for item in row]
        # Extract file content and name components
        text_content = row[0]
        file_name = f"{c_row[0]}_{c_row[1]}_{c_row[2]}.txt"
        file_path = os.path.join(output_dir, file_name)
        print(file_name,file_path)
        # Write content to text file
        with open(file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)

print("✅ Done! All text files have been generated.")



