from bs4 import BeautifulSoup
import requests

url = "https://www.dof.gob.mx/indicadores.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, verify=False, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table")
    
    for i, table in enumerate(tables):
        print(f"\n🔹 Tabla {i + 1}:")
        print(table.get_text(separator="\n", strip=True))  # Muestra el contenido sin etiquetas HTML

else:
    print("❌ Error al acceder a la página:", response.status_code)
