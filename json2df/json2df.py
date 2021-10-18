import os
import numpy as np
import pandas as pd
import json

# Set Print option
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)
pd.set_option('display.max_colwidth', 1000)


class LoadInfo:
    def __init__(self, info=None, file=None):
        self._info = info
        self._file = file
        self._config = self._load_config()

    def get_data(self):
        return self._config

    def load_from_file(self):
        with open(self._file) as f:
            data = f.read()
        return json.loads(data)

    def load_from_str(self):
        if isinstance(self._info, (dict, list)):
            return self._info
        elif isinstance(self._info, str):
            return json.loads(self._info)
        else:
            raise ValueError('Load config error')

    def _load_config(self):
        if self._info:
            return self.load_from_str()
        else:
            return self.load_from_file()


class JSONToDataframe:
    """ This is generic class that can we used to convert any
     JSON or Python dict into Pandas dataframe
     Args:
         json_data: this can be a json file or a python dict or list
         of python dict.
     Main method: The main method is the convert_to_df
     """
    def __init__(self, json_data):
        self._json_data = json_data

    @property
    def json_data(self):
        return self._json_data

    def _json_to_df(self, data_=None, col_pre_fix='', **kwargs):
        """ This the main method that converts the json to pandas dataframe.
         Its being called recursively."""
        if data_ is None:
            data_ = LoadInfo(self.json_data).get_data()
        else:
            data_ = LoadInfo(data_).get_data()

        master_df = kwargs.get('master_df', pd.DataFrame({'jkey_': [1]}))

        for k, v in data_.items():
            field_name = f'{k}' if col_pre_fix == '' else f'{col_pre_fix}_{k}'

            if not isinstance(v, (list, dict, tuple)):
                df_ = pd.DataFrame({field_name: [v], 'jkey_': [1]})
                master_df = pd.merge(master_df, df_, how='inner', on='jkey_')

            elif isinstance(v, dict):
                kw = {'master_df': master_df}
                master_df = self._json_to_df(data_=v, col_pre_fix=field_name, **kw)

            else:
                data_list = []
                m_df = pd.DataFrame({'jkey_': [1]})
                for i_ in v:
                    if isinstance(i_, dict) and i_:
                        data_list.append(
                            self._json_to_df(
                                i_,
                                col_pre_fix=field_name,
                                master_df=m_df
                            )
                        )
                    else:
                        t_df = pd.DataFrame({field_name: [i_], 'jkey_': [1]})
                        data_list.append(t_df)
                if data_list:
                    df_tmp = pd.concat(data_list, axis=0, ignore_index=True, sort=False)
                    master_df = pd.merge(master_df, df_tmp, how='inner', on='jkey_')
                else:
                    df_tmp = pd.DataFrame({field_name: [np.nan], 'jkey_': [1]})
                    master_df = pd.merge(master_df, df_tmp, how='inner', on='jkey_')

        return master_df

    def convert_to_df(self):
        info = LoadInfo(self.json_data).get_data()
        if isinstance(info, list):
            dflist_ = []
            for i_ in info:
                dflist_.append(self._json_to_df(i_))
            df_ = pd.concat(dflist_, axis=0, ignore_index=True, sort=False)
            df_.drop('jkey_', axis=1, inplace=True)
            return df_

        df_ = self._json_to_df(self.json_data)
        df_.drop('jkey_', axis=1, inplace=True)
        return df_


if __name__ == '__main__':
    json_data_ = {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters":
            {
                "batter_1":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"},
                        {"id": "1003", "type": "Blueberry"},
                        {"id": "1004", "type": "Devil's Food"}
                    ],
                "batter_2":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"},
                        {"id": "1003", "type": "Blueberry"},
                        {"id": "1004", "type": "Devil's Food"}
                    ]
            },
        "topping":
            [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5005", "type": "Sugar"},
                {"id": "5007", "type": "Powdered Sugar"},
                {"id": "5006", "type": "Chocolate with Sprinkles"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"}
            ]
    }

    # jdata = LoadInfo(info=json_data_).get_data()
    j2df = JSONToDataframe(json_data=json_data_).convert_to_df()
    print(j2df)

