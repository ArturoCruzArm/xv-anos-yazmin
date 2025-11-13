# Selector de Fotos - XV Años Geraldine

## 📸 Uso del Selector (Solo Local)

Este selector de fotos funciona **SOLO EN LOCAL** (en tu computadora), no en GitHub Pages, porque las fotos son muy pesadas.

### ✅ Cómo Usar:

1. **Abrir el selector:**
   - Navega a la carpeta: `C:\Users\foro7\xv-anos-geraldine\`
   - Doble clic en `selector.html`
   - Se abrirá en tu navegador

2. **Seleccionar fotos:**
   - Haz clic en cada foto para ver opciones
   - Selecciona una o más categorías:
     - 📸 **Ampliación** - Para foto grande (50x60cm)
     - 🖼️ **Impresión** - Para fotos estándar (5x7")
     - 📱 **Redes Sociales** - Para compartir en redes
     - 💌 **Invitaciones Web** - Para la invitación digital
     - 🗑️ **Descartar** - No usar

3. **Agregar comentarios:**
   - Si necesitas edición en alguna foto, escríbelo en "Comentarios"
   - Ejemplo: "Mejorar iluminación", "Recortar fondo", etc.

4. **Navegar:**
   - Usa las flechas ← → del teclado
   - O haz clic en los botones de navegación

5. **Exportar selección:**
   - Cuando termines, haz clic en "Exportar Selección"
   - Se descargará un archivo JSON con todas tus elecciones
   - Envía ese archivo al fotógrafo

### 📊 Estadísticas:

El selector muestra en tiempo real cuántas fotos has seleccionado por categoría.

### 🔒 Protección:

- No puedes hacer clic derecho en las fotos
- No puedes arrastrar las fotos
- Las fotos están protegidas contra descarga

### 📁 Estructura de Archivos:

```
xv-anos-geraldine/
├── selector.html          ← Abrir este archivo
├── photos_list.js         ← Lista de 211 fotos
├── fotos-sesion/          ← Fotos originales JPG (211)
├── fotos-webp/            ← Fotos optimizadas WebP (211)
├── convert_to_webp.py     ← Script de conversión
└── generate_photo_list.py ← Regenerar lista si es necesario
```

### ⚠️ Notas Importantes:

1. **Las fotos NO están en GitHub** (son muy pesadas)
2. **Solo funciona en tu computadora local**
3. **Necesitas tener todos los archivos en la misma carpeta**
4. Si agregas más fotos:
   - Ponlas en `fotos-sesion/`
   - Ejecuta: `python convert_to_webp.py`
   - Ejecuta: `python generate_photo_list.py`
   - Recarga `selector.html`

### 🎯 Total de Fotos:

- **211 fotos** disponibles para selección
- Formatos: WebP optimizado (~70% menos peso que JPG)
- Calidad: Alta (85% quality)

---

**Evento:** XV Años de Geraldine Guadalupe Méndez Villegas
**Fecha:** 31 de Diciembre de 2025
**Lugar:** Dolores Hidalgo, Guanajuato
