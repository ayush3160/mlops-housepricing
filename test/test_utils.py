import os
import pytest
from src.utils.utils import *  # Importing all from the source module, evaluate_model, load_object, save_object
def test_dummy():
	assert True
# Test generated using Keploy
def test_save_object_happy_path(tmp_path):
    # Arrange
    from src.utils.utils import save_object
    test_object = {"key": "value"}
    file_path = tmp_path / "test.pkl"
    # Act
    save_object(file_path, test_object)
    # Assert
    assert file_path.exists(), "File was not created"
# Test generated using Keploy
def test_load_object_happy_path(tmp_path):
    # Arrange
    from src.utils.utils import save_object, load_object
    test_object = {"key": "value"}
    file_path = tmp_path / "test.pkl"
    save_object(file_path, test_object)
    # Act
    loaded_object = load_object(file_path)
    # Assert
    assert loaded_object == test_object, "Loaded object does not match the saved object"
# Test generated using Keploy
def test_load_object_file_not_found():
    # Arrange
    from src.utils.utils import load_object
    invalid_file_path = "/non_existent_file.pkl"
    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        load_object(invalid_file_path)
    assert "No such file or directory" in str(exc_info.value), "Expected file not found error not raised"
# Test generated using Keploy
def test_save_object_directory_path(tmp_path):
    # Arrange
    from src.utils.utils import save_object
    directory_path = tmp_path / "test_dir"
    directory_path.mkdir()  # Create a directory instead of a file
    test_object = {"key": "value"}
    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        save_object(directory_path, test_object)
    assert "Is a directory" in str(exc_info.value), "Expected directory path error not raised"
# Test generated using Keploy
def test_evaluate_model_empty_models():
    # Arrange
    from src.utils.utils import evaluate_model
    import numpy as np
    X_train = np.array([[1], [2], [3]])
    y_train = np.array([1, 2, 3])
    X_test = np.array([[4], [5]])
    y_test = np.array([4, 5])
    models = {}  # Empty dictionary
    # Act
    report = evaluate_model(X_train, y_train, X_test, y_test, models)
    # Assert
    assert isinstance(report, dict), "Report is not a dictionary"
    assert len(report) == 0, "Report should be empty for no models"