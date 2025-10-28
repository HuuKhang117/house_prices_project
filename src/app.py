# =======================================
# Import các module cần thiết từ các file đã tạo trước
# ---------------------------------------
# Mỗi file đảm nhận một nhiệm vụ riêng:
#   - preprocessing.py: tải và làm sạch dữ liệu
#   - feature_engineering.py: tạo đặc trưng mới
#   - model_training.py: huấn luyện mô hình
#   - evaluation.py: trực quan và chọn mô hình tốt nhất
# =======================================
from preprocessing import load_data, clean_data, impute_knn
from feature_engineering import add_features
from model_training import train_models
from evaluation import plot_model_results, get_best_model

# =======================================
# BƯỚC 1: Nạp dữ liệu gốc
# ---------------------------------------
# Đường dẫn có thể thay đổi tùy nơi bạn lưu file CSV.
# Nếu dùng Google Colab: dùng upload trực tiếp từ máy (files.upload()).
# =======================================
df = load_data("data/train.csv")

# =======================================
# BƯỚC 2: Tiền xử lý dữ liệu
# ---------------------------------------
# - Làm sạch giá trị thiếu và mã hóa biến phân loại.
# - Dùng KNN Imputer để điền thêm giá trị thiếu còn lại.
# =======================================
df = clean_data(df)
df = impute_knn(df)

# =======================================
# BƯỚC 3: Tạo đặc trưng mới (Feature Engineering)
# ---------------------------------------
# Thêm các biến mới như:
#   - TotalSF: tổng diện tích sàn
#   - HouseAge: tuổi nhà
#   - Outdoors: diện tích khu vực ngoài trời
# =======================================
df = add_features(df)

# =======================================
# BƯỚC 4: Chuẩn bị dữ liệu huấn luyện
# ---------------------------------------
# Biến mục tiêu: 'SalePrice'
# Đầu vào X: tất cả cột còn lại
# =======================================
X = df.drop(columns=['SalePrice'])
y = df['SalePrice']

# =======================================
# BƯỚC 5: Huấn luyện và đánh giá mô hình
# ---------------------------------------
# Gọi hàm train_models() để huấn luyện:
#   - Linear Regression
#   - Random Forest
#   - XGBoost
# Trả về bảng kết quả RMSE và R²
# =======================================
results = train_models(X, y)

# =======================================
# BƯỚC 6: Hiển thị kết quả mô hình
# ---------------------------------------
# In bảng kết quả, vẽ biểu đồ so sánh và chọn mô hình tốt nhất.
# =======================================
print("Kết quả đánh giá mô hình:\n")
print(results)
plot_model_results(results)
print("\n✅ Mô hình tốt nhất là:", get_best_model(results))
