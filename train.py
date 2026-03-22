import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from data_ingestion import load_data
from preprocessing import preprocess
import joblib

def train():
    df = load_data("data/sample.csv")
    X_train, X_test, y_train, y_test = preprocess(df)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    mlflow.set_experiment("mlops_project")
    with mlflow.start_run():
        mlflow.log_param("model", "RandomForest")
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")
    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()
