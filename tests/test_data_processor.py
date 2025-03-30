import pytest
from src.data_processor import process_data

def test_process_data():
    assert process_data([2, 4, 6]) == [4, 16, 36]

print(__name__)
if __name__ == "__main__":
    pytest.main()
