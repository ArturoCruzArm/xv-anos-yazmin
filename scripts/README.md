# 🛠️ Scripts Auxiliares

Estos scripts Python ayudan a optimizar y gestionar el sitio web del evento.

## 📋 Scripts Disponibles

### 1. generar_qr.py
Genera códigos QR para compartir el sitio fácilmente.

**Requisitos:**
```bash
pip install qrcode[pil]
```

**Uso:**
```bash
python3 generar_qr.py
```

**Genera:**
- `invitacion.png` - QR a la página principal
- `contrato.png` - QR al contrato
- `contacto.png` - QR a la página de contacto
- `evento.png` - QR con detalles del evento

**Personalización:**
Edita la variable `WEBSITE_URL` con tu dominio real:
```python
WEBSITE_URL = "https://tu-dominio.com"  # Cambiar aquí
```

---

### 2. comprimir_imagenes.py
Comprime automáticamente todas las imágenes de la carpeta `images/`.

**Requisitos:**
```bash
pip install Pillow
```

**Uso:**
```bash
python3 comprimir_imagenes.py
```

**Características:**
- Comprime sin perder calidad significativa
- Respeta las proporciones originales
- Limita el tamaño máximo a 2000x2000 px
- Muestra el porcentaje de reducción

---

## 🚀 Instalación Rápida

### 1. Instalar Python (si no lo tienes)
- **Windows:** Descargar de python.org
- **macOS:** `brew install python3`
- **Linux:** `sudo apt install python3 python3-pip`

### 2. Instalar dependencias
```bash
# Para generar códigos QR
pip install qrcode[pil]

# Para comprimir imágenes
pip install Pillow

# Ambas librerías
pip install qrcode[pil] Pillow
```

### 3. Ejecutar scripts
```bash
python3 generar_qr.py
python3 comprimir_imagenes.py
```

---

## 💡 Casos de Uso

### Caso 1: Compartir invitación por WhatsApp/Redes Sociales
1. Ejecutar `generar_qr.py`
2. Descargar `invitacion.png`
3. Compartir en redes sociales o enviar por WhatsApp
4. Las personas pueden escanear el código para ver la invitación

### Caso 2: Optimizar fotos antes de subir
1. Colocar fotos en la carpeta `images/`
2. Ejecutar `comprimir_imagenes.py`
3. Las imágenes se comprimen automáticamente
4. El sitio carga más rápido

---

## ⚙️ Configuración Avanzada

### Cambiar calidad de compresión
En `comprimir_imagenes.py`:
```python
QUALITY = 85  # Reducir para más compresión (1-100)
```

### Cambiar dimensiones máximas
```python
MAX_WIDTH = 2000   # Ancho máximo en píxeles
MAX_HEIGHT = 2000  # Alto máximo en píxeles
```

### Agregar más códigos QR
En `generar_qr.py`, agregar al diccionario `qr_configs`:
```python
"mi_codigo": {
    "data": "https://mi-sitio.com/pagina",
    "filename": "mi_codigo.png",
    "description": "Mi descripción"
}
```

---

## 📊 Ejemplos de Salida

### generar_qr.py
```
============================================================
Generador de Códigos QR - XV Años Geraldine Guadalupe
============================================================

Generando QR: QR para la página principal de invitación
✅ Guardado en: ../codigos_qr/invitacion.png

... (más códigos) ...

============================================================
✅ Todos los códigos QR han sido generados exitosamente
📁 Ubicación: ../codigos_qr/
============================================================
```

### comprimir_imagenes.py
```
======================================================================
Comprimiendo 5 imagen(s) de ../images
======================================================================

Procesando: foto1.jpg ... ✅
  Original: 5.32 MB → Comprimida: 0.85 MB (84.0% reducción)

... (más imágenes) ...

======================================================================
RESUMEN DE COMPRESIÓN
======================================================================
✅ Archivos comprimidos exitosamente: 5
❌ Archivos con error: 0
📊 Tamaño total original: 25.45 MB
📊 Tamaño total comprimido: 4.23 MB
📊 Reducción total: 83.4%
======================================================================
```

---

## 🐛 Solución de Problemas

### "ModuleNotFoundError: No module named 'qrcode'"
Instala: `pip install qrcode[pil]`

### "ModuleNotFoundError: No module named 'PIL'"
Instala: `pip install Pillow`

### El script no encuentra las imágenes
Asegurate de que:
1. La carpeta `images/` existe
2. Las imágenes están en formato JPG, PNG, GIF o WEBP
3. Ejecutas el script desde la carpeta `scripts/`

### Las imágenes comprimidas se ven borrosas
Aumenta el valor de `QUALITY` en `comprimir_imagenes.py` (máximo 100)

---

## 📝 Notas

- Los scripts están diseñados para ejecutarse desde la carpeta `scripts/`
- Los scripts no eliminarán los originales, sobrescriben en la misma ubicación
- Si necesitas mantener copias originales, haz un backup antes

---

## 🔗 Recursos Útiles

- [Documentación qrcode](https://pypi.org/project/qrcode/)
- [Documentación Pillow](https://pillow.readthedocs.io/)
- [Python Documentation](https://docs.python.org/)

---

**¡Listos para optimizar el sitio!** ⚡✨
