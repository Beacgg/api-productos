import requests  # Importamos la librería requests

# 🔹 Producto que queremos buscar (puedes cambiarlo por cualquier otro)
producto = "Coca Cola"

# 🔹 URL de la API de OpenFoodFacts
url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={producto}&search_simple=1&action=process&json=1"

# 🔹 Hacer la solicitud a la API
respuesta = requests.get(url)

# 🔹 Convertir la respuesta en formato JSON (datos estructurados)
datos = respuesta.json()

# 🔹 Comprobar si encontramos productos
if "products" in datos and len(datos["products"]) > 0:
    producto_info = datos["products"][0]  # Tomamos el primer resultado encontrado

    print(f"📦 Producto: {producto_info.get('product_name', 'Nombre no disponible')}")
    print(f"🏭 Marca: {producto_info.get('brands', 'Marca no disponible')}")
    print(f"🍽️ Ingredientes: {producto_info.get('ingredients_text', 'No disponible')}")
    print(f"📊 Calorías: {producto_info.get('nutriments', {}).get('energy-kcal_100g', 'No disponible')} kcal por 100g")
    print(f"💪 Proteínas: {producto_info.get('nutriments', {}).get('proteins_100g', 'No disponible')} g")
    print(f"🥑 Grasas: {producto_info.get('nutriments', {}).get('fat_100g', 'No disponible')} g")
    print(f"🍞 Carbohidratos: {producto_info.get('nutriments', {}).get('carbohydrates_100g', 'No disponible')} g")
    print(f"⚠️ Aditivos: {producto_info.get('additives_tags', 'No disponible')}")
else:
    print("⚠️ No se encontró información para este producto.")
