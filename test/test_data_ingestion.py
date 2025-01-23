from unittest.mock import patch
import pytest
from src.data.data_ingestion import *  # Importing all from the source module
def test_dummy():
	assert True
# Test generated using Keploy
def test_fetch_and_save_data_happy_path():
    """
    Test that the fetch_and_save_data method downloads data and saves it correctly.
    """
    # Mock read_csv to return a sample DataFrame
    with patch('pandas.read_csv') as mock_read_csv:
        mock_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        mock_read_csv.return_value = mock_data
        # Mock os.makedirs to avoid creating actual directories
        with patch('os.makedirs') as mock_makedirs:
            # Mock DataFrame.to_csv to avoid writing files
            with patch.object(pd.DataFrame, 'to_csv') as mock_to_csv:
                ingestion = DataIngestion()
                ingestion.fetch_and_save_data()
                # Assertions to ensure the correct behavior
                mock_read_csv.assert_called_once_with(ingestion.data_config.url)
                mock_makedirs.assert_called_once_with("artifacts", exist_ok=True)
                assert mock_to_csv.call_count == 3  # raw, train, and test data are saved