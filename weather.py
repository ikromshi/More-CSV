from urllib.request import urlopen
import json


def fetch_weather_info(zipcode):
    api_key = "106af9554c40433c03cc1fc20fe91ba6"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?zip=" + str(
        zipcode) + ",us&appid=f47252c8cfc93091922cfdf86bcbff69"
    web_data = urlopen(weather_url)
    print(weather_url)

    byte_list = web_data.readlines()
    weather_str = byte_list[0].decode("utf-8")
    d = json.loads(weather_str)
    return d


def get_current_temp(weather_dict):
    '''
    returns the current temperature in Fahrenheit when given a weather_str fetched from the openweathermap API
    '''
    kelvin_temp = weather_dict["main"]["temp"]
    f_temp = (kelvin_temp - 273.15) * (9 / 5) + 32
    return f_temp


def main():
    weather_dict = fetch_weather_info("14850")
    print(weather_dict)

    temp = get_current_temp(weather_dict)
    print("The current Temp is:", temp)


main()
