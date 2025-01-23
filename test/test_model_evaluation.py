import numpy
import pytest
from src.data.model_evaluation import *  # Importing all from the source module
def test_dummy():
	assert True
# Test generated using Keploy
def test_eval_metrics_valid_inputs():
    # Arrange
    model_eval = ModelEvaluation()
    actual = [3.0, -0.5, 2.0, 7.0]
    pred = [2.5, 0.0, 2.0, 8.0]
    # Act
    rmse, mae, r2 = model_eval.eval_metrics(actual, pred)
    # Assert
    assert round(rmse, 2) == 0.61, "RMSE calculation is incorrect"
    assert round(mae, 2) == 0.5, "MAE calculation is incorrect"
    assert round(r2, 2) == 0.95, "R2 score calculation is incorrect"
# Test generated using Keploy
def test_eval_metrics_mismatched_lengths():
    # Arrange
    model_eval = ModelEvaluation()
    actual = [3.0, -0.5, 2.0]
    pred = [2.5, 0.0, 2.0, 8.0]
    # Act & Assert
    with pytest.raises(ValueError, match="Found input variables with inconsistent numbers of samples"):
        model_eval.eval_metrics(actual, pred)