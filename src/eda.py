import seaborn as sns
import matplotlib.pyplot as plt

# =======================================
# Hàm 1: plot_price_distribution(df)
# ---------------------------------------
# Mục đích:
#   - Hiển thị biểu đồ phân phối (histogram) của biến mục tiêu 'SalePrice'
#   - Giúp hiểu được hình dạng phân phối giá nhà (chuẩn, lệch trái, lệch phải,...)
# Tham số:
#   df (DataFrame): dữ liệu chứa cột 'SalePrice'
# =======================================
def plot_price_distribution(df):
    # Vẽ biểu đồ histogram có đường mật độ KDE (đường cong phân phối)
    sns.histplot(df['SalePrice'], kde=True, color='skyblue', edgecolor='black')
    plt.title("Phân phối giá nhà (SalePrice)")
    plt.xlabel("Giá nhà")
    plt.ylabel("Tần suất xuất hiện")
    plt.show()


# =======================================
# Hàm 2: plot_top_correlations(df)
# ---------------------------------------
# Mục đích:
#   - Xác định các biến có tương quan cao nhất với 'SalePrice'
#   - Vẽ biểu đồ scatter để quan sát mối quan hệ giữa các biến này với giá nhà
# Tham số:
#   df (DataFrame): dữ liệu chứa các biến số và 'SalePrice'
# =======================================
def plot_top_correlations(df):
    # Tính hệ số tương quan giữa các cột dạng số với 'SalePrice'
    corr = df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False)
    
    # Lấy ra 5 biến có tương quan cao nhất (bỏ cột 'SalePrice' chính nó)
    top = corr.head(6).index[1:]
    
    # Lặp qua từng biến và vẽ biểu đồ scatter
    for f in top:
        sns.scatterplot(x=df[f], y=df['SalePrice'], color='orange')
        plt.title(f"Tương quan giữa {f}

