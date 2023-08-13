file_path = 'normalize_date.txt' 

# Mở tệp tin để đọc
with open(file_path, 'r') as file:
    # Đọc nội dung từ tệp tin
    data = file.read()

# Chia dữ liệu thành các dòng
lines = data.split('\n')

# Tạo danh sách để lưu trữ dữ liệu
data_list = []

# Xử lý từng dòng dữ liệu
for line in lines:
    # Chia dòng thành các cột
    columns = line.split('\t' )

    # Kiểm tra xem dòng có đủ cột hay không
    if len(columns) == 2:
        # Lấy giá trị ngày và giá trị số liệu từ các cột
        date = columns[0]
        value = int(columns[1])

        # Tạo một bộ dữ liệu (date, value) và thêm vào danh sách
        data_list.append((date, value))

# In danh sách dữ liệu
for date, value in data_list:
    print(f"Date: {date}, Value: {value}")