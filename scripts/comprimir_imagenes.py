#!/usr/bin/env python3
"""
Script para comprimir imágenes del evento
Requiere: pip install Pillow
"""

import os
from PIL import Image
from pathlib import Path

# Configuración
MAX_WIDTH = 2000
MAX_HEIGHT = 2000
QUALITY = 85
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

def compress_image(input_path, output_path=None, max_width=MAX_WIDTH, max_height=MAX_HEIGHT, quality=QUALITY):
    """
    Comprime una imagen manteniendo la proporción

    Args:
        input_path: Ruta de la imagen original
        output_path: Ruta donde guardar la imagen comprimida (si no se especifica, sobrescribe)
        max_width: Ancho máximo permitido
        max_height: Altura máxima permitida
        quality: Calidad JPEG (1-100)
    """
    try:
        # Abrir imagen
        img = Image.open(input_path)

        # Convertir RGBA a RGB si es necesario
        if img.mode in ('RGBA', 'LA', 'P'):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = bg

        # Calcular nuevas dimensiones manteniendo proporción
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        # Guardar imagen comprimida
        if output_path is None:
            output_path = input_path

        # Determinar formato
        if output_path.lower().endswith('.png'):
            img.save(output_path, 'PNG', optimize=True)
        else:
            img.save(output_path, 'JPEG', quality=quality, optimize=True)

        # Obtener información de tamaño
        original_size = os.path.getsize(input_path)
        new_size = os.path.getsize(output_path)
        reduction = ((original_size - new_size) / original_size) * 100 if original_size > 0 else 0

        return True, original_size, new_size, reduction

    except Exception as e:
        return False, None, None, str(e)

def process_images_in_folder(folder_path):
    """
    Procesa todas las imágenes en una carpeta

    Args:
        folder_path: Ruta de la carpeta con imágenes
    """
    if not os.path.exists(folder_path):
        print(f"⚠️ Carpeta no encontrada: {folder_path}")
        return False

    image_files = [f for f in os.listdir(folder_path)
                   if os.path.isfile(os.path.join(folder_path, f))
                   and Path(f).suffix.lower() in ALLOWED_EXTENSIONS]

    if not image_files:
        print(f"⚠️ No se encontraron imágenes en: {folder_path}")
        return False

    print("=" * 70)
    print(f"Comprimiendo {len(image_files)} imagen(s) de {folder_path}")
    print("=" * 70)
    print()

    total_original = 0
    total_compressed = 0
    successful = 0
    failed = 0

    for filename in image_files:
        filepath = os.path.join(folder_path, filename)

        print(f"Procesando: {filename}", end=" ... ")

        success, original, new, info = compress_image(filepath)

        if success:
            total_original += original
            total_compressed += new
            successful += 1
            size_mb_original = original / (1024 * 1024)
            size_mb_new = new / (1024 * 1024)
            print(f"✅")
            print(f"  Original: {size_mb_original:.2f} MB → Comprimida: {size_mb_new:.2f} MB ({info:.1f}% reducción)")
        else:
            failed += 1
            print(f"❌ Error: {info}")

        print()

    # Resumen
    print("=" * 70)
    print("RESUMEN DE COMPRESIÓN")
    print("=" * 70)
    print(f"✅ Archivos comprimidos exitosamente: {successful}")
    print(f"❌ Archivos con error: {failed}")

    if successful > 0:
        total_reduction = ((total_original - total_compressed) / total_original) * 100
        print(f"📊 Tamaño total original: {total_original / (1024 * 1024):.2f} MB")
        print(f"📊 Tamaño total comprimido: {total_compressed / (1024 * 1024):.2f} MB")
        print(f"📊 Reducción total: {total_reduction:.1f}%")
    print("=" * 70)

    return True

def main():
    """Función principal"""
    print()
    print("🖼️  Compresor de Imágenes para XV Años")
    print()

    # Ruta de la carpeta de imágenes
    images_folder = os.path.join(os.path.dirname(__file__), '..', 'images')

    try:
        process_images_in_folder(images_folder)
    except ImportError:
        print("❌ Error: Se requiere la librería 'Pillow'")
        print("Instala con: pip install Pillow")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
