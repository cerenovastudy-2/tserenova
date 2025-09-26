#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int count = 0;
    while (n > 0) {
        if (n % 2 == 1) // если младший бит равен 1
            count++;
        n /= 2; // делим на 2
    }

    cout << count << endl;
    return 0;
}
