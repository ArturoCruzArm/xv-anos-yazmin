# 🚀 GitHub Pages - Tu Sitio Web en Internet

## ✅ Estado Actual

Tu sitio web está **ACTIVO Y EN VIVO** en:

### 📍 URLs principales:
- **Página Principal:** https://arturocruzarm.github.io/xv-anos-geraldine/
- **Contrato:** https://arturocruzarm.github.io/xv-anos-geraldine/contrato.html
- **Contacto:** https://arturocruzarm.github.io/xv-anos-geraldine/contacto.html
- **Admin Panel:** https://arturocruzarm.github.io/xv-anos-geraldine/admin.html

### 🔗 Repositorio GitHub:
https://github.com/ArturoCruzArm/xv-anos-geraldine

---

## 🎯 Cómo Compartir el Sitio

### Opción 1: Compartir el URL Directo
```
https://arturocruzarm.github.io/xv-anos-geraldine/
```
Copia este URL y comparte en:
- ✓ Email
- ✓ WhatsApp
- ✓ Facebook / Instagram
- ✓ SMS
- ✓ Mensajería instantánea

### Opción 2: Crear Código QR
```bash
cd /root/geraldine-15-anos
python3 scripts/generar_qr.py
```
Esto genera códigos QR en la carpeta `codigos_qr/` que puedes:
- Imprimir en las invitaciones
- Compartir en redes sociales
- Enviar por WhatsApp

### Opción 3: Incluir en Invitaciones Impresas
Puedes imprimir el URL o el código QR en las invitaciones físicas.

---

## ✏️ Editar el Contenido

### Método 1: Panel Administrativo (MÁS FÁCIL)
1. Abre: https://arturocruzarm.github.io/xv-anos-geraldine/admin.html
2. Edita toda la información que desees
3. Haz clic en "💾 Guardar Cambios"
4. ¡Los cambios se guardan en tu navegador!

**Ventaja:** No necesitas tocar código ni hacer push a GitHub

### Método 2: Editar Localmente y Hacer Push
```bash
# 1. Clonar el repositorio
git clone https://github.com/ArturoCruzArm/xv-anos-geraldine.git
cd xv-anos-geraldine

# 2. Hacer cambios a los archivos

# 3. Agregar cambios
git add .

# 4. Hacer commit
git commit -m "Descripción de los cambios"

# 5. Hacer push a GitHub
git push origin master
```

Los cambios se actualizan automáticamente en GitHub Pages (dentro de 1-2 minutos).

---

## 📸 Agregar Fotos

### Paso 1: Preparar las Fotos
1. Coloca las fotos en una carpeta local
2. (Opcional) Comprime las fotos:
   ```bash
   python3 scripts/comprimir_imagenes.py
   ```

### Paso 2: Agregar a GitHub
```bash
# Clonar repositorio (si no lo tienes)
git clone https://github.com/ArturoCruzArm/xv-anos-geraldine.git
cd xv-anos-geraldine

# Copiar fotos a la carpeta images/
cp /ruta/a/tus/fotos/* images/

# Hacer commit y push
git add .
git commit -m "Agregar fotos del evento"
git push origin master
```

### Paso 3: Mostrar las Fotos en el Sitio
Edita `index.html` y agrega:
```html
<div class="section">
    <h2>📸 Fotos del Evento</h2>
    <img src="images/foto1.jpg" alt="Descripción" style="width: 100%; border-radius: 10px; margin: 10px 0;">
    <img src="images/foto2.jpg" alt="Descripción" style="width: 100%; border-radius: 10px; margin: 10px 0;">
</div>
```

---

## 🎵 Agregar Música

### Paso 1: Agregar Archivo de Música
```bash
# Copiar archivo MP3 a la carpeta audio/
cp /ruta/a/tu/musica.mp3 audio/

# Hacer commit y push
git add audio/
git commit -m "Agregar música de fondo"
git push origin master
```

### Paso 2: Reproducir en el Sitio
Edita `index.html` y agrega:
```html
<audio src="audio/musica.mp3" controls autoplay loop></audio>
```

