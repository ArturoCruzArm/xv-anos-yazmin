# 📖 Guía de Instalación y Personalización

## Instalación Rápida

### Opción 1: Abrir directamente en el navegador
1. Descargar o clonar el repositorio
2. Abrir el archivo `index.html` en tu navegador web (hacer doble clic)

### Opción 2: Con Python
```bash
cd geraldine-15-anos/
python3 -m http.server 8000
```
Luego acceder a: `http://localhost:8000`

### Opción 3: Con Node.js
```bash
npm install -g http-server
cd geraldine-15-anos/
http-server
```
Acceder a: `http://localhost:8080`

---

## 🎨 Personalización

### Método 1: Panel Administrativo (Recomendado)
1. Abrir `admin.html` en el navegador
2. Llenar todos los campos con la información correcta
3. Hacer clic en "💾 Guardar Cambios"
4. La configuración se guardará automáticamente en el navegador

### Método 2: Editar archivos HTML directamente
1. Abrir `index.html` con un editor de texto (VS Code, Notepad++, etc.)
2. Reemplazar los datos de ejemplo con la información real
3. Guardar los cambios
4. Recargar la página en el navegador

### Método 3: Modificar config.js
1. Abrir `config.js` con un editor de texto
2. Editar el objeto `EVENT_CONFIG` con los datos reales
3. Guardar y recargar el navegador

---

## 📝 Información que Debes Actualizar

### 1. Datos de la Quinceañera
- [ ] Nombre completo
- [ ] Nombre de la madre/tutora
- [ ] Color del vestido

### 2. Información del Evento
- [ ] Fecha exacta
- [ ] Ubicación de la ceremonia religiosa
- [ ] Ciudad/Estado
- [ ] Hora de la ceremonia

### 3. Información de la Fiesta
- [ ] Nombre del salón
- [ ] Distancia/ubicación relativa
- [ ] Hora de inicio
- [ ] Hora de término
- [ ] Entretenimiento (bandas, DJs, etc.)

### 4. Paquete Fotográfico
- [ ] Precio
- [ ] Viáticos
- [ ] Detalles de lo incluido

### 5. Información de Contacto
- [ ] Nombre del fotógrafo
- [ ] Teléfono
- [ ] Email
- [ ] Sitio web (opcional)

---

## 🎵 Agregar Multimedia

### Agregar Imágenes
1. Colocar imágenes en la carpeta `images/`
2. Editar `index.html` y agregar:
```html
<img src="images/nombre.jpg" alt="descripción" style="width: 100%; border-radius: 10px;">
```

### Agregar Música de Fondo
1. Colocar archivos MP3 en la carpeta `audio/`
2. Agregar a `index.html`:
```html
<audio src="audio/musica.mp3" controls autoplay loop></audio>
```

---

## 🖨️ Imprimir el Contrato

1. Ir a la página del contrato (botón "Ver Contrato")
2. Hacer clic en "🖨️ Imprimir Contrato"
3. En el navegador:
   - Ajustar márgenes: Ninguno o Mínimo
   - Orientación: Vertical
   - Escala: 100%
4. Guardar como PDF o imprimir en papel

---

## 📤 Compartir el Sitio

### Opción 1: GitHub Pages (Recomendado)
1. Crear cuenta en GitHub.com
2. Crear un nuevo repositorio con el nombre `xv-anos-geraldine`
3. Subir los archivos
4. En Settings > Pages, activar GitHub Pages
5. El sitio estará disponible en: `https://tu-usuario.github.io/xv-anos-geraldine/`

### Opción 2: Netlify
1. Ir a netlify.com
2. Crear cuenta
3. Drag & drop la carpeta del proyecto
4. El sitio estará disponible en una URL pública

### Opción 3: Servidor Local
1. Compartir los archivos por USB o email
2. Los usuarios pueden abrir `index.html` directamente

---

## 🔍 Verificación

Antes de compartir, verifica:
- [ ] Todos los nombres están correctos
- [ ] Las fechas y horas están correctas
- [ ] Los precios están actualizados
- [ ] El número de contacto es correcto
- [ ] El email de contacto funciona
- [ ] Todas las páginas se cargan correctamente
- [ ] El contrato se imprime correctamente
- [ ] Los colores se ven bien

---

## ❓ Solución de Problemas

### El sitio no se abre
- Asegurate de tener un navegador moderno (Chrome, Firefox, Edge, Safari)
- Intenta abrir en modo "Acceso anónimo" del navegador
- Verifica que el archivo `index.html` existe

### Los estilos no se ven correctamente
- Limpia la caché del navegador (Ctrl+Shift+Del)
- Intenta abrir en otro navegador
- Verifica que los archivos CSS están en la carpeta `css/`

### Las imágenes no se muestran
- Verifica que las imágenes estén en la carpeta `images/`
- Revisa que la ruta en HTML sea correcta
- Intenta con imágenes en formato JPG o PNG

### El contrato no imprime bien
- Desactiva encabezados y pies de página en la configuración de impresión
- Usa márgenes mínimos
- Intenta guardar como PDF primero

---

## 🚀 Características Avanzadas

### Agregar Código QR
```python
# generar_qr.py
import qrcode

qr = qrcode.QR Code(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('http://tu-sitio.com')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('codigos_qr/invitacion.png')
```

### Personalizar Colores
Editar las variables CSS en `css/styles.css`:
```css
:root {
    --gold: #D4AF37;           /* Color primario */
    --dark-gold: #DAA520;      /* Color oscuro */
    --light-gold: #FFD700;     /* Color claro */
    /* ... etc ... */
}
```

---

## 📞 Soporte

Si tienes problemas:
1. Verifica que todos los archivos están en el mismo directorio
2. Asegurate de tener permisos de lectura en los archivos
3. Intenta en otro navegador
4. Limpia la caché del navegador

---

## 📄 Archivos del Proyecto

```
geraldine-15-anos/
├── index.html                  # Página principal
├── contrato.html              # Contrato de servicios
├── contacto.html              # Página de contacto
├── admin.html                 # Panel administrativo
├── config.js                  # Configuración del evento
├── css/
│   ├── styles.css            # Estilos principales
│   └── contrato-styles.css   # Estilos del contrato
├── js/
│   └── script.js             # Scripts interactivos
├── images/                   # Carpeta para imágenes
├── audio/                    # Carpeta para audio
├── codigos_qr/               # Códigos QR
├── README.md                 # Información general
├── GUIA_INSTALACION.md       # Esta guía
└── .gitignore                # Archivos ignorados por git
```

---

**¡Listo para celebrar los XV años de Geraldine Guadalupe!** 🎉✨

*Última actualización: Diciembre 2025*
