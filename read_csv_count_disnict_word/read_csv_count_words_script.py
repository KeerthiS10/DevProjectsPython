"""
Read csv file and print the distinct count of words and convert it to xml and xlsx file
    1. remove all special character like [$@&*%.,] and [-()]
    2. only add the words less than or equal to 7 char
"""
# Install pip3 install pandas to word with files
# Install pip3 install lxml to use to_xml function from pandas
# Install pip3 install openpyxl to use to_excel function from pandas
#

import pandas as pd
import re


def read_csv_convert_to_list(fname):
    # read csv file and convert ot dataframe
    df_data = pd.read_csv(fname)
    # converting df to string
    data = ''.join(df_data)
    # removing all unwanted special character and returning the list of words
    data = re.sub("[$@&*%.,]", "", data)
    data = re.sub("[-()]", " ", data)
    return data.split()


def get_distinct_word_count(data_ls):
    # counting the number of words and converting to dict to get distinct word and count
    # filtering the dict and removing the words greater than 7
    words_count = {}
    for char in data_ls:
        if char in words_count:
            words_count[char] += 1
        else:
            words_count[char] = 1
        words_count = {key: value for key, value in words_count.items() if len(key) <= 7}
    return words_count


def convert_dict_df(data_dict, filename):
    # converting the result dict to dataframe to save the file in xlsx and xml format
    df_val = pd.DataFrame(data_dict.items(), columns=["Distinct_word", "Count"])
    print(df_val)
    # converting to Excel file and saving it in the given location
    df_val.to_excel(f"{filename}.xlsx")
    print(f"The data is stored in {filename}.xlsx as output")
    # converting to xml file and saving it in the given location
    df_val.to_xml(f"{filename}.xml")
    print(f"The data is stored in {filename}.xml as output")


if __name__ == '__main__':
    filename = "python_paragraph.csv"
    data = read_csv_convert_to_list(filename)
    count = get_distinct_word_count(data)
    excel_output = "distinct_word_count_output"
    convert_dict_df(count, excel_output)
    # print(count)
