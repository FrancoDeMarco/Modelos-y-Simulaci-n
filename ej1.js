// Genera números aleatorios con dos decimales como máximo.
function generateRandomDecimalInRangeFormatted(min, max, places) {
    let value = (Math.random() * (max - min)) + min; // Eliminar +1 del max - min
    return Number.parseFloat(value.toFixed(places)); // Aplicar toFixed antes de convertir a número
}

// Array para almacenar los valores generados aleatoriamente
let randomValues = [];

// Generar y almacenar 100 números decimales aleatorios entre 2.5 y 10.75
for (let i = 0; i < 100; i++) {
    let randomValue = generateRandomDecimalInRangeFormatted(2.5, 10.75, 2); // Ajustar el rango y las decimales
    randomValues.push(randomValue);
    console.log('Número', i + 1, ':', randomValue);
}


//MEDIA
// Calcular la media de los valores generados
let suma = 0; // Inicializar la suma
for (let i = 0; i < randomValues.length; i++) {
    suma += randomValues[i]; // Sumar cada valor al acumulador
}
let media = suma / randomValues.length; // Calcular la media
console.log('Media:', media.toFixed(2));


//DESVÍO ESTÁNDAR
// Función para calcular el desvío estándar
function calcularDesvioEstandar(valores, media) {
    let sumaCuadradosDiferencias = 0;
    for (let i = 0; i < valores.length; i++) {
        sumaCuadradosDiferencias += Math.pow(valores[i] - media, 2);
    }
    let varianza = sumaCuadradosDiferencias / valores.length;
    return Math.sqrt(varianza);
}

// Calcular el desvío estándar
let desvioEstandar = calcularDesvioEstandar(randomValues, media);
console.log('Desvío estándar:', desvioEstandar.toFixed(2));


// VARIANZA
let varianza = desvioEstandar ** 2;
console.log('Varianza:', varianza.toFixed(2));


//GRÁFICOS
// Función para generar una cadena de caracteres de longitud proporcionada
function generateBar(length) {
    let bar = '';
    for (let i = 0; i < length; i++) {
        bar += '|';
    }
    return bar;
}

// Función para mostrar los valores en forma de gráfico de barras
function displayGraph(values) {
    const maxValue = Math.max(...values);
    const scaleFactor = 50 / maxValue; // Escalar los valores para que quepan en una línea de 50 caracteres

    console.log('Gráfico de los valores generados:');
    for (let i = 0; i < values.length; i++) {
        const barLength = Math.round(values[i] * scaleFactor);
        console.log(generateBar(barLength));
    }
}

// Mostrar el gráfico de barras de los valores generados
displayGraph(randomValues);
