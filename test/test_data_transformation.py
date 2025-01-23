import pandas
from src.exception.exception import customexception
import pytest
from src.data.data_transformation import *  # Importing all from the source module, DataTransformation
def test_dummy():
	assert True
# Test generated using Keploy
def test_initialize_data_transformation_missing_train_file(tmp_path):
    # Arrange
    test_data = {
        "Feature1": [4.0, 5.0],
        "Feature2": ["D", "E"],
        "Price": [400, 500]
    }
    test_path = tmp_path / "test.csv"
    pd.DataFrame(test_data).to_csv(test_path, index=False)
    data_transformation = DataTransformation()
    # Act & Assert
    with pytest.raises(customexception):
        data_transformation.initialize_data_transformation("missing_train.csv", test_path)
# Test generated using Keploy
def test_initialize_data_transformation_missing_target_column(tmp_path):
    # Arrange
    train_data = {
        "Feature1": [1.0, 2.0, 3.0],
        "Feature2": ["A", "B", "C"]
    }
    test_data = {
        "Feature1": [4.0, 5.0],
        "Feature2": ["D", "E"],
        "Price": [400, 500]
    }
    train_path = tmp_path / "train.csv"
    test_path = tmp_path / "test.csv"
    pd.DataFrame(train_data).to_csv(train_path, index=False)
    pd.DataFrame(test_data).to_csv(test_path, index=False)
    data_transformation = DataTransformation()
    # Act & Assert
    with pytest.raises(customexception):
        data_transformation.initialize_data_transformation(train_path, test_path)
# Test generated using Keploy
def test_initialize_data_transformation_missing_values(tmp_path):
    # Arrange
    train_data = {
        "Feature1": [1.0, None, 3.0],
        "Feature2": ["A", "B", None],
        "Price": [100, 200, None]
    }
    test_data = {
        "Feature1": [4.0, 5.0],
        "Feature2": ["D", "E"],
        "Price": [400, 500]
    }
    train_path = tmp_path / "train.csv"
    test_path = tmp_path / "test.csv"
    pd.DataFrame(train_data).to_csv(train_path, index=False)
    pd.DataFrame(test_data).to_csv(test_path, index=False)
    data_transformation = DataTransformation()
    # Act & Assert
    with pytest.raises(customexception):
        data_transformation.initialize_data_transformation(train_path, test_path)