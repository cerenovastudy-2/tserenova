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
string result = str;
    
    // Меняем симметричные символы местами
    swap(result[left], result[right]);
    
    // Рекурсивно обрабатываем подстроку
    return reverseStringEfficient(result, left + 1, right - 1);
}

int main() {
    string testCases[] = {"hello", "algorithm", "recursion", "a", ""};
    
    cout << "=== Рекурсивный реверс строки ===" << endl;
    
    for (const string& test : testCases) {
        string reversed = reverseString(test);
        cout << "Исходная: \"" << test << "\" -> Перевернутая: \"" << reversed << "\"" << endl;
    }
    
    cout << "\n=== Альтернативная реализация ===" << endl;
    for (const string& test : testCases) {
        string reversed = reverseStringIndex(test, test.length() - 1);
        cout << "Исходная: \"" << test << "\" -> Перевернутая: \"" << reversed << "\"" << endl;
    }
    
    cout << "\n=== Эффективная реализация ===" << endl;
    for (const string& test : testCases) {
        string reversed = reverseStringEfficient(test, 0, test.length() - 1);
        cout << "Исходная: \"" << test << "\" -> Перевернутая: \"" << reversed << "\"" << endl;
    }
    
    return 0;
}

