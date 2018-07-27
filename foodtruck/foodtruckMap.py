import folium
import pandas as pd
import urllib.request
import datetime
import json
import webbrowser

# [CODE 1]

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", "vkTPImVeE4MVQPlXFpFs")
    req.add_header("X-Naver-Client-Secret", "c_rFSF5ZQe")
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 2]

def getGeoData(address):
    base = "https://openapi.naver.com/v1/map/geocode"

    try:
        parameters = "?query=%s" % urllib.parse.quote(address)
    except:
        return None

    url = base + parameters

    retData = get_request_url(url)

    if retData == None:
        return None

    jsonAddress = json.loads(retData, strict=False)

    if 'result' in jsonAddress.keys():
        latitude = jsonAddress['result']['items'][0]['point']['y']
        longitude = jsonAddress['result']['items'][0]['point']['x']
    else:
        return None

    return [latitude, longitude]


def main():

    map = folium.Map(location=[37.5103, 126.982], zoom_start=12)

    filename = 'C:\deep\\foodtruck/foodTrcukE.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []

    for index, row in df.iterrows():
        geoData = getGeoData(row['주소'])
        if geoData != None:
            folium.Marker(geoData, popup=row['가게명'], icon=folium.Icon(color='red')).add_to(map)

    svFilename = 'd:/download/foodTruck1.html'
    map.save(svFilename)
    webbrowser.open(svFilename)

if __name__ == "__main__":
    main()
