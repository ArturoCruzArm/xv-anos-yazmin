#!/usr/bin/env python3
"""
Script para obtener fotos marcadas para invitaciones web
"""

import json
import re

# Leer default_selections.js
with open('default_selections.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer el objeto JSON
match = re.search(r'const defaultSelections = ({.*?});', content, re.DOTALL)
if match:
    selections_json = match.group(1)
    selections = json.loads(selections_json)

    # Filtrar fotos con invitaciones_web
    web_photos = []
    for name, data in selections.items():
        if 'invitaciones_web' in data['categories']:
            web_photos.append(name + '.webp')

    print(f"Total de fotos para invitaciones web: {len(web_photos)}\n")
    print("Fotos para la galería web:")
    for i, photo in enumerate(web_photos, 1):
        print(f"{i}. {photo}")

    # Generar array JavaScript
    js_array = json.dumps(web_photos, indent=4)
    print(f"\n\nArray JavaScript:\nconst webGalleryPhotos = {js_array};")
else:
    print("ERROR: No se pudo encontrar el objeto de selecciones")
