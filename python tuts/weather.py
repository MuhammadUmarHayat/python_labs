import requests

def get_weather(city):
    try:
        # Encode the city name to handle spaces or special characters
        city = str(city).replace(" ", "%20")
        
        # Fetch weather from wttr.in with proper URL formatting
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        
        # Check if the response was successful
        if response.status_code == 200:
            weather_report = response.text
            print(f"Weather in {city.replace('%20', ' ')}: {weather_report}")
        elif response.status_code == 404:
            print(f"Error: City '{city.replace('%20', ' ')}' not found. Please check the city name.")
        else:
            print(f"Failed to retrieve weather data for {city.replace('%20', ' ')}. HTTP Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Input city name in console
city = 'Jehlum'  # You can replace this with input("Enter your city name: ") for dynamic input
get_weather(city)
