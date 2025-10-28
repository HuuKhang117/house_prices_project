import matplotlib.pyplot as plt
import seaborn as sns

def plot_model_results(results_df):
    results_df.sort_values(by="RMSE", inplace=True)
    sns.barplot(x=results_df.index, y=results_df["RMSE"])
    plt.title("So sánh sai số RMSE giữa các mô hình")
    plt.show()

def get_best_model(results_df):
    return results_df["RMSE"].idxmin()

