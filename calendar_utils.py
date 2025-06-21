import requests

def get_holidays():
    API_KEY = "2Qx4a8OTB0pVdvInEj2fr2Bk6pzrqDVv"
    try:
        url = f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country=IN&year=2025"
        response = requests.get(url)
        holidays = response.json()["response"]["holidays"]
        return [h["name"] for h in holidays[:5]]
    except:
        return ["Holiday data unavailable"]