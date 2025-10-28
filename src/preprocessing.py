import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer

def load_data(path):
    df = pd.read_csv(path)
    if 'Id' in df.columns:
        df.drop(columns=['Id'], inplace=True)
    return df

def clean_data(df):
    df.fillna(df.median(numeric_only=True), inplace=True)
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    return df

def impute_knn(df):
    num_df = df.select_dtypes(include='number')
    imputer = KNNImputer(n_neighbors=5)
    df[num_df.columns] = imputer.fit_transform(num_df)
    return df

