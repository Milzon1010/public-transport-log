import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_schedule(start, end):
    # Contoh API (dummy endpoint, ganti dengan API real misal Google Maps Directions API)
    # Ini simulasi API, ganti url + key sesuai yang kamu pakai
    url = "https://api.publictransport.example.com/route"
    params = {'origin': start, 'destination': end}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.json_normalize(data['routes'])
            travel_time = df['duration'].min()
            return f"Estimated travel time: {travel_time} minutes"
        else:
            # Kalau API gagal, coba scraping (contoh scrape struktur sederhana)
            scrape_url = f"https://somepublictransportwebsite.com/schedule?start={start}&end={end}"
            page = requests.get(scrape_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            duration_element = soup.find('span', class_='duration')
            if duration_element:
                return f"Scraped travel time: {duration_element.text}"
            else:
                return "Could not find travel time."
    except Exception as e:
        return f"Error fetching data: {str(e)}"
# This code defines a function to get public transport schedules.
# It first tries to fetch data from a public transport API.
# If that fails, it attempts to scrape a website for the travel time.
# The function returns the estimated travel time or an error message.