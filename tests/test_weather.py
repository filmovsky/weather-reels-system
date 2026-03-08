from app.weather.providers.open_meteo import get_forecast


def test_open_meteo():

    latitude = 52.23
    longitude = 21.01

    data = get_forecast(latitude, longitude)

    assert data is not None

    print("Weather API test OK")