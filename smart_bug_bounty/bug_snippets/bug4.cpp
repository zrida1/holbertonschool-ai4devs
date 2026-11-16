#include <iostream>
#include <vector>
using namespace std;

double calculateAverage(const vector<int>& numbers) {
    if (numbers.empty()) {
        return 0;
    }

    int sum = 0;

    for (int number : numbers) {
        sum += number;
    }

    return sum / numbers.size();
}

int main() {
    vector<int> numbers = {10, 20, 25};

    cout << "Average: " << calculateAverage(numbers) << endl;

    return 0;
}