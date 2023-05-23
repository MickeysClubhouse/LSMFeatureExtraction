import json

file_path = "data/train_plans_serial.json"  # 替换为你的文件路径

scan_rows = []

with open(file_path, "r") as file:
    data = json.load(file)
    for item in data:
        plan = item["plan"]
        scan_row = [row for row in plan if "scan_detail" in row][0]
        scan_rows.append(scan_row)

for scan_row in scan_rows:
    print(scan_row)
