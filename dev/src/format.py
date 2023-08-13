import json
import csv
import pandas as pd
from datetime import datetime

INPUT_FILE_PATH = '../log/access.log'
OUTPUT_FILE_PATH = '../dataset/access.csv'

CONST_INPUT_DATE = "%d/%b/%Y:%H:%M:%S %z"
CONST_OUTPUT_DATE = "%Y-%m-%dT%H:%M:%S.%fZ"

with open(INPUT_FILE_PATH, 'r') as f_log, open(OUTPUT_FILE_PATH, 'w', newline='') as f_csv:
    writer = csv.writer(f_csv)
    for line in f_log:
        log_dict = json.loads(line)

        keys_to_select = ['time_local','remote_addr', 'http_user_agent']

        selected_values = {key: log_dict.get(key) for key in keys_to_select}
        
        old_format_date = datetime.strptime(selected_values['time_local'],CONST_INPUT_DATE)
        new_format_date = datetime.strftime(old_format_date, CONST_OUTPUT_DATE)
        selected_values['time_local'] = new_format_date

        writer.writerow(selected_values.values())