from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

# =======================================
# Hàm: train_models(X, y)
# ---------------------------------------
# Mục đích:
#   - Chia dữ liệu thành tập huấn luyện và kiểm tra.
#   - Huấn luyện nhiều mô hình hồi quy khác nhau.
#   - So sánh hiệu suất dựa trên chỉ số RMSE và R².
#
# Tham số:
#   X (DataFrame hoặc ndarray): dữ liệu đầu vào (feature).
#   y (Series hoặc ndarray): biến mục tiêu (SalePrice).
#
# Trả về:
#   DataFrame chứa RMSE và R² của từng mô hình.
# =======================================
def train_models(X, y):
    # -----------------------------
    # Bước 1: Chia dữ liệu train/test (80% train - 20% test)
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -----------------------------
    # Bước 2: Khởi tạo các mô hình hồi quy
    # -----------------------------
    models = {
        "Linear Regression": LinearRegression(),                  # Hồi quy tuyến tính
        "Random Forest": RandomForestRegressor(random_state=42),   # Rừng ngẫu nhiên (ensemble)
        "XGBoost": XGBRegressor(random_state=42)                   # Gradient boosting nâng cao
    }

    # -----------------------------
    # Bước 3: Huấn luyện và đánh giá từng mô hình
    # -----------------------------
    results = {}

    for name, model in models.items():
        # Huấn luyện mô hình
        model.fit(X_train, y_train)

        # Dự đoán trên tập test
        pred = model.predict(X_test)

        # Tính RMSE (Root Mean Squared Error) → càng nhỏ càng tốt
        rmse = np.sqrt(mean_squared_error(y_test, pred))

        # Tính R² (hệ số xác định) → càng gần 1 càng tốt
        r2 = r2_score(y_test, pred)

        # Lưu kết quả
        results[name] = [rmse, r2]

    # -----------------------------
    # Bước 4: Trả về bảng tổng hợp kết quả
    # -----------------------------
    return pd.DataFrame(results, index=["RMSE", "R²"]).T
