#include <iostream>
#include <string>
using namespace std;

/**
 * Рекурсивная функция для переворота строки
 * @param str - исходная строка
 * @return перевернутая строка
 */
string reverseString(const string& str) {
    // Базовый случай: пустая строка или один символ
    if (str.length() <= 1) {
        return str;
    }
    
    // Рекурсивный случай: последний символ + реверс оставшейся части
    return str[str.length() - 1] + reverseString(str.substr(0, str.length() - 1));
}

/**
 * Альтернативная реализация с использованием индексов
 */
string reverseStringIndex(const string& str, int index) {
    // Базовый случай: дошли до начала строки
    if (index < 0) {
        return "";
    }
    
    // Рекурсивный случай: текущий символ + реверс предыдущей части
    return str[index] + reverseStringIndex(str, index - 1);
}

/**
 * Эффективная реализация с двумя указателями
 */
string reverseStringEfficient(const string& str, int left, int right) {
    // Базовый случай: пересекли указатели
    if (left >= right) {
        return str;
    }
    
    // Создаем копию строки для модификации
