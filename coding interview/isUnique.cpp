#include<iostream>

using namespace std;

bool isUnique(string);

int main() {
    string s = "abcde";
    cout << isUnique(s) << endl;

    s = "abcda";
    cout << isUnique(s) << endl;
}

bool isUnique(string s){
    if (s.length() > 128) return false;

    bool chars[128] = {false};

    for(int i = 0; i < s.length(); i++){
        int val = s[i];
        cout << val << endl;
        if (chars[val]){
            return false;
        }
        chars[val] = true;
    }
    return true;

}