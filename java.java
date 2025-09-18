// Массивы 
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Статический массив
        int[] staticArr = {1, 2, 3, 4, 5};
        
        // Динамический массив (ArrayList)
        ArrayList<Integer> dynamicArr = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        // Добавление элемента
        dynamicArr.add(6);
        
        // Доступ к элементам
        System.out.println("Element at index 2: " + dynamicArr.get(2));
        
        // Размер массива
        System.out.println("Array size: " + dynamicArr.size());
    }
}
// Стеки
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        
        // Добавление элементов
        stack.push(1);
        stack.push(2);
        stack.push(3);
        
        // Просмотр верхнего элемента
        System.out.println("Top element: " + stack.peek());
        
        // Удаление элемента
        stack.pop();
        
        // Проверка на пустоту
        System.out.println("Is empty: " + stack.empty());
        
        // Размер стека
        System.out.println("Stack size: " + stack.size());
    }
}



