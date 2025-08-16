import pytest
import pandas as pd
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

# Test process_data function
def test_process_data():
    """
    Test that process_data returns correct shapes and objects.
    """
    data = pd.DataFrame({
        "workclass": ["Private", "Self-emp"],
        "education": ["Bachelors", "HS-grad"],
        "marital-status": ["Never-married", "Married-civ-spouse"],
        "occupation": ["Tech-support", "Craft-repair"],
        "relationship": ["Not-in-family", "Husband"],
        "race": ["White", "Black"],
        "sex": ["Male", "Female"],
        "native-country": ["United-States", "Canada"],
        "salary": ["<=50K", ">50K"]
    })
    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)
    assert X.shape[0] == 2
    assert y.shape[0] == 2
    assert encoder is not None
    assert lb is not None

# Test train_model and inference
def test_train_and_inference():
    """
    Test that train_model trains and inference predicts.
    """
    X = [[0, 1], [1, 0]]
    y = [0, 1]
    model = train_model(X, y)
    preds = inference(model, X)
    assert len(preds) == 2

# Test compute_model_metrics
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns correct metric values.
    """
    y = [0, 1, 1, 0]
    preds = [0, 1, 0, 0]
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
