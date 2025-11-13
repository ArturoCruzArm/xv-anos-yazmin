// Configuración del evento - XV Años de Geraldine Guadalupe
// Edita estos valores para personalizar la invitación y contrato

const EVENT_CONFIG = {
    // Información de la quinceañera
    quinceaneraName: "Geraldine Guadalupe Méndez Villegas",
    quinceaneraShortName: "Geral",
    quinceaneraAge: 15,
    motherName: "Elida Villegas Hernández",
    fatherName: "José Víctor Manuel Méndez Rayas",
    dressColor: "#D4AF37", // Dorado

    // Información del evento
    eventDate: "31 de Diciembre de 2025",
    eventDateISO: "2025-12-31",

    // Ceremonia religiosa
    ceremonyLocation: "Parroquia de Nuestra Señora de los Dolores",
    ceremonyAddress: "Calle Querétaro 1, Centro, 37800 Dolores Hidalgo Cuna de la Independencia Nacional, Gto., México",
    ceremonyCity: "Dolores Hidalgo, Guanajuato",
    ceremonyTime: "2:00 PM",
    ceremonyHour: 14,
    ceremonyMinute: 0,
    ceremonyMapsUrl: "https://maps.google.com/?q=Parroquia+de+Nuestra+Señora+de+los+Dolores,Calle+Querétaro+1,Centro,37800+Dolores+Hidalgo",

    // Fiesta
    partyLocation: "Jardín de la Aurora",
    partyAddress: "Prolongación Baja California Norte 61, Centro, 37800 Dolores Hidalgo Cuna de la Independencia Nacional, Gto., México",
    partyDistance: "A 5 minutos de la Parroquia",
    partyStartTime: "4:00 PM",
    partyStartHour: 16,
    partyStartMinute: 0,
    partyEndTime: "11:00 PM",
    partyEndHour: 23,
    partyEndMinute: 0,
    partyMapsUrl: "https://maps.google.com/?q=Jardín+de+la+Aurora,Prolongación+Baja+California+Norte+61,Centro,37800+Dolores+Hidalgo",

    // Padrinos
    padrinos: {
        misa: {
            names: "Amapola Cortez y Moisés Leon",
            type: "Padrinos de Misa"
        },
        corona: {
            name: "Elizabeth Juárez",
            type: "Madrina de Corona"
        },
        brindis: {
            name: "Diana Villegas",
            type: "Madrina de Brindis"
        },
        muneca: {
            name: "Jesús Méndez",
            type: "Padrino de Muñeca"
        },
        regalo: {
            name: "Areli Juárez",
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
            type: "Tecladista",
            startTime: "5:00 PM",
            endTime: "6:00 PM",
            icon: "🎹"
        },
        {
            type: "Sonido Fiesta Loca",
            startTime: "6:00 PM",
            endTime: "11:00 PM",
            icon: "🎵"
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
