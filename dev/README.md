### CHUẨN BỊ

- Python version 3.11
- Jupyter version lastest
- Docker lastest

### KHỞI TẠO WEBSERVER

- Chạy lệnh docker

```bash
docker compose up
```

- Vào đường dẫn http://127.0.0.1/80

### CHẠY VÀ TÌM NHỮNG NGÀY BẤT THƯỜNG

1. Chuyển các dữ liệu trong file access log trong cùng một chuẩn

```bash
py format.py
```

2. Nhận biết những ngày bất thường

```bash
py index.py
```
