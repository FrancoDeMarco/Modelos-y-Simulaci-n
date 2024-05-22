const { ChartJSNodeCanvas } = require('chartjs-node-canvas');
const fs = require('fs');

// Función para generar números aleatorios con una distribución uniforme
function randomWithDistribution(minValue, maxValue, exponent) {
    const random_number = Math.random(); // Generar un número aleatorio entre 0 y 1
    const scaled_number = minValue + random_number * (maxValue - minValue);
    const distributed_number = Math.pow(scaled_number, exponent);
    return Math.round(distributed_number);
}

// Lista para almacenar los valores generados aleatoriamente
const randomValues = [];

// Generar y almacenar 100 números aleatorios entre 1 y 100 siguiendo una distribución uniforme
for (let i = 0; i < 100; i++) {
    const randomValue = randomWithDistribution(1, 100, 1);
    randomValues.push(randomValue);
    console.log('Número', i + 1, ':', randomValue);
}

// MEDIA
// Calcular la media de los valores generados
const media = randomValues.reduce((acc, val) => acc + val, 0) / randomValues.length;
console.log(`La media de los números generados es: ${media.toFixed(2)}`);

// VARIANZA
// Calcular la varianza
const varianza = randomValues.reduce((acc, val) => acc + Math.pow(val - media, 2), 0) / randomValues.length;
console.log(`La varianza de los números generados es: ${varianza.toFixed(2)}`);

// DESVÍO ESTÁNDAR
// Calcular el desvío estándar
const desvioEstandar = Math.sqrt(varianza);
console.log(`El desvío estándar de los números generados es: ${desvioEstandar.toFixed(2)}`);

// GRÁFICO
// Configurar Chart.js-node
const width = 800; // Ancho del gráfico
const height = 600; // Alto del gráfico

const chartCallback = (ChartJS) => {
    // Asignar los valores por defecto de Chart.js
    ChartJS.defaults.font.family = 'Arial';
    ChartJS.defaults.font.size = 16;
};

// Crear instancia de ChartJSNodeCanvas
const chartNode = new ChartJSNodeCanvas({ width, height, chartCallback });

// Crear datos para el gráfico
const data = {
    labels: randomValues.map((val, index) => index + 1),
    datasets: [{
        label: 'Valor',
        data: randomValues,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

const config = {
    type: 'bar',
    data: data,
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Índice'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Valor'
                }
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Distribución uniforme de números generados'
            }
        }
    }
};

// Generar el gráfico
chartNode.renderToBuffer(config)
    .then(buffer => {
        // Guardar la imagen en un archivo
        fs.writeFileSync('output.png', buffer);
        console.log('Gráfico generado con éxito.');
    })
    .catch((error) => {
        console.error(error);
    });