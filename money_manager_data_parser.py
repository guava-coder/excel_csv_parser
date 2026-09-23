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


def find_column(probable_s: str, data_frame: pd.DataFrame) -> Column:
    keys = data_frame.keys()
    col = Column(name="", index=0)
    for k in range(len(keys)):
        kt = keys[k]
        for s in probable_s:
            if kt.find(s) >= 0:
                col.name = kt
                col.index = k
        if col.name != "":
            break

    return col


def data_frame_to_custom_dict(data_frame: pd.DataFrame):
    proba_time = "時日"
    col_time = find_column(proba_time, data_frame)

    proba_keys = [
        "資產",
        "類別",
        "子類別",
        "內容",
        "收入/支出",
        "備忘錄",
        "金額",
        "貨幣",
    ]

    def get_custom_dict(data_frame):
        _dict = {}
        for k in proba_keys:
            _dict[k] = data_frame.values.tolist()[0][
                find_column(k, data_frame).index
            ]
        return _dict

    return (
        data_frame.set_index(col_time.name)
        .groupby(col_time.name)
        .apply(lambda x: get_custom_dict(x))
        .to_dict()
    )
