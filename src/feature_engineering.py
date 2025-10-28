# =======================================
# Hàm: add_features(df)
# ---------------------------------------
# Mục đích:
#   - Tạo ra các **biến đặc trưng mới (feature engineering)** từ dữ liệu gốc.
#   - Các đặc trưng này giúp mô hình học được thêm thông tin tiềm ẩn,
#     có thể cải thiện độ chính xác khi dự đoán giá nhà.
#
# Tham số:
#   df (DataFrame): dữ liệu gốc đã được làm sạch.
#
# Trả về:
#   DataFrame: dữ liệu có thêm các cột đặc trưng mới.
# =======================================
def add_features(df):
    # Tổng diện tích sàn (bao gồm tầng hầm + tầng 1 + tầng 2)
    df["TotalSF"] = df["TotalBsmtSF"] + df["1stFlrSF"] + df["2ndFlrSF"]

    # Tuổi của căn nhà tại thời điểm bán (năm bán - năm xây dựng)
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]

    # Tổng diện tích các khu vực ngoài trời (sân, hiên, hồ bơi, v.v.)
    df["Outdoors"] = (
        df["WoodDeckSF"] +
        df["OpenPorchSF"] +
        df["EnclosedPorch"] +
        df["ScreenPorch"] +
        df["PoolArea"]
    )

    return df
