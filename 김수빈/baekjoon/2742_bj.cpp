#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    string output = "";
    cin >> n;
    for (int i = n; i > 0; i--) {
        output += to_string(i) + "\n";
    }
    cout << output << endl;
}
