# generate_all_maps.py
import folium
import os

# Katalog docelowy w systemie
MAPS_DIR = os.path.join(os.path.dirname(__file__), "../../assets/maps")
os.makedirs(MAPS_DIR, exist_ok=True)

def generate_maps():
    # Lista lokalizacji do generowania map
    locations = [
        {"name": "Warszawa", "coords": [52.2297, 21.0122]},
        {"name": "Kraków", "coords": [50.0647, 19.9450]},
        {"name": "Gdańsk", "coords": [54.3520, 18.6466]}
    ]
    
    for loc in locations:
        # Tworzenie mapy
        m = folium.Map(location=loc["coords"], zoom_start=6)
        folium.Marker(loc["coords"], popup=loc["name"]).add_to(m)
        
        # Zapis mapy w katalogu assets/maps
        output_path = os.path.join(MAPS_DIR, f"{loc['name'].lower()}_map.html")
        m.save(output_path)
        print(f"Mapa wygenerowana: {output_path}")

if __name__ == "__main__":
    generate_maps()