import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from pydispatch import dispatcher

load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')

file_path = 'normalize_date.txt' 

with open(file_path, 'r') as file:
    data = file.read()

lines = data.split('\n')

data_list = []

for line in lines:
    columns = line.split('\t' )

    if len(columns) == 2:
        date = columns[0]
        value = int(columns[1])
        data_list.append((date, value))

receiver_email = 'n19dcat016@student.ptithcm.edu.vn'


message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Báo cáo kết quả những request bất thường'
# Tạo nội dung bảng HTML
table_html = """
<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Ngày bất thường</th>
    <th style="border: 1px solid black; padding: 8px;">Số lượng request bất thường</th>
  </tr>
 </table> 
"""

new_rows = ""
col_pattern = """
    <tr>
        <td style="border: 1px solid black; padding: 8px;">{}</td>
        <td style="border: 1px solid black; padding: 8px;">{}</td>
    </tr>
    """
for date, value in data_list:
    new_row = col_pattern.format(date, value)
    new_rows += new_row

table_html = table_html.replace("</table>", new_rows + "</table>")
table_mime = MIMEText(table_html, 'html')

message.attach(table_mime)

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()

smtp_connection.login(sender_email, sender_password)

smtp_connection.sendmail(sender_email, receiver_email, message.as_string())
smtp_connection.quit()
    







