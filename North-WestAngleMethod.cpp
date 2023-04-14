#include <iostream>
#include <vector>

using namespace std;

// arrays of suppliers and consumers
vector<int> A;
vector<int> B;
// arrays to mark used suppliers or consumers
vector<bool> used_A;
vector<bool> used_B;
// amount of consumers and suppliers
int n_A;
int n_B;
// matrix with prices cij
vector<vector<pair<int, int>>> matrix;

void print_matrix() {
    for (int i = 0; i < n_A; i++) {
        for (int j = 0; j < n_B; j++) {
            cout << matrix[i][j].first << "|" << matrix[i][j].second << ' ';
        }
        cout << endl;
    }
}

// delete supplier from table
void cross_row(int row_number) {
    used_A[row_number] = true;
    for (int i = 0; i < n_B; i++) {
        if(matrix[row_number][i].second == -1) matrix[row_number][i].second = 0;
    }
}

// delete consumer from table
void cross_column(int column_number) {
    used_B[column_number] = true;
    for (int i = 0; i < n_A; i++) {
        if (matrix[i][column_number].second == -1) matrix[i][column_number].second = 0;
    }
}

// find new coordinates of north-west angle
pair<int, int> find_next_start() {
    int ai, bj;

    for (int i = 0; i < n_A; i++) {
        if (!used_A[i]) {
            ai = i;
            break;
        }
    }

    for (int j = 0; j < n_B; j++) {
        if (!used_B[j]) {
            bj = j;
            break;
        }
    }

    return { ai, bj };
}


int main()
{
    int sum_A = 0, sum_B = 0; // check if type open/closed

    cout << "Enter the size of A array: ";
    cin >> n_A;
    cout << "\nEnter A array(separate with ' '): ";
    
    for (int i = 0; i < n_A; ++i) {
        int temp;
        cin >> temp;
        A.push_back(temp);
        sum_A += temp;
    }

    cout << "\nEnter the size of B array: ";
    cin >> n_B;
    cout << "\nEnter B array(separate with ' '): ";

    for (int i = 0; i < n_B; ++i) {
        int temp;
        cin >> temp;
        B.push_back(temp);
        sum_B += temp;
    }

    matrix.resize(n_A);

    cout << "Enter price matrix(separate elements in a row with ' ' and rows with Enter): \n";
    for (int i = 0; i < n_A; i++) {
        for (int j = 0; j < n_B; j++) {
            int temp;
            cin >> temp;
            matrix[i].push_back({ temp, -1 });
        }
    }

    print_matrix();

    if (sum_A > sum_B) {
        cout << "Type was: open; sumA = " << sum_A << "; sumB = " << sum_B << "; now type: closed\n";
        B.push_back(abs(sum_A - sum_B));
        n_B++;
        for (int i = 0; i < n_A; i++) {
            matrix[i].push_back({ 0, -1 });
        }
    }
    else if (sum_A < sum_B) {
        cout << "Type was: open; sumA = " << sum_A << "; sumB = " << sum_B << "; now type: closed\n";
        A.push_back(abs(sum_B - sum_A));
        n_A++;
        vector<pair<int, int>> add;
        for (int i = 0; i < n_B; i++) {
            add.push_back({ 0, -1 });
        }
        matrix.push_back(add);
    }
    else {
        cout << "Type: closed\n";
    }

    print_matrix();

    used_A.resize(n_A);
    used_B.resize(n_B);

    //зробимо наразі всі вершини невідвіданими
    for (int i = 0; i < n_A; i++) {
        used_A.push_back(false);
    }
    for (int i = 0; i < n_A; i++) {
        used_B.push_back(false);
    }
    
    for (int iter = 0; iter < n_A + n_B - 1; iter++) {
        int min_row = find_next_start().first;
        int min_column = find_next_start().second;

        if (A[min_row] >= B[min_column]) {
            matrix[min_row][min_column].second = B[min_column];
            A[min_row] -= B[min_column];
            cross_column(min_column);
        }
        else if (A[min_row] < B[min_column]) {
            matrix[min_row][min_column].second = A[min_row];
            B[min_column] -= A[min_row];
            cross_row(min_row);
        }
    }
    cout << endl;
    print_matrix();

    // порахуємо значення цільової функції для першого опорного плану
    int fx = 0;
    for (int i = 0; i < n_A; i++) {
        for (int j = 0; j < n_B; j++) {
            fx += matrix[i][j].first * matrix[i][j].second;
        }
    }
    cout << "\nF(x) = " << fx;
    return 0;
}
/*
the output is given in cij|xij form
*/