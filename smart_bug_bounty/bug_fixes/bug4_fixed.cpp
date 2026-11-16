#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

double calculateAverage(const vector<int>& numbers) {
    if (numbers.empty()) {
        return 0.0;
    }
    int sum = 0;
    for (int number : numbers) {
        sum += number;
    }
    return static_cast<double>(sum) / numbers.size();
}

int main() {
    vector<int> numbers = {10, 20, 25};
    assert(calculateAverage(numbers) > 18.33 &&
           calculateAverage(numbers) < 18.34);
    assert(calculateAverage({10, 20}) == 15.0);
    assert(calculateAverage({5}) == 5.0);
    assert(calculateAverage({}) == 0.0);
    cout << "All C++ tests passed." << endl;
    return 0;
}