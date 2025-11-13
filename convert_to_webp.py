#!/usr/bin/env python3
"""
Script para convertir imágenes JPG a WebP
Optimiza las imágenes para web manteniendo buena calidad
"""

import os
from PIL import Image
import glob

def convert_to_webp(input_dir="fotos-sesion", output_dir="fotos-webp", quality=85):
    """
    Convierte todas las imágenes JPG a WebP

    Args:
        input_dir: Directorio con las imágenes originales
        output_dir: Directorio para las imágenes convertidas
        quality: Calidad de la imagen WebP (1-100)
    """
    # Crear directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Buscar todas las imágenes JPG
    jpg_files = glob.glob(os.path.join(input_dir, "*.JPG"))
    jpg_files += glob.glob(os.path.join(input_dir, "*.jpg"))

    total = len(jpg_files)
    print(f"Encontradas {total} imágenes para convertir...")

    converted = 0
    errors = 0

    for i, jpg_path in enumerate(jpg_files, 1):
        try:
            # Obtener nombre base sin extensión
            filename = os.path.basename(jpg_path)
            name_without_ext = os.path.splitext(filename)[0]
            webp_filename = f"{name_without_ext}.webp"
            webp_path = os.path.join(output_dir, webp_filename)

            # Abrir y convertir imagen
            with Image.open(jpg_path) as img:
                # Corregir orientación EXIF si existe
                try:
                    from PIL import ImageOps
                    img = ImageOps.exif_transpose(img)
                except Exception:
                    pass  # Si no hay datos EXIF, continuar sin rotación

                # Convertir a RGB si es necesario
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Guardar como WebP
                img.save(webp_path, "WEBP", quality=quality, method=6)

                # Obtener tamaños de archivo
                original_size = os.path.getsize(jpg_path) / 1024 / 1024  # MB
                webp_size = os.path.getsize(webp_path) / 1024 / 1024  # MB
                reduction = ((original_size - webp_size) / original_size) * 100

                print(f"[{i}/{total}] {filename}")
                print(f"  Original: {original_size:.2f}MB → WebP: {webp_size:.2f}MB (Reducción: {reduction:.1f}%)")

                converted += 1

        except Exception as e:
            print(f"ERROR al convertir {filename}: {e}")
            errors += 1

    print("\n" + "="*60)
    print(f"Conversión completada:")
    print(f"  ✓ Convertidas: {converted}")
    print(f"  ✗ Errores: {errors}")
    print(f"  Total: {total}")
    print("="*60)

if __name__ == "__main__":
    convert_to_webp()
