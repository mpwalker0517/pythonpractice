import schedule
import time

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data

def celsius_to_farenheit(celsius):
    return(celsius * 9/5) + 32

def send_text_message(body):
    account_sid = ""
    auth_token = ""
    from_phone_number = ""
    to_phone_number = ""

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_= from_phone_number,
        to=to_phone_number
    )
    print("Text message sent!")

def send_weather_update():
    #Hardcoded latitude and longitude for Cincinnati
    latitude = 39.1031
    longitude = 84.5120

    weather_data = get_weather(latitude,longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]
    temperature_farenheit = celsius_to_farenheit(temperature_celsius)

    weather_info= (
        f"Good morning!\n"
        f"Current weather in Cincinnati:\n"
        f"Temperature: {temperature_farenheit:.2f}F \n" 
        f"Relative humidity: {relative_humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"
    )

    send_text_message(weather_info)

def main():
    schedule.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
