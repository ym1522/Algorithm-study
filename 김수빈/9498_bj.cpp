#include <iostream>
#include <stdio.h>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    int score;
    char grade;
    scanf_s("%d", &score);

    if (score >= 90) {
        grade = 'A';
    }
    else if (score >= 80) {
        grade = 'B';
    }
    else if (score >= 70) {
        grade = 'C';
    }
    else if (score >= 60) {
        grade = 'D';
    }
    else {
        grade = 'F';
    }
    cout << grade << "\n";
    return 0;
}