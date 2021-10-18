# import pandas as pd
from json2df.json2df import JSONToDataframe
from json2df.json2df import LoadInfo


if __name__ == '__main__':
    json_file = 'data/svg_example.json'

    info_ = LoadInfo(file=json_file).get_data()

    j2df = JSONToDataframe(json_data=info_).convert_to_df()
    print(j2df.head(n=15))
