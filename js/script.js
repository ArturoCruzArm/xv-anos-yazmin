// ============================================
// INVITACIÓN XV AÑOS - GERALDINE GUADALUPE
// Script Principal
// ============================================

// Detectar si el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    // Animación suave al cargar la página
    animatePageLoad();

    // Inicializar Scroll Reveal
    initScrollAnimations();

    // Inicializar botones
    initButtons();

    // Log en consola
    console.log('✨ Invitación XV Años de Geraldine Guadalupe cargada correctamente');
});

// ============================================
// ANIMACIONES DE CARGA
// ============================================

function animatePageLoad() {
    const pages = document.querySelectorAll('.page');
    pages.forEach((page, index) => {
        page.style.animationDelay = `${index * 0.1}s`;
    });
}

// ============================================
// ANIMACIONES AL SCROLL
// ============================================

function initScrollAnimations() {
    // Crear estilo de animación
    const styleSheet = document.createElement('style');
    styleSheet.textContent = `
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInScale {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        .animate-on-scroll {
            animation: fadeInScale 0.8s ease-out forwards;
            animation-play-state: paused;
        }
    `;
    document.head.appendChild(styleSheet);

    // Observer para animaciones al scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observar elementos animables
    document.querySelectorAll('.section-title, .event-block, .feature-item, .gallery-item').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
}

// ============================================
// INICIALIZAR BOTONES
// ============================================

function initButtons() {
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Efecto ripple
            createRippleEffect(this, event);
        });

        // Hover effect
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
        });

        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// ============================================
// EFECTO RIPPLE EN BOTONES
// ============================================

function createRippleEffect(button, event) {
    const ripple = document.createElement('span');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');

    // Agregar estilos de ripple
    if (!document.querySelector('style[data-ripple-styles]')) {
        const rippleStyle = document.createElement('style');
        rippleStyle.setAttribute('data-ripple-styles', 'true');
        rippleStyle.textContent = `
            .btn {
                position: relative;
                overflow: hidden;
            }

            .ripple {
                position: absolute;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.5);
                transform: scale(0);
                animation: rippleAnimation 0.6s ease-out;
                pointer-events: none;
            }

            @keyframes rippleAnimation {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(rippleStyle);
    }

    button.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
}

// ============================================
// COUNTDOWN TIMER (Ya incluido en HTML)
// ============================================

function updateCountdown() {
    const eventDate = new Date('2025-12-31T14:00:00').getTime();
    const now = new Date().getTime();
    const distance = eventDate - now;

    if (distance < 0) {
        // Evento ya pasó
        const elements = ['days', 'hours', 'minutes', 'seconds'];
        elements.forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                el.textContent = '0';
                el.parentElement.style.opacity = '0.5';
            }
        });
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const daysEl = document.getElementById('days');
    const hoursEl = document.getElementById('hours');
    const minutesEl = document.getElementById('minutes');
    const secondsEl = document.getElementById('seconds');

    if (daysEl) daysEl.textContent = days;
    if (hoursEl) hoursEl.textContent = hours;
    if (minutesEl) minutesEl.textContent = minutes;
    if (secondsEl) secondsEl.textContent = seconds;
}

// Actualizar countdown cada segundo
if (typeof updateCountdown === 'function') {
    updateCountdown();
    setInterval(updateCountdown, 1000);
}

// ============================================
// SMOOTH SCROLL
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// ============================================
// LAZY LOADING DE IMÁGENES
// ============================================

function initLazyLoading() {
    const images = document.querySelectorAll('img');

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.animation = 'fadeInScale 0.6s ease-out';
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLazyLoading);
} else {
    initLazyLoading();
}

// ============================================
// UTILIDADES
// ============================================

// Función para validar contrato
function validateContract() {
    const signatures = document.querySelectorAll('.signature-space');
    let allSigned = true;

    signatures.forEach(sig => {
        if (!sig.style.backgroundColor) {
            allSigned = false;
        }
    });

    return allSigned;
}

// Función para exportar como PDF
function exportAsPDF() {
    window.print();
}

// ============================================
// INFORMACIÓN DE CONSOLA
// ============================================

console.log(`
╔════════════════════════════════════════╗
║   XV AÑOS - GERALDINE GUADALUPE        ║
║   Invitación Digital Profesional       ║
║   31 de Diciembre de 2025              ║
╚════════════════════════════════════════╝

✨ Características:
  • Diseño responsivo y elegante
  • Animaciones fluidas
  • Countdown timer
  • Galería fotográfica
  • Información completa del evento
  • Optimizado para todos los dispositivos

📞 Contacto:
  Fotografía Profesional
  (Por definir)
`);
