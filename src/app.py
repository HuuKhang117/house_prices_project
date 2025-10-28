from preprocessing import load_data, clean_data, impute_knn
from feature_engineering import add_features
from model_training import train_models
from evaluation import plot_model_results, get_best_model

df = load_data("data/train.csv")
df = clean_data(df)
df = impute_knn(df)
df = add_features(df)

X = df.drop(columns=['SalePrice'])
y = df['SalePrice']

results = train_models(X, y)
print(results)
plot_model_results(results)
print(" Mô hình tốt nhất:", get_best_model(results))
