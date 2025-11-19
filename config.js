// Configuración del evento - XV Años de Yazmin del Carmen
// Edita estos valores para personalizar la invitación y contrato

const EVENT_CONFIG = {
    // Información de la quinceañera
    quinceaneraName: "Yazmin del Carmen García Servín",
    quinceaneraShortName: "Yazmin",
    quinceaneraAge: 15,
    motherName: "María del Carmen Servín Hernández",
    fatherName: "José García",
    dressColor: "#D4AF37", // Dorado

    // Información del evento
    eventDate: "22 de Noviembre de 2025",
    eventDateISO: "2025-11-22",

    // Ceremonia religiosa
    ceremonyLocation: "Proyecto Niños Don Bosco",
    ceremonyAddress: "San Juan Crisóstomo 1102, Plan de Ayala, 37490 León de los Aldama, Gto.",
    ceremonyCity: "León de los Aldama, Guanajuato",
    ceremonyTime: "1:00 PM",
    ceremonyHour: 13,
    ceremonyMinute: 0,
    ceremonyMapsUrl: "https://maps.app.goo.gl/F3G4sy1gMSffYqqH7",

    // Fiesta
    partyLocation: "Salón de Fiestas Memo",
    partyAddress: "SAPAL, 37666 Plan de Ayala, Gto.",
    partyDistance: "Al terminar la ceremonia",
    partyStartTime: "3:00 PM",
    partyStartHour: 15,
    partyStartMinute: 0,
    partyEndTime: "10:00 PM",
    partyEndHour: 22,
    partyEndMinute: 0,
    partyMapsUrl: "https://maps.app.goo.gl/KXTDK7go4oGTwHrj8",

    // Sesión de fotos
    photoSession: {
        date: "19 de Noviembre de 2025",
        dateISO: "2025-11-19",
        time: "3:00 PM",
        location: "Expiatorio",
        cost: 2500,
        currency: "MXN"
    },

    // Padrinos
    padrinos: {
        misa: {
            names: "Por confirmar",
            type: "Padrinos de Misa"
        },
        corona: {
            name: "Por confirmar",
            type: "Madrina de Corona"
        },
        brindis: {
            name: "Por confirmar",
            type: "Madrina de Brindis"
        },
        muneca: {
            name: "Por confirmar",
            type: "Padrino de Muñeca"
        },
        regalo: {
            name: "Por confirmar",
            type: "Madrina de Regalo Sorpresa"
        }
    },

    // Música
    backgroundMusic: {
        enabled: true,
        songName: "La petite fille de la mer (Remastered)",
        songUrl: "" // Se agregará el archivo de audio
    },

    // Entretenimiento
    entertainment: [
        {
            type: "Comida",
            startTime: "3:30 PM",
            endTime: "5:30 PM",
            icon: "🍽️"
        },
        {
            type: "Vals de la Quinceañera",
            startTime: "5:30 PM",
            endTime: "6:00 PM",
            icon: "💃"
        },
        {
            type: "Grupo Musical",
            startTime: "7:00 PM",
            endTime: "10:00 PM",
            icon: "🎵"
        },
        {
            type: "Sonido",
            startTime: "3:00 PM",
            endTime: "10:00 PM",
            icon: "🎶"
        }
    ],

    // Paquete fotográfico
    package: {
        name: "PAQUETE COMPLETO DE FOTOGRAFÍA, VIDEO, DRON E INVITACIÓN WEB",
        price: 6000,
        drone: 500,
        viatics: 500,
        webInvitation: 500,
        currency: "MXN",
        includes: [
            "Cobertura por Sesión, Misa y 5 horas de Fiesta",
            "100 Fotos del Evento Impresas en Tamaño 5x7 Pulgadas",
            "1 Película USB EN 4K con duración de 3:00 hrs editada musicalizada y titulada 📹",
            "1 Videoclip para Proyectar en el salón + fotos del recuerdo",
            "Cobertura con Dron 4K - Videos aéreos de la ceremonia y fiesta 🚁",
            "Invitación Web Personalizada - Sitio elegante para compartir 🌐",
            "1 Caja Impresa para la USB",
            "1 Foto Ampliada A 50x60 cm con Marco",
            "1 Caja Impresa para Las Fotografías",
            "1 Sesión de Fotografías antes del Evento"
        ]
    },

    // Pagos
    payments: {
        subtotal: 7500,
        deposit: 2000,
        balance: 5500,
        currency: "MXN"
    },

    // Información de contacto
    contact: {
        photographer: "Mamá - Elida",
        phone: "+52 418 145 4596",
        phoneWhatsApp: "+52 418 145 4596",
        phoneSecondary: "+52 899 679 6555",
        email: "",
        website: "",
        responseTime: "24 horas",
        dressCode: "Elegante"
    },

    // Colores personalizados
    colors: {
        gold: "#D4AF37",
        darkGold: "#DAA520",
        lightGold: "#FFD700",
        darkBg: "#1a1a1a",
        textDark: "#333",
        textLight: "#f5f5f5"
    },

    // Términos y condiciones
    terms: {
        deposit: "50%",
        depositDueDate: "Al momento de firmar",
        balanceDueDate: "7 días antes del evento",
        deliveryDays: 30,
        sessionPreEventDays: "A acordar",
        cancellationPolicy: {
            moreThan30Days: "80% de reembolso",
            between15And30Days: "50% de reembolso",
            lessThan15Days: "Sin reembolso"
        }
    }
};

// Función auxiliar para obtener valor de configuración
function getConfig(key) {
    const keys = key.split('.');
    let value = EVENT_CONFIG;
    for (let k of keys) {
        value = value[k];
    }
    return value;
}

// Función para actualizar configuración
function updateConfig(key, value) {
    const keys = key.split('.');
    let obj = EVENT_CONFIG;
    for (let i = 0; i < keys.length - 1; i++) {
        obj = obj[keys[i]];
    }
    obj[keys[keys.length - 1]] = value;
}

// Función para exportar configuración
function exportConfig() {
    return JSON.stringify(EVENT_CONFIG, null, 2);
}

// Función para importar configuración
function importConfig(jsonString) {
    try {
        const imported = JSON.parse(jsonString);
        Object.assign(EVENT_CONFIG, imported);
        console.log("Configuración importada exitosamente");
        return true;
    } catch (error) {
        console.error("Error al importar configuración:", error);
        return false;
    }
}

console.log("Configuración del evento cargada correctamente");
console.log("XV Años de", EVENT_CONFIG.quinceaneraName);
console.log("Sesión fotográfica:", EVENT_CONFIG.photoSession.date, "a las", EVENT_CONFIG.photoSession.time, "en", EVENT_CONFIG.photoSession.location);
