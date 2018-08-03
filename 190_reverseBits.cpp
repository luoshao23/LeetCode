#include <iostream>
#include <cmath>

using namespace std;

int reversedBits(int n){
    int d = 32;
    int res = 0;
    while (n){
        res += n % 2 * 1 << --d;
        n /= 2;
    }
    return res;
}

int main(){

    cout << reversedBits(64) << endl;
    return 0;
}