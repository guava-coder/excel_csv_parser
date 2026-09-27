import pandas as pd
from dataclasses import dataclass


@dataclass
class Record:
    time: str
    assets: str
    currency: str
    amount: int
    income_expenses: str
    type: str
    sub_type: str
    info: str


@dataclass
class Column:
    name: str
    index: int


def get_mm_data_frame():
    return pd.read_excel(
        io="mm_data.xlsx",
    )


def find_column(probable_s: str, keys: pd.Index) -> Column:
    col = Column(name="", index=-1)
    for k in range(len(keys)):
        kt = keys[k]
        for s in probable_s:
            if kt.find(s) >= 0:
                col.name = kt
                col.index = k
        if col.index >= 0:
            break

    return col


def find_time_column(df_keys: pd.Index) -> Column:
    proba_time = "時日期"
    return find_column(probable_s=proba_time, keys=df_keys)


def data_frame_to_custom_dict(data_frame: pd.DataFrame):
    proba_keys = [
        "資產",
        "類別",
        "內容",
        "收入/支出",
        "備忘錄",
        "金額",
        "貨幣",
    ]
    df_keys = data_frame.keys()
    col_time = find_time_column(df_keys)
    df_keys = df_keys.delete(col_time.index)

    def get_custom_dict(data_frame:pd.DataFrame, df_keys:pd.Index):
        _dict = {}
        for k in proba_keys:
            col = find_column(probable_s=k, keys=df_keys)
            _dict[k] = data_frame.values.tolist()[0][col.index]
            print(col,":", _dict[k])
        return _dict

    return (
        data_frame.set_index(col_time.name)
        .groupby(col_time.name)
        .apply(lambda x: get_custom_dict(x, df_keys))
        .to_dict()
    )
