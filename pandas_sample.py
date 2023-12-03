import pandas as pd

df = pd.read_csv(
    "data/data.csv",
    skiprows=3,  # 行を飛ばす
    # usecols=[0, 1],  # 列を配列で指定
    # delimiter=",",  # 区切り文字 デフォルトはカンマ
    dtype={"年月日": "str", "平均気温(℃)": "float"},  # 辞書で各データ型を指定できる 指定無しはstr or float
    parse_dates=["年月日"],  # 日付型のデータはここで指定する
    encoding="shift-jis",
)
print(df)  # 全表示
print(df["年月日"])  # 列を指定
print(df[df["年月日"] == pd.to_datetime("2021-03-30")])  # 検索 
