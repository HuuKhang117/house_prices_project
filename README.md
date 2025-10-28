# house_prices_project
Dự án dự đoán giá nhà bằng kỹ thuật hồi quy nâng cao
#  Hệ Thống Dự Đoán Giá Nhà

Hệ thống web dự đoán giá nhà bằng kỹ thuật hồi quy nâng cao.

##  Tính năng

-  **Dự đoán giá nhà đơn lẻ**: Nhập thông tin và xem kết quả ngay lập tức
-  **Phân tích dữ liệu hàng loạt**: Tải file CSV/Excel để phân tích
-  **Biểu đồ trực quan**: 4 loại biểu đồ phân tích tự động
-  **Giao diện hiện đại**: Gradient design, responsive, dễ sử dụng
-  **Dữ liệu mẫu**: Sử dụng dữ liệu mẫu có sẵn để demo

##  Cài đặt và Chạy

### Cách 1: Cài đặt tự động
```bash
pip install -r requirements.txt
python src/app.py
```

### Cách 2: Cài đặt thủ công
```bash
pip install flask pandas numpy scikit-learn plotly werkzeug openpyxl
python src/app.py
```

**Hoặc chạy file batch:**
```bash
.\run_app.bat
```

Sau đó mở trình duyệt: **http://localhost:5000**

## Hướng dẫn sử dụng

### 1. Dự đoán đơn lẻ
1. Nhập thông tin nhà:
   - Diện tích (m²)
   - Số phòng ngủ
   - Số phòng tắm
   - Tuổi nhà (năm)
2. Nhấn "Dự Đoán Giá"
3. Xem kết quả

### 2. Tải file phân tích
1. Click vào vùng "Tải lên file dữ liệu"
2. Chọn file CSV có các cột: `area, bedrooms, bathrooms, age`
3. Xem biểu đồ và bảng kết quả

### 3. Dữ liệu mẫu
1. Nhấn "Sử dụng dữ liệu mẫu"
2. Xem 100 mẫu dữ liệu với biểu đồ

## Biểu đồ phân tích

- **Phân phối giá**: So sánh giá thực tế và dự đoán
- **Diện tích vs Giá**: Mối quan hệ giữa diện tích và giá
- **Giá theo phòng ngủ**: Giá trung bình theo số phòng ngủ
- **Tương quan đặc trưng**: Mức độ ảnh hưởng của các yếu tố
## Model

- **Algorithm**: Linear Regression
- **Features**: Diện tích, Phòng ngủ, Phòng tắm, Tuổi nhà
- **Output**: Giá nhà (triệu VNĐ)
- **Training**: Tự động train khi lần đầu sử dụng

## Tài liệu

- `HUONG_DAN.md`: Hướng dẫn chi tiết
- `CHAY_UNG_DUNG.txt`: Cách chạy app
- `DEMO.txt`: Demo và ví dụ
- `TONG_KET.txt`: Tóm tắt dự án

## Công nghệ

**Backend**: Flask, scikit-learn, pandas, numpy, plotly, xgboost, lightgbm  
**Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, Plotly.js  
**ML Algorithms**: Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting, XGBoost, LightGBM

## Cài đặt dependencies

```bash
pip install -r requirements.txt
```

Hoặc cài từng package:
```bash
# Web framework
pip install flask werkzeug

# Data processing
pip install pandas numpy openpyxl

# Machine Learning
pip install scikit-learn xgboost lightgbm catboost

# Visualization
pip install plotly matplotlib seaborn
```

## Chạy ML Pipeline

Để chạy toàn bộ pipeline machine learning:

```bash
python src/main.py
```

Pipeline sẽ:
1. Load và xử lý dữ liệu
2. EDA (Exploratory Data Analysis)
3. Preprocessing
4. Feature Engineering
5. Train nhiều models
6. Chọn model tốt nhất
7. Lưu model và tạo submission

## Chạy Web App

```bash
python src/app.py
```

Hoặc:
```bash
.\START.bat
```

Sau đó mở: http://localhost:5000
