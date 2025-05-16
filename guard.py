import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_model():
    df = pd.read_csv("data/creditcard.csv")
    df['Amount'] = StandardScaler().fit_transform(df[['Amount']])
    df = df.drop(['Time'], axis=1)
    X = df.drop('Class', axis=1)
    y = df['Class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

    rf = RandomForestClassifier(n_estimators=100, class_weight='balanced')
    rf.fit(X_train, y_train)
    joblib.dump((rf, X.columns.tolist()), "app/fraud_model.pkl")

    return rf

def load_model():
    if not os.path.exists("app/fraud_model.pkl"):
        return train_model()
    import joblib
    return joblib.load("app/fraud_model.pkl")
