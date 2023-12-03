import pandas as pd

df = pd.read_csv("data/employees.csv", encoding="utf-8", parse_dates=["生年月日"])

def getAge(birthday):
    """日付から現在の年齢を返す関数"""
    today = int(pd.to_datetime("today").strftime("%Y%m%d"))
    birthday = int(birthday.strftime("%Y%m%d"))
    return int((today - birthday) / 10000)

def bariumTest(age):
    """年齢に基づいてバリウム検査結果を返す関数"""
    if age >= 35:
        return True
    elif age >= 30:
        return True
    else:
        return False

# 生年月日を使って年齢を算出
df["年齢"] = df["生年月日"].apply(lambda date: getAge(date))

# バリウム検査列を追加
df["バリウム検査"] = df["年齢"].apply(lambda age: bariumTest(age))

# 結果をCSVファイルに保存
today_str = pd.to_datetime("today").strftime("%Y%m%d")
df.to_csv(f"data/{today_str}_with_barium_test.csv", index=False)

# print(df)

