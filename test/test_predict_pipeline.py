import pytest
from src.pipeline.predict_pipeline import *  # Importing all from the source module, main, predict
def test_dummy():
	assert True
# Test generated using Keploy
import pandas as pd
from unittest.mock import MagicMock, patch
from src.pipeline.predict_pipeline import predict
def test_predict_happy_path():
    # Mock input data
    features = pd.DataFrame({
        "Avg. Area Income": [65000],
        "Avg. Area House Age": [5],
        "Avg. Area Number of Rooms": [7],
        "Avg. Area Number of Bedrooms": [4],
        "Area Population": [30000],
        "Address": ["123 Main St"]
    })
    # Mock preprocessor and model
    mock_preprocessor = MagicMock()
    mock_preprocessor.transform.return_value = "transformed_features"
    mock_model = MagicMock()
    mock_model.predict.return_value = [250000]
    with patch("src.pipeline.predict_pipeline.load_object", side_effect=[mock_preprocessor, mock_model]):
        prediction = predict(features)
    # Assertions
    mock_preprocessor.transform.assert_called_once_with(features)
    mock_model.predict.assert_called_once_with("transformed_features")
    assert prediction == [250000]
# Test generated using Keploy
import sys
import pandas as pd
from unittest.mock import patch, MagicMock
from src.pipeline.predict_pipeline import predict
def test_cli_argument_parsing():
    test_args = [
        "predict_pipeline.py",
        "--income", "65000",
        "--house_age", "5",
        "--num_rooms", "7",
        "--num_bedrooms", "4",
        "--population", "30000",
        "--address", "123 Main St"
    ]
    expected_data = pd.DataFrame({
        "Avg. Area Income": [65000.0],
        "Avg. Area House Age": [5.0],
        "Avg. Area Number of Rooms": [7.0],
        "Avg. Area Number of Bedrooms": [4.0],
        "Area Population": [30000.0],
        "Address": ["123 Main St"]
    })
    with patch.object(sys, "argv", test_args), patch("src.pipeline.predict_pipeline.predict", return_value=[250000]) as mock_predict:
        from src.pipeline.predict_pipeline import main
        main()
        mock_predict.assert_called_once()
        pd.testing.assert_frame_equal(mock_predict.call_args[0][0], expected_data)