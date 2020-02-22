from src.services import seti_service_handler


def test_csv_to_dict():
    """ we need a test to confirm we can read a csv and translate it into a useful python structure
    in this case a list of dict rows"""
    actual = seti_service_handler.read_data()
    assert len(actual) == 299


def test_freq_in_file():
    expected = "1380.702368"
    actual = seti_service_handler.read_data()
    assert actual[0]["Freq"] == expected


def test_grab_frequency_data():
    actual = seti_service_handler.grab_frequency_data()
    assert len(actual) == 299
    assert actual[0] == "1380.702368"
    assert actual[-1] == "1381.564092"


def test_convert_freq_data_to_hex():
    actual = seti_service_handler.convert_freq_data_to_hex()

    assert len(actual) == 299
    assert actual[0] == "1592cf398e970740000000000"
    assert actual[-1] == "acb20d0aaa7df20000000000"


def test_output_to_seti_hex_file():
    actual = seti_service_handler.pump_out_freq_data_as_hex()
    assert actual is True
