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

3. Python реализация
def reverse_string(s):
    """
    Рекурсивная функция для переворота строки
    Args:
        s: исходная строка
    Returns:
        перевернутая строка
    """
    # Базовый случай: пустая строка или один символ
    if len(s) <= 1:
        return s
    
    # Рекурсивный случай: последний символ + реверс оставшейся части
    return s[-1] + reverse_string(s[:-1])

def reverse_string_index(s, index):
    """
    Альтернативная реализация с использованием индексов
    Args:
        s: исходная строка
        index: текущий индекс
    Returns:
        перевернутая строка
    """
    # Базовый случай: дошли до начала строки
    if index < 0:
        return ""
    
    # Рекурсивный случай: текущий символ + реверс предыдущей части
    return s[index] + reverse_string_index(s, index - 1)

def reverse_string_efficient(s, left, right):
    """
    Эффективная реализация с двумя указателями
    Args:
        s: исходная строка
        left: левый индекс
        right: правый индекс
    Returns:
        перевернутая строка
    """
    # Базовый случай: пересекли указатели
    if left >= right:
        return s
    
    # Преобразуем в список для модификации
    chars = list(s)
    
    # Меняем симметричные символы местами
    chars[left], chars[right] = chars[right], chars[left]
    
    # Рекурсивно обрабатываем подстроку
    return reverse_string_efficient(''.join(chars), left + 1, right - 1)

def analyze_reverse(s, depth=0):
    """
    Метод для анализа шагов рекурсии
    """
    indent = "  " * depth
    print(f"{indent}Вызов: reverse_string('{s}')")
    
    if len(s) <= 1:
        print(f"{indent}Базовый случай: возвращаем '{s}'")
        return s
    
    last_char = s[-1]
    remaining = s[:-1]
    
    print(f"{indent}Рекурсивный вызов: '{last_char}' + reverse_string('{remaining}')")
    result = last_char + analyze_reverse(remaining, depth + 1)
    print(f"{indent}Возврат: '{last_char}' + результат от '{remaining}' = '{result}'")
    
    return result

if __name__ == "__main__":
    test_cases = ["hello", "algorithm", "recursion", "a", ""]
    
    print("=== Рекурсивный реверс строки ===")
    
    for test in test_cases:
        reversed_str = reverse_string(test)
        print(f"Исходная: '{test}' -> Перевернутая: '{reversed_str}'")
    
    print("\n=== Альтернативная реализация ===")
    for test in test_cases:
        reversed_str = reverse_string_index(test, len(test) - 1)
        print(f"Исходная: '{test}' -> Перевернутая: '{reversed_str}'")
    
    print("\n=== Эффективная реализация ===")
    for test in test_cases:
        reversed_str = reverse_string_efficient(test, 0, len(test) - 1)
        print(f"Исходная: '{test}' -> Перевернутая: '{reversed_str}'")
    
    print("\n=== Анализ рекурсии для 'hello' ===")
    analyze_reverse("hello")

🔍 Анализ алгоритма

Принцип работы
