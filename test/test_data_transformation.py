# import pandas
# from src.exception.exception import customexception
# import pytest
# from src.data.data_transformation import *  # Importing all from the source module, DataTransformation
# def test_dummy():
# 	assert True
# # Test generated using Keploy
# def test_initialize_data_transformation_invalid_train_path(mocker):
#     # Mocking dependencies
#     mocker.patch("pandas.read_csv", side_effect=FileNotFoundError("File not found"))
#     # Initialize the DataTransformation object
#     data_transformation = DataTransformation()
#     # Call the method and expect an exception
#     with pytest.raises(customexception) as exc_info:
#         data_transformation.initialize_data_transformation("invalid_train.csv", "test.csv")
#     # Assertions
#     assert "File not found" in str(exc_info.value)
# # Test generated using Keploy
# def test_initialize_data_transformation_invalid_test_path(mocker):
#     # Mocking dependencies
#     mocker.patch("pandas.read_csv", side_effect=[
#         pd.DataFrame({"Feature1": [1, 2], "Feature2": ["A", "B"], "Price": [100, 200]}),
#         FileNotFoundError("File not found")
#     ])
#     # Initialize the DataTransformation object
#     data_transformation = DataTransformation()
#     # Call the method and expect an exception
#     with pytest.raises(customexception) as exc_info:
#         data_transformation.initialize_data_transformation("train.csv", "invalid_test.csv")
#     # Assertions
#     assert "File not found" in str(exc_info.value)
# # Test generated using Keploy
# def test_initialize_data_transformation_missing_target_column_train(mocker):
#     # Mocking dependencies
#     mocker.patch("pandas.read_csv", side_effect=[
#         pd.DataFrame({"Feature1": [1, 2], "Feature2": ["A", "B"]}),  # Missing 'Price' column
#         pd.DataFrame({"Feature1": [3, 4], "Feature2": ["C", "D"], "Price": [300, 400]})
#     ])
#     # Initialize the DataTransformation object
#     data_transformation = DataTransformation()
#     # Call the method and expect an exception
#     with pytest.raises(customexception) as exc_info:
#         data_transformation.initialize_data_transformation("train.csv", "test.csv")
#     # Assertions
#     assert "['Price'] not found in axis" in str(exc_info.value)
# # Test generated using Keploy
# def test_initialize_data_transformation_missing_target_column_test(mocker):
#     # Mocking dependencies
#     mocker.patch("pandas.read_csv", side_effect=[
#         pd.DataFrame({"Feature1": [1, 2], "Feature2": ["A", "B"], "Price": [100, 200]}),
#         pd.DataFrame({"Feature1": [3, 4], "Feature2": ["C", "D"]})  # Missing 'Price' column
#     ])
#     # Initialize the DataTransformation object
#     data_transformation = DataTransformation()
#     # Call the method and expect an exception
#     with pytest.raises(customexception) as exc_info:
#         data_transformation.initialize_data_transformation("train.csv", "test.csv")
#     # Assertions
#     assert "['Price'] not found in axis" in str(exc_info.value)

import pytest
from src.data.data_transformation import *  # Importing all from the source module
def test_dummy():
	assert True
