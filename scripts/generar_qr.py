#!/usr/bin/env python3
"""
Script para generar códigos QR para la invitación de XV años
Requiere: pip install qrcode[pil]
"""

import qrcode
import os
from datetime import datetime

# Crear carpeta de códigos QR si no existe
os.makedirs('../codigos_qr', exist_ok=True)

# Información para los códigos QR
WEBSITE_URL = "http://localhost:8000"  # Cambiar por la URL real del sitio

qr_configs = {
    "invitacion_principal": {
        "data": f"{WEBSITE_URL}/index.html",
        "filename": "invitacion.png",
        "description": "QR para la página principal de invitación"
    },
    "contrato": {
        "data": f"{WEBSITE_URL}/contrato.html",
        "filename": "contrato.png",
        "description": "QR para ver el contrato"
    },
    "contacto": {
        "data": f"{WEBSITE_URL}/contacto.html",
        "filename": "contacto.png",
        "description": "QR para contactar"
    },
    "evento_principal": {
        "data": "Celebración XV Años - Geraldine Guadalupe Villegas - 31 de Diciembre de 2025",
        "filename": "evento.png",
        "description": "QR con información del evento"
    }
}

def generate_qr_code(data, filename, size=10, border=4, fill_color="black", back_color="white"):
    """
    Genera un código QR y lo guarda como imagen

    Args:
        data: Texto o URL a codificar
        filename: Nombre del archivo de salida
        size: Tamaño de cada caja del QR
        border: Tamaño del borde
        fill_color: Color del código (negro)
        back_color: Color de fondo (blanco)
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    filepath = os.path.join('../codigos_qr', filename)
    img.save(filepath)

    return filepath

def main():
    """Función principal para generar todos los códigos QR"""
    print("=" * 60)
    print("Generador de Códigos QR - XV Años Geraldine Guadalupe")
    print("=" * 60)
    print()

    try:
        for qr_key, qr_config in qr_configs.items():
            print(f"Generando QR: {qr_config['description']}")
            filepath = generate_qr_code(
                data=qr_config['data'],
                filename=qr_config['filename']
            )
            print(f"✅ Guardado en: {filepath}")
            print()

        print("=" * 60)
        print(f"✅ Todos los códigos QR han sido generados exitosamente")
        print(f"📁 Ubicación: ../codigos_qr/")
        print("=" * 60)

    except ImportError:
        print("❌ Error: Se requiere la librería 'qrcode'")
        print("Instala con: pip install qrcode[pil]")
        return False
    except Exception as e:
        print(f"❌ Error al generar códigos QR: {e}")
        return False

    return True

if __name__ == "__main__":
    main()
