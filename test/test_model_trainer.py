import numpy
from unittest.mock import patch
from src.exception.exception import customexception
import pytest
from src.data.model_trainer import *  # Importing all from the source module, ModelTrainer
def test_dummy():
	assert True
# Test generated using Keploy
def test_initate_model_training_empty_arrays():
    # Create empty train and test arrays
    train_array = np.empty((0, 0))
    test_array = np.empty((0, 0))
    # Initialize ModelTrainer
    trainer = ModelTrainer()
    # Mock evaluate_model and save_object
    with patch('src.utils.utils.evaluate_model') as mock_evaluate_model, \
         patch('src.utils.utils.save_object') as mock_save_object:
        # Assert that customexception is raised
        with pytest.raises(customexception):
            trainer.initate_model_training(train_array, test_array)
# Test generated using Keploy
def test_initate_model_training_mismatched_dimensions():
    # Create train and test arrays with mismatched dimensions
    train_array = np.array([[1, 2, 3], [4, 5, 6]])
    test_array = np.array([[7, 8], [9, 10]])
    # Initialize ModelTrainer
    trainer = ModelTrainer()
    # Assert that customexception is raised
    with pytest.raises(customexception):
        trainer.initate_model_training(train_array, test_array)