// Функция для вычисления расстояния Левенштейна
function levenshteinDistance(a, b) {
    const matrix = Array.from({ length: a.length + 1 }, () => Array(b.length + 1).fill(0));

    for (let i = 0; i <= a.length; i++) {
        matrix[i][0] = i;
    }
    for (let j = 0; j <= b.length; j++) {
        matrix[0][j] = j;
    }

    for (let i = 1; i <= a.length; i++) {
        for (let j = 1; j <= b.length; j++) {
            const cost = a[i - 1] === b[j - 1] ? 0 : 1;
            matrix[i][j] = Math.min(
                matrix[i - 1][j] + 1, // Удаление
                matrix[i][j - 1] + 1, // Вставка
                matrix[i - 1][j - 1] + cost // Замена
            );
        }
    }

    return matrix[a.length][b.length];
}

// Функция для вычисления расстояния Дамерау-Левенштейна
function damerauLevenshteinDistance(a, b) {
    const matrix = Array.from({ length: a.length + 1 }, () => Array(b.length + 1).fill(0));

    for (let i = 0; i <= a.length; i++) {
        matrix[i][0] = i;
    }
    for (let j = 0; j <= b.length; j++) {
        matrix[0][j] = j;
    }

    for (let i = 1; i <= a.length; i++) {
        for (let j = 1; j <= b.length; j++) {
            const cost = a[i - 1] === b[j - 1] ? 0 : 1;
            matrix[i][j] = Math.min(
                matrix[i - 1][j] + 1, // Удаление
                matrix[i][j - 1] + 1, // Вставка
                matrix[i - 1][j - 1] + cost // Замена
            );

            if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
                matrix[i][j] = Math.min(matrix[i][j], matrix[i - 2][j - 2] + cost); // Транспозиция
            }
        }
    }

    return matrix[a.length][b.length];
}

// Функция для вычисления расстояния Хемминга
function hammingDistance(a, b) {
    if (a.length !== b.length) {
        throw new Error("Слова должны быть одинаковой длины для расстояния Хемминга");
    }

    let distance = 0;
    for (let i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) {
            distance++;
        }
    }
    return distance;
}

// Список пар слов
const wordPairs = [
    ["Марта", "Карта"],
    ["Карета", "Карат"],
    ["Маэстро", "Мастер"],
    ["Порт", "Ропот"],
    ["Арт", "Рать"]
];

// Вычисление расстояний для каждой пары
wordPairs.forEach(([word1, word2]) => {
    console.log(`Слова: "${word1}" и "${word2}"`);
    console.log(`Расстояние Левенштейна: ${levenshteinDistance(word1, word2)}`);
    console.log(`Расстояние Дамерау-Левенштейна: ${damerauLevenshteinDistance(word1, word2)}`);
    try {
        console.log(`Расстояние Хемминга: ${hammingDistance(word1, word2)}`);
    } catch (error) {
        console.log(`Расстояние Хемминга: ${error.message}`);
    }
    console.log("-----------------------------");
});