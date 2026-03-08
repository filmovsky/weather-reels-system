from app.workers.tasks_weather import fetch_weather
from app.workers.tasks_analysis import analyze_weather
from app.workers.tasks_script import generate_weather_script
from app.db.session import init_db


def run(region_name: str, latitude: float, longitude: float):

    weather = fetch_weather(latitude, longitude)

    analysis = analyze_weather(weather)

    script = generate_weather_script(region_name, weather)

    return {
        "weather": weather,
        "analysis": analysis,
        "script": script
    }


if __name__ == "__main__":

    init_db()

    result = run("Test Region", 52.23, 21.01)

    print(result)