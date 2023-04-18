#include <iostream>
#include <vector>

using namespace std;

void bubble_sort(vector<int>& arr) {
    
    for (int i = 0; i < arr.size(); ++i) {
        bool swapped = false;
        for (int j = 0; j < arr.size() - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }

    cout << "Sorted array: ";
    for (int& elem : arr) {
        cout << elem << ' ';
    }

    return;
}

int main()
{
    cout << "Enter array size: ";
    int arr_size;
    cin >> arr_size;

    vector<int> arr(arr_size);
    cout << "Enter array: ";
    for (int i = 0; i < arr_size; ++i) {
        cin >> arr[i];
    }

    bubble_sort(arr);

    return 0;
}
