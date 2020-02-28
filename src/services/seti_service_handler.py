import os
import csv


SETI_DATA_INPUT_FILE = "seti.csv"
SETI_DATA_OUTPUT_FILE = "seti-freq.txt"


class InvalidDelimiterException(Exception):
    def __init__(self, message):
        self.message = message


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
        output.append(left[2:] + str(right[2:]).replace("0", ""))
    return output


def is_valid_delimiter(delimiter):
    """https://en.wikipedia.org/wiki/Delimiter"""
    if isinstance(delimiter, str) is False:
        raise InvalidDelimiterException(
            f"delimiter should be of type String not this {type(delimiter)} --> {delimiter}"
        )
    else:
        if len(delimiter) != 1:
            raise InvalidDelimiterException(
                f"delimiter should be a single character, not this --> '{delimiter}' with a lenght of {len(delimiter)} "
            )

        return True


def formatLineTo(delimiter, width=80):
    """ create fixed width array entries delimited and wrap"""
    is_valid_delimiter(delimiter)
    hex_freq_data = convert_freq_data_to_hex()
    wrapped_hex_freq_data = []
    tmpBucketStack = []
    # fill buckets wrapping with delimiters
    for hex_freq in hex_freq_data:
        tmpBucketStack.append(delimiter)
        for hexchar in hex_freq:
            if len(tmpBucketStack) == width:
                # bucket full
                wrapped_hex_freq_data.append("".join(tmpBucketStack))
                tmpBucketStack = []
            else:
                # continue to fill bucket
                tmpBucketStack.append(hexchar)

    return wrapped_hex_freq_data


def pump_out_freq_data_as_hex(
    width,
    in_the_line_delimiter=" ",
    file_name=SETI_DATA_OUTPUT_FILE,
    end_of_line_delimiter="\r\r",
):

    hex_freq_data = formatLineTo(in_the_line_delimiter, width)
    full_file_name = __get_file_path(file_name)
    # delimiter = " "
    delimiter = "\r\n"
    eof = "***"

    try:
        with open(full_file_name, "w") as textfile:
            for hex_freq in hex_freq_data:
                textfile.write(f"{hex_freq}{delimiter}")
            textfile.write(f"{eof}")

    except Exception as wex:
        raise wex

    return True
