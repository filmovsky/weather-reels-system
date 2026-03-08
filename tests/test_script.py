from app.scripting.generators.en import generate_script


def test_script_generation():

    weather = {
        "temperature": 22,
        "wind_speed": 10,
        "precipitation": 0
    }

    result = generate_script("Test Region", weather)

    assert isinstance(result, str)

    print("Script generation test OK")