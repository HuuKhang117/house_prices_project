import matplotlib.pyplot as plt
import seaborn as sns

# =======================================
# Hàm: plot_model_results(results_df)
# ---------------------------------------
# Mục đích:
#   - Trực quan hóa kết quả đánh giá các mô hình (RMSE).
#   - Giúp dễ dàng so sánh mô hình nào hoạt động tốt nhất.
#
# Tham số:
#   results_df (DataFrame): bảng kết quả từ train_models()
#       có cột "RMSE" và "R²" với chỉ số của từng mô hình.
# =======================================
def plot_model_results(results_df):
    # Sắp xếp mô hình theo RMSE (từ nhỏ → lớn, mô hình tốt nhất ở trên)
    results_df.sort_values(by="RMSE", inplace=True)
    
    # Vẽ biểu đồ cột thể hiện RMSE giữa các mô hình
    sns.barplot(x=results_df.index, y=results_df["RMSE"], palette="crest")
    plt.title("So sánh sai số RMSE giữa các mô hình")
    plt.xlabel("Tên mô hình")
    plt.ylabel("RMSE (Càng thấp càng tốt)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()


# =======================================
# Hàm: get_best_model(results_df)
# ---------------------------------------
# Mục đích:
#   - Xác định mô hình tốt nhất dựa trên chỉ số RMSE nhỏ nhất.
#
# Tham số:
#   results_df (DataFrame): bảng kết quả huấn luyện mô hình.
#
# Trả về:
#   str: tên mô hình có RMSE nhỏ nhất (tức là mô hình tốt nhất).
# =======================================
def get_best_model(results_df):
    return results_df["RMSE"].idxmin()
