#include <iostream>
#include <vector>

using namespace std;

void insertion_sort(vector<int>& arr) {

    for (int i = 1; i < arr.size(); ++i) {
        int j = i - 1;
        int key_elem = arr[i];

        while (j >= 0 && arr[j] > key_elem) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key_elem;
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

    insertion_sort(arr);

    return 0;
}
