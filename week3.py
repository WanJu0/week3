import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理json 資料格式
print(data)

data_All=data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
    for spot in data_All:
        if int(spot["xpostDate"][0:4]) >= 2015:
            address=spot["address"]
            address_split=(address.split("  "))
            region=address_split[1]
            longitude=spot["longitude"]
            latitude=spot["latitude"]
            photo=spot["file"]
            photo_split=photo.split("https")
            file.write(spot["stitle"]+","+region[0:3]+","+longitude+","+latitude+","+"https"+photo_split[1]+"\n")
