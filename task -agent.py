import os
import csv
from datetime import datetime

INPUT_FOLDER = "input"
REPORT_FOLDER = "reports"

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

print("DESKTOP TASK AGENT STARTED")

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".csv"):
        path = os.path.join(INPUT_FOLDER, filename)

        with open(path, "r", encoding="utf-8") as file:
            data = list(csv.reader(file))

        report = os.path.join(
            REPORT_FOLDER,
            filename.replace(".csv", "_report.txt")
        )

        with open(report, "w", encoding="utf-8") as output:
            output.write("AUTOMATION REPORT\n")
            output.write(f"File: {filename}\n")
            output.write(f"Rows: {len(data)}\n")
            output.write(f"Date: {datetime.now()}\n")

        print("Processed:", filename)

print("TASK AGENT FINISHED")
