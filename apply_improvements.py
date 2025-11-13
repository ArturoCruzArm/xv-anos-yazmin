#!/usr/bin/env python3
"""
Script para aplicar todas las mejoras a la invitación
"""

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Eliminar sección de contacto (líneas 364-392)
# Encontrar y eliminar
new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<!-- INFORMACIÓN DE CONTACTO -->' in line:
        skip = True
    if skip and '<!-- CIERRE/DESPEDIDA -->' in line:
        skip = False
    if not skip:
        new_lines.append(line)

# 2. Agregar hashtag en la portada (después del círculo de edad)
hashtag_html = """
            <div class="event-hashtag">
                <p class="hashtag-label">Comparte tus fotos con</p>
                <h3 class="hashtag-text">#GeralXV</h3>
                <p class="hashtag-sublabel">#Geral15Años #MisXVGeral</p>
            </div>
"""

# 3. Agregar botón de calendario en programa
calendar_button = """
                <div class="calendar-button-container">
                    <button onclick="addToCalendar()" class="btn-calendar">
                        📅 Agregar a mi Calendario
                    </button>
                </div>
"""

# 4. Agregar timeline después del programa
timeline_html = """
    <!-- ITINERARIO DEL DÍA -->
    <section class="page page-timeline">
        <div class="page-content">
            <h2 class="section-title">Itinerario del Día</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-time">17:00 PM</div>
                    <div class="timeline-content">
                        <h3>Ceremonia Religiosa</h3>
                        <p>Parroquia de Nuestra Señora de los Dolores</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">18:30 PM</div>
                    <div class="timeline-content">
                        <h3>Recepción</h3>
                        <p>Bienvenida a los invitados</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">19:00 PM</div>
                    <div class="timeline-content">
                        <h3>Cena</h3>
                        <p>Disfruta de una deliciosa cena</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">20:00 PM</div>
                    <div class="timeline-content">
                        <h3>Vals y Celebración</h3>
                        <p>Baile de la quinceañera</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">21:00 PM</div>
                    <div class="timeline-content">
                        <h3>¡Fiesta!</h3>
                        <p>Baile y diversión hasta la madrugada</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# 5. Botón de compartir en el cierre
share_button = """
            <div class="share-buttons">
                <p class="share-label">Comparte esta invitación:</p>
                <div class="share-icons">
                    <button onclick="shareWhatsApp()" class="btn-share whatsapp" title="Compartir por WhatsApp">
                        <i class="fab fa-whatsapp"></i>
                    </button>
                    <button onclick="shareFacebook()" class="btn-share facebook" title="Compartir en Facebook">
                        <i class="fab fa-facebook"></i>
                    </button>
                    <button onclick="copyLink()" class="btn-share link" title="Copiar enlace">
                        <i class="fas fa-link"></i>
                    </button>
                </div>
            </div>
"""

# Aplicar cambios
result = []
for i, line in enumerate(new_lines):
    result.append(line)

    # Agregar hashtag después del círculo de edad
    if 'cover-age-circle' in line and '</div>' in new_lines[i+2]:
        # Buscar el cierre del div de age-circle
        j = i
        while j < len(new_lines) and 'age-number' not in new_lines[j]:
            j += 1
        while j < len(new_lines) and '</div>' not in new_lines[j]:
            j += 1
        if j < len(new_lines):
            result.append(hashtag_html)

    # Agregar botón de calendario antes del cierre de page-program
    if 'page-program' in new_lines[i-20:i] and '</section>' in line and 'countdown' in ''.join(new_lines[i-30:i]):
        result.insert(-1, calendar_button)

    # Agregar timeline después de page-program
    if '</section>' in line and 'page-program' in ''.join(new_lines[i-30:i]):
        found_program = False
        for j in range(max(0, i-50), i):
            if 'page page-program' in new_lines[j]:
                found_program = True
        if found_program:
            result.append(timeline_html)

    # Agregar botón compartir en cierre
    if 'closing-message' in line:
        result.append(share_button)

# Escribir resultado
with open('index-improved.html', 'w', encoding='utf-8') as f:
    f.writelines(result)

print("✓ Sección de contacto eliminada")
print("✓ Hashtag agregado")
print("✓ Botón de calendario agregado")
print("✓ Timeline agregado")
print("✓ Botón compartir agregado")
print("\nArchivo generado: index-improved.html")
print("Revisa el archivo y si está bien, reemplaza index.html")
