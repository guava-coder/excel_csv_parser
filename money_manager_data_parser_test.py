from money_manager_data_parser import (
    data_frame_to_custom_dict,
    find_column,
    get_mm_data_frame,
)


def test_get_mm_data_frame():
    dataframe = get_mm_data_frame()
    ks = dataframe.keys()
    assert len(ks) > 0
    assert ks[0] == "日"


def test_data_frame_to_custom_dict():
    custom_dict = data_frame_to_custom_dict(get_mm_data_frame())
    cd_keys = list(custom_dict.keys())
    latest = custom_dict[cd_keys[-1]]
    print("latest data: ", latest)
    assert latest["金額"] > 0


def test_find_time_key():
    probable_s = "時日"
    col = find_column(probable_s, get_mm_data_frame())
    assert col.name == "日"
    assert col.index == 0

def test_find_assets_key():
    data_frame = get_mm_data_frame()
    col = find_column("資產", data_frame)
    assert col.name == "資產"