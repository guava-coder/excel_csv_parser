import pytest
import pandas as pd

from money_manager_data_parser import (
    Record,
    data_frame_to_custom_dict,
    find_column,
    get_mm_data_frame,
    find_time_column,
)


@pytest.fixture
def setup():
    return get_mm_data_frame()


def test_get_mm_data_frame(setup):
    dataframe = setup
    ks = dataframe.keys()
    assert len(ks) > 0
    assert ks[0] == "日"


def test_find_time_column(setup):
    col = find_time_column(df_keys=setup.keys())
    assert col.name == "日"
    assert col.index == 0


def test_find_assets_key(setup):
    data_frame = setup
    col = find_column(probable_s="資產", keys=data_frame.keys())
    assert col.name == "資產"


def test_data_frame_to_custom_dict(setup):
    custom_dict = data_frame_to_custom_dict(setup)
    cd_keys = list(custom_dict.keys())
    latest = custom_dict[cd_keys[-1]]
    assert latest["金額"] > 0


def test_convert_dict_to_record(setup):
    custom_dict = data_frame_to_custom_dict(setup)
    cd_keys = list(custom_dict.keys())
    time:pd.Timestamp = cd_keys[-1]
    latest = custom_dict[time]
    
    record = Record(
        time=str(time),
        assets=latest["資產"],
        currency=latest["貨幣"],
        amount=latest["金額"],
        income_expenses=latest["收入/支出"],
        type=latest["類別"],
        info=latest["內容"],
    )
    assert record.amount > 0
