from app.intelligence.forecast_classifier import classify_forecast


def test_classifier():

    weather = {
        "temperature": 36,
        "wind_speed": 10,
        "precipitation": 0
    }

    result = classify_forecast(weather)

    assert result == "extreme_weather"

    print("Intelligence test OK")