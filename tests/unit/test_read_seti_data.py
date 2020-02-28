from src.services import seti_service_handler
from src.services.seti_service_handler import InvalidDelimiterException
import pytest

# def test_csv_to_dict():
#     """ we need a test to confirm we can read a csv and translate it into a useful python structure
#     in this case a list of dict rows"""
#     actual = seti_service_handler.read_data()
#     assert len(actual) == 1123505


def test_freq_in_file():
    expected = "1380.702368"
    actual = seti_service_handler.read_data()
    assert actual[0]["Freq"] == expected


# def test_grab_frequency_data():
#     actual = seti_service_handler.grab_frequency_data()
#     assert len(actual) == 1123505
#     assert actual[0] == "1380.702368"
#     assert actual[-1] == "1381.564092"


# def test_convert_freq_data_to_hex():
#     actual = seti_service_handler.convert_freq_data_to_hex()

#     assert len(actual) == 1123505
#     assert actual[0] == "1592cf398e97074"
#     assert actual[-1] == "656365e8922531"


def test_delimiter_valid():
    actual = seti_service_handler.is_valid_delimiter(" ")
    assert actual is True


@pytest.mark.xfail(raises=InvalidDelimiterException)
def test_delimiter_invalid_long_string():
    actual = seti_service_handler.is_valid_delimiter("~~")
    assert actual is True


@pytest.mark.xfail(raises=InvalidDelimiterException)
def test_delimiter_invalid_NaStr():
    actual = seti_service_handler.is_valid_delimiter(42)
    assert actual is True


def test_chunk_to_fixed_width():
    expected_width = 80
    actual = seti_service_handler.formatLineTo(" ", expected_width)
    assert len(actual) == 4


def test_output_to_seti_hex_file():
    SPACE = " "
    actual = seti_service_handler.pump_out_freq_data_as_hex(80, SPACE)
    assert actual is True
