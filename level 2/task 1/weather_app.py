import requests

api_key = "f59e987fc01685f09bf0389b5985f364"  

while True:
    city = input("\nEnter city name: ")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            print(f"\n--- Weather in {city.capitalize()} ---")
            print(f"☞  Temperature: {temp}°C (Feels like {feels}°C)")
            print(f"☞  Condition: {weather.capitalize()}")
            print(f"☞  Humidity: {humidity}%")
        else:
            print("City not found. Please check the city name.")

    except Exception as error:
        print("Error:", error)

 
    choice = input("\nDo you want to check another city? (y/n): ").lower()
    if choice != 'y' :
        print("Goodbye! 👋😉")
        break
