import pprint
import requests
import json

# エリアコード
area_dic = {
    "北海道/釧路": "014100",
    "北海道/旭川": "012000",
    "北海道/札幌": "016000",
    "青森県": "020000",
    "岩手県": "030000",
    "宮城県": "040000",
    "秋田県": "050000",
    "山形県": "060000",
    "福島県": "070000",
    "茨城県": "080000",
    "栃木県": "090000",
    "群馬県": "100000",
    "埼玉県": "110000",
    "千葉県": "120000",
    "東京都": "130000",
    "神奈川県": "140000",
    "新潟県": "150000",
    "富山県": "160000",
    "石川県": "170000",
    "福井県": "180000",
    "山梨県": "190000",
    "長野県": "200000",
    "岐阜県": "210000",
    "静岡県": "220000",
    "愛知県": "230000",
    "三重県": "240000",
    "滋賀県": "250000",
    "京都府": "260000",
    "大阪府": "270000",
    "兵庫県": "280000",
    "奈良県": "290000",
    "和歌山県": "300000",
    "鳥取県": "310000",
    "島根県": "320000",
    "岡山県": "330000",
    "広島県": "340000",
    "山口県": "350000",
    "徳島県": "360000",
    "香川県": "370000",
    "愛媛県": "380000",
    "高知県": "390000",
    "福岡県": "400000",
    "佐賀県": "410000",
    "長崎県": "420000",
    "熊本県": "430000",
    "大分県": "440000",
    "宮崎県": "450000",
    "鹿児島県": "460100",
    "沖縄県/那覇": "471000",
    "沖縄県/石垣": "474000",
}

comando_list = {
    "help": "How to handle the module",
    "end": "Terminates the interaction process",
    "weather area_name": "Returns weather information as a dictionary",
}


def help():
    print("=====area list=====")
    for key, value in area_dic.items():
        print(key + ":" + value)
    print("===================")
    print("=====command list=====")
    for key, value in comando_list.items():
        print(key + ":" + value)
    print("===================")


def weather(area_code):
    jma_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
    jma_json = requests.get(jma_url).json()

    # 取得したいデータを選ぶ
    jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][0]
    jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    jma_wind = jma_json[0]["timeSeries"][0]["areas"][0]["winds"][0]
    jma_wave = jma_json[0]["timeSeries"][0]["areas"][0]["waves"][0]

    # 全角スペースの削除
    jma_weather = jma_weather.replace("　", "")
    jma_wind = jma_wind.replace("　", "")
    jma_wave = jma_wave.replace("　", "")

    print(jma_date)
    print(jma_weather)
    print(jma_wind)
    print(jma_wave)

    return {
        "jma_date": jma_date,
        "jma_weather": jma_weather,
        "jma_wind": jma_wind,
        "jma_wave": jma_wave,
    }


if __name__ == "__main__":
    while True:
        user_input = input("command >")
        # 実行終了
        if user_input == "end":
            break
        elif user_input == "help":
            help()
        elif "weather " in user_input:
            area_key = user_input.replace("weather ", "")
            area_code = area_dic.get(area_key)
            if area_code is None:
                print("Please set a valid value")
                continue
            weather(area_code)
        else:
            print("Please enter a valid command")
            print("use the 'help' command")
