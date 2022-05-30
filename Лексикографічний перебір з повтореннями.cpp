#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

//функція, яка повертає trueБ якщо стрічка mainstr виконала свою роботу і тепер складається тільки з максимальних значень у кожному розряді
bool CheckEnding(string mainstr, string check) {
    string temp = mainstr;
    sort(temp.begin(), temp.end());
    return includes(check.begin(), check.end(), temp.begin(), temp.end());
}

int main() {
    //змінна maxNumber це максимальне число для кожного з розрядів
    //змінна amountOfDigits це кількість розрядів в числі
    int maxNumber, amountOfDigits;
    cin >> maxNumber >> amountOfDigits;

    string mainstr;
    string check;

    //заповнюємо початкову стрічку значеннями "1", а стрічку для перевірки "maxNumber" для кожного розряду
    for (int i = 0; i < amountOfDigits; i++) {
        mainstr += to_string(1);
        check += to_string(maxNumber);
    }

    cout << mainstr << endl;

    while (!CheckEnding(mainstr, check)) {

        for (int i = mainstr.size() - 1; i >= 0; i--) {
            if (mainstr[i] == maxNumber + '0') mainstr[i] = '1';
            else {
                mainstr[i] ++;
                cout << mainstr << endl;
                break;
            }
        }
    }
    return 0;
}