import pandas as pd

data_frame = pd.read_excel(
    io="mm_data.xlsx",
)
# print(data_frame)
# print(data_frame.columns[0])
custom_dict = (
    data_frame.set_index("日")
    .groupby("日")
    .apply(
        lambda x: {
            "資產": x.values.tolist()[0][0],
            "類別": x.values.tolist()[0][1],
            "子類別": x.values.tolist()[0][2],
            "內容": x.values.tolist()[0][3],
            "TWD": x.values.tolist()[0][4],
            "收入/支出": x.values.tolist()[0][5],
            "備忘錄": x.values.tolist()[0][6],
            "金額": x.values.tolist()[0][7],
            "貨幣": x.values.tolist()[0][8],
            "資產.1": x.values.tolist()[0][9],
        }
    )
    .to_dict()
)
cd_keys = list(custom_dict.keys())
print("latest data: ", custom_dict[cd_keys[-1]])
print()
print("data: ", custom_dict)
