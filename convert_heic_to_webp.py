#!/usr/bin/env python3
"""
Script para convertir imágenes HEIC (iPhone) a WebP
"""

import os
from PIL import Image
import glob
from pillow_heif import register_heif_opener

# Registrar soporte HEIF/HEIC en Pillow
register_heif_opener()

def convert_heic_to_webp(source_dir="F:/2025/12/31", output_dir="fotos-webp", quality=85):
    """
    Convierte todas las imágenes HEIC a WebP

    Args:
        source_dir: Directorio con las imágenes HEIC originales
        output_dir: Directorio para las imágenes convertidas
        quality: Calidad de la imagen WebP (1-100)
    """
    # Crear directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Buscar todas las imágenes HEIC
    heic_files = glob.glob(os.path.join(source_dir, "*.HEIC"))
    heic_files += glob.glob(os.path.join(source_dir, "*.heic"))

    total = len(heic_files)
    print(f"Encontradas {total} imagenes HEIC para convertir...")

    converted = 0
    errors = 0

    for i, heic_path in enumerate(heic_files, 1):
        try:
            # Obtener nombre base sin extensión
            filename = os.path.basename(heic_path)
            name_without_ext = os.path.splitext(filename)[0]
            webp_filename = f"{name_without_ext}.webp"
            webp_path = os.path.join(output_dir, webp_filename)

            # Abrir y convertir imagen
            with Image.open(heic_path) as img:
                # Corregir orientación EXIF si existe
                try:
                    from PIL import ImageOps
                    img = ImageOps.exif_transpose(img)
                except Exception:
                    pass

                # Convertir a RGB si es necesario
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Guardar como WebP
                img.save(webp_path, "WEBP", quality=quality, method=6)

                # Obtener tamaños de archivo
                original_size = os.path.getsize(heic_path) / 1024 / 1024  # MB
                webp_size = os.path.getsize(webp_path) / 1024 / 1024  # MB
                reduction = ((original_size - webp_size) / original_size) * 100

                print(f"[{i}/{total}] {filename}")
                print(f"  Original: {original_size:.2f}MB -> WebP: {webp_size:.2f}MB (Reduccion: {reduction:.1f}%)")

                converted += 1

        except Exception as e:
            print(f"ERROR al convertir {filename}: {e}")
            errors += 1

    print("\n" + "="*60)
    print(f"Conversion completada:")
    print(f"  Convertidas: {converted}")
    print(f"  Errores: {errors}")
    print(f"  Total: {total}")
    print("="*60)

if __name__ == "__main__":
    convert_heic_to_webp()
