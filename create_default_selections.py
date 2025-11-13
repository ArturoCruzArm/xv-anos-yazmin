#!/usr/bin/env python3
"""
Script para crear las selecciones predeterminadas
"""

import json
import re

# Selecciones basadas en el reporte (usando nombres de archivo)
selections_data = {
    # Ampliación
    "DSC_3003": {
        "categories": ["ampliacion"],
        "notes": ""
    },
    # Impresión
    "DJI_20251109130347_0048_D": {"categories": ["impresion"], "notes": ""},
    "DJI_20251109130448_0062_D": {"categories": ["impresion"], "notes": "Borrar objetos personas"},
    "DJI_20251109_125954_782": {"categories": ["impresion"], "notes": ""},
    "DJI_20251109_131933_132": {"categories": ["impresion"], "notes": ""},
    "DJI_20251109_132104_113": {"categories": ["impresion"], "notes": ""},
    "DSC_2925": {"categories": ["impresion"], "notes": ""},
    "DSC_2928": {"categories": ["impresion"], "notes": ""},
    "DSC_2936": {"categories": ["impresion"], "notes": ""},
    "DSC_2938": {"categories": ["impresion"], "notes": ""},
    "DSC_2939": {"categories": ["impresion"], "notes": ""},
    "DSC_2955": {"categories": ["impresion", "redes_sociales", "invitaciones_web"], "notes": ""},
    "DSC_2957": {"categories": ["impresion"], "notes": ""},
    "DSC_2967": {"categories": ["impresion", "invitaciones_web"], "notes": ""},
    "DSC_2970": {"categories": ["impresion"], "notes": ""},
    "DSC_2973": {"categories": ["impresion"], "notes": ""},
    "DSC_2977": {"categories": ["impresion", "redes_sociales", "invitaciones_web"], "notes": ""},
    "DSC_2983": {"categories": ["impresion"], "notes": ""},
    "DSC_2987": {"categories": ["impresion"], "notes": ""},
    "DSC_2996": {"categories": ["impresion"], "notes": ""},
    "DSC_2998": {"categories": ["impresion"], "notes": ""},
    "DSC_3001": {"categories": ["impresion"], "notes": ""},
    "DSC_3002": {"categories": ["impresion", "redes_sociales", "invitaciones_web"], "notes": ""},
    "DSC_3018": {"categories": ["impresion", "invitaciones_web"], "notes": ""},
    "DSC_3023": {"categories": ["impresion"], "notes": ""},
    "DSC_3030": {"categories": ["impresion", "invitaciones_web"], "notes": ""},
    "DSC_3031": {"categories": ["impresion"], "notes": ""},
    "DSC_3034": {"categories": ["impresion", "invitaciones_web"], "notes": ""},
    "DSC_3036": {"categories": ["impresion"], "notes": ""},
    "DSC_3041": {"categories": ["impresion"], "notes": ""},
    "DSC_3043": {"categories": ["impresion", "redes_sociales"], "notes": ""},
    "DSC_3074": {"categories": ["impresion"], "notes": "Editar el letrero de León"},
    "DSC_3077": {"categories": ["impresion"], "notes": ""},
    "IMG_4410": {"categories": ["impresion"], "notes": ""},
    "IMG_4419": {"categories": ["impresion"], "notes": ""},
    # Solo redes sociales
    "DJI_20251109130316_0040_D": {"categories": ["redes_sociales"], "notes": "Borrar objetos"},
    "DSC_2931": {"categories": ["redes_sociales"], "notes": ""},
    # Solo invitaciones web
    "DJI_20251109130445_0060_D": {"categories": ["invitaciones_web"], "notes": "Borrar objetos"},
    "DSC_2927": {"categories": ["invitaciones_web"], "notes": ""},
    "DSC_2948": {"categories": ["invitaciones_web"], "notes": ""},
    "DSC_2980": {"categories": ["invitaciones_web"], "notes": ""},
    "DSC_2999": {"categories": ["invitaciones_web"], "notes": ""},
    "DSC_3025": {"categories": ["invitaciones_web"], "notes": "Borrar personas"},
    "DSC_3028": {"categories": ["invitaciones_web"], "notes": ""},
    "DSC_3032": {"categories": ["invitaciones_web"], "notes": ""},
    "DSC_3044": {"categories": ["invitaciones_web"], "notes": ""},
    "IMG_4438": {"categories": ["invitaciones_web"], "notes": ""},
}

# Generar el código JavaScript
js_code = "const defaultSelections = " + json.dumps(selections_data, indent=4, ensure_ascii=False) + ";\n"

print("Selecciones predeterminadas creadas:")
print(f"- Total: {len(selections_data)} fotos con selecciones")
print("\nCódigo JavaScript generado en default_selections.js")

# Guardar en un archivo
with open('default_selections.js', 'w', encoding='utf-8') as f:
    f.write(js_code)