---

## 🔄 Sincronizar Cambios Entre Dispositivos

Si trabajas desde múltiples dispositivos:

### Dispositivo A:
```bash
git add .
git commit -m "Cambios realizados"
git push origin master
```

### Dispositivo B:
```bash
git pull origin master
```

---

## 🛠️ Troubleshooting

### El sitio no se actualiza después de hacer push
- **Solución:** GitHub Pages tarda 1-2 minutos en actualizar
- Espera un momento y recarga la página (Ctrl+F5)
- Limpia la caché del navegador

### Los cambios del admin.html no se ven en otros dispositivos
- **Motivo:** El admin.html guarda cambios localmente en el navegador
- **Solución:** Abre admin.html en cada dispositivo y realiza los cambios

### No puedo hacer push a GitHub
- **Verificar:** Está autenticado con GitHub CLI?
- Ejecutar: `gh auth status`
- Si no está autenticado: `gh auth login`

### El repositorio no está sincronizado
```bash
# Ver estado
git status

# Si hay cambios sin hacer commit
git add .
git commit -m "Cambios pendientes"
git push origin master

# Si hay conflictos
git pull origin master
# Resolver conflictos manualmente
git add .
git commit -m "Conflictos resueltos"
git push origin master
```

---

## 📊 Información del Repositorio

| Aspecto | Detalles |
|--------|----------|
| **Propietario** | ArturoCruzArm |
| **Nombre** | xv-anos-geraldine |
| **URL Repositorio** | https://github.com/ArturoCruzArm/xv-anos-geraldine |
| **URL Pages** | https://arturocruzarm.github.io/xv-anos-geraldine/ |
| **Visibilidad** | Público |
| **Rama Principal** | master |
| **GitHub Pages** | ✅ Activado |
| **Hosting** | GitHub Pages (Gratuito) |
| **Dominio** | arturocruzarm.github.io |

---

## 💡 Tips y Trucos

### Crear una rama para cambios experimentales
```bash
# Crear rama
git checkout -b experimental

# Hacer cambios

# Hacer commit
git add .
git commit -m "Cambios experimentales"

# Volver a master
git checkout master

# Después, cuando quieras, fusionar
git merge experimental
git push origin master
```

### Ver historial de cambios
```bash
# Ver últimos 10 commits
git log --oneline -10

# Ver cambios en un archivo específico
git log --oneline archivo.html
```

### Hacer un respaldo de tu sitio
```bash
# Crear un ZIP con todo
zip -r backup-xv-anos.zip .

# O usar GitHub como backup automático
# Tu código está seguro en GitHub
```

---

## 🔐 Seguridad

- ✅ El sitio está protegido con HTTPS automáticamente
- ✅ GitHub mantiene tu código en servidores seguros
- ✅ Puedes hacer el repositorio privado si lo deseas
- ✅ Los datos del admin.html se guardan localmente en tu navegador

---

## 📞 Soporte

Si tienes problemas:

1. **Problemas con GitHub:**
   - Ver documentación: https://docs.github.com/pages
   - Ejecutar: `gh repo view ArturoCruzArm/xv-anos-geraldine`

2. **Problemas técnicos:**
   - Revisar GUIA_INSTALACION.md
   - Ver RESUMEN.txt

3. **Problemas de sincronización:**
   - Ver sección Troubleshooting arriba
   - Ejecutar: `git status` y `git log --oneline`

---

## 🎉 ¡Tu Sitio Está Listo!

Ahora puedes:
- ✅ Compartir el URL con invitados
- ✅ Editar información desde cualquier dispositivo
- ✅ Agregar fotos y música
- ✅ Crear códigos QR
- ✅ Mantener tu código seguro en GitHub
- ✅ Tener un sitio web permanente y gratuito

**¡A celebrar los XV años de Geraldine Guadalupe Villegas!** 🎊✨

---

**Última actualización:** Diciembre 2025
**Versión:** 1.0
