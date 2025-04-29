import unittest
from unittest.mock import patch, mock_open
from csv_file_compare import load_csv, compare

class TestCsvFileCompare(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="header1,header2\nvalue1,value2\nvalue11,value22\n")
    @patch("csv_file_compare.chardet.detect")
    def test_load_csv(self, mock_chardet_detect, mock_open):
        # Arrange
        mock_chardet_detect.return_value = {"encoding": "utf-8"}
        file_path = "dummy.csv"
        keys = ["header1"]

        # Act
        result = load_csv(file_path, keys)

        # Assert
        expected_result = {"value1": {"header1": "value1", "header2": "value2"}, "value11": {"header1": "value11", "header2": "value22"}}
        
        self.assertEqual(result, expected_result)

        # Verify that chardet was called to detect encoding
        mock_chardet_detect.assert_called_once()

        # Verify that the file was opened in binary mode for encoding detection
        mock_open.assert_any_call(file_path, mode="rb")

        # Verify that the file was opened in text mode with the detected encoding
        mock_open.assert_any_call(file_path, mode="r", encoding="utf-8")

    def test_compare_with_no_changes(self):
        # Arrange
        previous = {
            "key1": {"field1": "value1", "field2": "value2"},
            "key2": {"field1": "value3", "field2": "value4"},
        }
        current = {
            "key1": {"field1": "value1", "field2": "value2"},
            "key2": {"field1": "value3", "field2": "value4"},
        }

        # Act
        result = compare(previous, current)

        # Assert
        self.assertEqual(result["deleted"], [])
        self.assertEqual(result["inserted"], [])
        self.assertEqual(result["updated"], [])

    def test_compare_with_deleted_records(self):
        # Arrange
        previous = {
            "key1": {"field1": "value1", "field2": "value2"},
            "key2": {"field1": "value3", "field2": "value4"},
        }
        current = {
            "key1": {"field1": "value1", "field2": "value2"},
        }

        # Act
        result = compare(previous, current)

        # Assert
        self.assertEqual(result["deleted"], [{"key": "key2", "field1": "value3", "field2": "value4"}])
        self.assertEqual(result["inserted"], [])
        self.assertEqual(result["updated"], [])

    def test_compare_with_inserted_records(self):
        # Arrange
        previous = {
            "key1": {"field1": "value1", "field2": "value2"},
        }
        current = {
            "key1": {"field1": "value1", "field2": "value2"},
            "key2": {"field1": "value3", "field2": "value4"},
        }

        # Act
        result = compare(previous, current)

        # Assert
        self.assertEqual(result["deleted"], [])
        self.assertEqual(result["inserted"], [{"key": "key2", "field1": "value3", "field2": "value4"}])
        self.assertEqual(result["updated"], [])

    def test_compare_with_updated_records(self):
        # Arrange
        previous = {
            "key1": {"field1": "value1", "field2": "value2"},
        }
        current = {
            "key1": {"field1": "value1", "field2": "new_value2"},
        }

        # Act
        result = compare(previous, current)

        # Assert
        self.assertEqual(result["deleted"], [])
        self.assertEqual(result["inserted"], [])
        self.assertEqual(
            result["updated"],
            [
                {
                    "key": "key1",
                    "field1": "value1",
                    "field2": "new_value2",
                    "updates": {"field2": ["value2", "new_value2"]},
                }
            ],
        )

    def test_compare_with_all_changes(self):
        # Arrange
        previous = {
            "key1": {"field1": "value1", "field2": "value2"},
            "key2": {"field1": "value3", "field2": "value4"},
        }
        current = {
            "key1": {"field1": "value1", "field2": "new_value2"},
            "key3": {"field1": "value5", "field2": "value6"},
        }

        # Act
        result = compare(previous, current)

        # Assert
        self.assertEqual(result["deleted"], [{"key": "key2", "field1": "value3", "field2": "value4"}])
        self.assertEqual(result["inserted"], [{"key": "key3", "field1": "value5", "field2": "value6"}])
        self.assertEqual(
            result["updated"],
            [
                {
                    "key": "key1",
                    "field1": "value1",
                    "field2": "new_value2",
                    "updates": {"field2": ["value2", "new_value2"]},
                }
            ],
        )

if __name__ == "__main__":
    unittest.main()