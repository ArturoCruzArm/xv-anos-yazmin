#!/usr/bin/env python3
"""
Script para eliminar fotos descartadas de photos_list.js
"""

import json
import re

# Fotos descartadas (nombres de archivo)
discarded = [
    "DJI_20251109130309_0037_D.webp",  # #2
    "DJI_20251109130311_0038_D.webp",  # #3
    "DJI_20251109130313_0039_D.webp",  # #4
    "DJI_20251109130334_0041_D.webp",  # #6
    "DJI_20251109130340_0043_D.webp",  # #8
    "DJI_20251109130346_0047_D.webp",  # #12
    "DJI_20251109130350_0050_D.webp",  # #15
    "DSC_2994.webp",                    # #127
    "IMG_4382.webp",                    # #212
    "IMG_4406.webp"                     # #236
]

# Leer el archivo photos_list.js
with open('photos_list.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer el array JSON
match = re.search(r'const photos = (\[.*?\]);', content, re.DOTALL)
if match:
    photos_json = match.group(1)
    photos = json.loads(photos_json)

    print(f"Total de fotos antes: {len(photos)}")

    # Filtrar fotos descartadas
    filtered_photos = [p for p in photos if p['filename'] not in discarded]

    print(f"Total de fotos después: {len(filtered_photos)}")
    print(f"Fotos eliminadas: {len(photos) - len(filtered_photos)}")

    # Crear el nuevo contenido
    new_content = f"""// Lista de fotos generada automáticamente
// Total de fotos: {len(filtered_photos)}
// Generado: 2025-11-13 (fotos descartadas eliminadas)

const photos = {json.dumps(filtered_photos, indent=4, ensure_ascii=False)};

window.addEventListener('DOMContentLoaded', function() {{
    console.log(`Cargadas ${{photos.length}} fotos`);
    renderGallery();
    updateStats();
}});
"""

    # Guardar el archivo actualizado
    with open('photos_list.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("\n✓ Archivo photos_list.js actualizado correctamente")
    print(f"✓ Ahora hay {len(filtered_photos)} fotos en el selector")
else:
    print("ERROR: No se pudo encontrar el array de fotos")
