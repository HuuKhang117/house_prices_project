import seaborn as sns
import matplotlib.pyplot as plt

def plot_price_distribution(df):
    sns.histplot(df['SalePrice'], kde=True)
    plt.title("Phân phối giá nhà")
    plt.show()

def plot_top_correlations(df):
    corr = df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False)
    top = corr.head(6).index[1:]
    for f in top:
        sns.scatterplot(x=df[f], y=df['SalePrice'])
        plt.title(f"Tương quan {f} - SalePrice")
        plt.show()

