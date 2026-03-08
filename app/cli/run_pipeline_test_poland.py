# Lokalizacja: app/cli/run_pipeline_test_poland.py

import os
from app.tts.elevenlabs_tts import generate_voice

# Tworzymy folder output, jeśli nie istnieje
os.makedirs("output", exist_ok=True)

def run_test_pipeline_poland():
    # Przykładowe dane testowe
    regions = {
        "warsaw": "Dzisiaj w Warszawie spodziewamy się słońca i lekkiego wiatru.",
        "krakow": "W Krakowie pojawią się przelotne opady deszczu, temperatura ok. 18°C."
    }

    for region_id, script_text in regions.items():
        # Ścieżka pliku wyjściowego
        output_file = f"output/{region_id}.mp3"
        
        # Generowanie audio z wykorzystaniem pliku elevenlabs_tts.py
        generate_voice(
            region_id=region_id,
            text=script_text,
            output_path=output_file
        )

        print(f"[INFO] Wygenerowano audio dla {region_id}: {output_file}")


if __name__ == "__main__":
    run_test_pipeline_poland()