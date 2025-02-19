from flask import Flask, request, jsonify
import requests  # Para hacer la solicitud a OpenFoodFacts

app = Flask(__name__)  # Inicializamos Flask

@app.route('/producto', methods=['GET'])
def obtener_producto():
    # Obtener el nombre del producto desde la URL
    nombre_producto = request.args.get('nombre')

    if not nombre_producto:
        return jsonify({"error": "Debes proporcionar un nombre de producto"}), 400

    # Llamamos a la API de OpenFoodFacts
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={nombre_producto}&search_simple=1&action=process&json=1"
    respuesta = requests.get(url)
    datos = respuesta.json()

    # Si no encontramos productos
    if "products" not in datos or len(datos["products"]) == 0:
        return jsonify({"error": "Producto no encontrado"}), 404

    # Tomamos el primer producto encontrado
    producto_info = datos["products"][0]

    # Extraemos la información
    resultado = {
        "nombre": producto_info.get('product_name', 'Nombre no disponible'),
        "marca": producto_info.get('brands', 'Marca no disponible'),
        "ingredientes": producto_info.get('ingredients_text', 'No disponible'),
        "calorias": producto_info.get('nutriments', {}).get('energy-kcal_100g', 'No disponible'),
        "proteinas": producto_info.get('nutriments', {}).get('proteins_100g', 'No disponible'),
        "grasas": producto_info.get('nutriments', {}).get('fat_100g', 'No disponible'),
        "carbohidratos": producto_info.get('nutriments', {}).get('carbohydrates_100g', 'No disponible'),
        "aditivos": producto_info.get('additives_tags', 'No disponible')
    }

    return jsonify(resultado)

# Ejecutamos la API en modo desarrollo
if __name__ == '__main__':
    app.run(debug=True)
