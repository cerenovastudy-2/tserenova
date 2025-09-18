// Массивы 
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Статический массив
    int staticArray[5] = {1, 2, 3, 4, 5};
    
    // Динамический массив (вектор)
    vector<int> dynamicArray = {1, 2, 3, 4, 5};
    
    // Добавление элемента
    dynamicArray.push_back(6);
    
    // Доступ к элементам
    cout << "Element at index 2: " << dynamicArray[2] << endl;
    
    // Размер массива
    cout << "Array size: " << dynamicArray.size() << endl;
    
    return 0;
}
// Стеки
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> st;
    
    // Добавление элементов
    st.push(1);
    st.push(2);
    st.push(3);
    
    // Просмотр верхнего элемента
    cout << "Top element: " << st.top() << endl;
    
    // Удаление элемента
    st.pop();
    
    // Проверка на пустоту
    cout << "Is empty: " << st.empty() << endl;
    
    // Размер стека
    cout << "Stack size: " << st.size() << endl;
    
    return 0;
}