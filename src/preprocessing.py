import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer

# ==============================
# Hàm 1: load_data(path)
# ------------------------------
# Mục đích: Đọc dữ liệu từ file CSV và loại bỏ cột 'Id' (nếu có)
# Tham số:
#   path (str): đường dẫn đến file CSV (ví dụ: "data/train.csv")
# Trả về:
#   df (DataFrame): dữ liệu đã được nạp vào pandas DataFrame
# ==============================
def load_data(path):
    df = pd.read_csv(path)
    # Nếu có cột 'Id' (thường là mã định danh không dùng cho mô hình), thì xóa
    if 'Id' in df.columns:
        df.drop(columns=['Id'], inplace=True)
    return df


# ==============================
# Hàm 2: clean_data(df)
# ------------------------------
# Mục đích:
#   - Xử lý giá trị thiếu (missing values) bằng cách thay thế các giá trị số bằng median
#   - Mã hóa (encoding) các biến phân loại (categorical) sang dạng số bằng LabelEncoder
# Tham số:
#   df (DataFrame): dữ liệu đầu vào
# Trả về:
#   df (DataFrame): dữ liệu sau khi được làm sạch và mã hóa
# ==============================
def clean_data(df):
    # Điền giá trị thiếu cho các cột số bằng median của cột đó
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    # Xác định các cột phân loại (kiểu object)
    cat_cols = df.select_dtypes(include='object').columns
    
    # Mã hóa từng cột phân loại thành dạng số (Label Encoding)
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    return df


# ==============================
# Hàm 3: impute_knn(df)
# ------------------------------
# Mục đích:
#   - Sử dụng thuật toán KNN Imputer để điền giá trị thiếu
#     dựa trên độ tương đồng giữa các hàng (hàng có giá trị gần nhau)
# Tham số:
#   df (DataFrame): dữ liệu đầu vào
# Trả về:
#   df (DataFrame): dữ liệu sau khi được KNN Imputer điền giá trị thiếu
# ==============================
def impute_knn(df):
    # Lọc ra các cột dạng số (KNN chỉ hoạt động với dữ liệu số)
    num_df = df.select_dtypes(include='number')
    
    # Khởi tạo đối tượng KNNImputer với k=5 (dùng 5 hàng gần nhất)
    imputer = KNNImputer(n_neighbors=5)
    
    # Điền giá trị thiếu và gán lại vào DataFrame
    df[num_df.columns] = imputer.fit_transform(num_df)
    return df
