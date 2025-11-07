public class StringReverse {
    
    /**
     * Рекурсивная функция для переворота строки
     * @param str - исходная строка
     * @return перевернутая строка
     */
    public static String reverseString(String str) {
        // Базовый случай: пустая строка или один символ
        if (str == null || str.length() <= 1) {
            return str;
        }
        
        // Рекурсивный случай: последний символ + реверс оставшейся части
        return str.charAt(str.length() - 1) + reverseString(str.substring(0, str.length() - 1));
    }
    
    /**
     * Альтернативная реализация с использованием индексов
     */
    public static String reverseStringIndex(String str, int index) {
        // Базовый случай: дошли до начала строки
        if (index < 0) {
            return "";
        }
        
        // Рекурсивный случай: текущий символ + реверс предыдущей части
        return str.charAt(index) + reverseStringIndex(str, index - 1);
    }
    
    public static void main(String[] args) {
        String[] testCases = {"hello", "algorithm", "recursion", "a", ""};
        
        System.out.println("=== Рекурсивный реверс строки ===");
        
        for (String test : testCases) {
            String reversed = reverseString(test);
            System.out.println("Исходная: \"" + test + "\" -> Перевернутая: \"" + reversed + "\"");
        }
        
        System.out.println("\n=== Альтернативная реализация ===");
        for (String test : testCases) {
            String reversed = reverseStringIndex(test, test.length() - 1);
            System.out.println("Исходная: \"" + test + "\" -> Перевернутая: \"" + reversed + "\"");
        }
        
        // Анализ работы на примере "hello"
        System.out.println("\n=== Анализ рекурсии для 'hello' ===");
        analyzeReverse("hello");
    }
    
    /**
     * Метод для анализа шагов рекурсии
     */
    public static void analyzeReverse(String str) {
        if (str.length() <= 1) {
            System.out.println("Базовый случай: возвращаем \"" + str + "\"");
            return;
        }
        
        char lastChar = str.charAt(str.length() - 1);
        String remaining = str.substring(0, str.length() - 1);
        
        System.out.println("Рекурсивный вызов: '" + lastChar + "' + reverse(\"" + remaining + "\")");
        analyzeReverse(remaining);
        System.out.println("Возврат: '" + lastChar + "' + результат от \"" + remaining + "\"");
    }
}
