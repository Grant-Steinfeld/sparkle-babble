import os
import csv


SETI_DATA_INPUT_FILE = "seti.csv"
SETI_DATA_OUTPUT_FILE = "seti-freq.txt"


def __get_file_path(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return f"{dir_path}/data/{file_name}"


def read_data(file_name=SETI_DATA_INPUT_FILE):
    rows = []
    with open(__get_file_path(file_name), newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def grab_frequency_data():
    data = read_data()
    return [row["Freq"] for row in data]


def convert_freq_data_to_hex():
    freq_data = grab_frequency_data()
    output = []
    for frequency in freq_data:
        freq_ratio = float(frequency).as_integer_ratio()
        left = hex(freq_ratio[0])
        right = hex(freq_ratio[1])
        output.append(left[2:] + right[2:])
    return output


def pump_out_freq_data_as_hex(file_name=SETI_DATA_OUTPUT_FILE):
    hex_freq_data = convert_freq_data_to_hex()
    full_file_name = __get_file_path(file_name)
    newline = "\r\n"

    try:
        with open(full_file_name, "w") as textfile:
            for hex_freq in hex_freq_data:
                textfile.write(f"{hex_freq}{newline}")
    except Exception as wex:
        raise wex

    return True
