#include <iostream>
#include <cmath>
using namespace std;
 
// Main() function: where the execution of program begins
void strings(){
    // prints hello world
  string phrase = "aFarzan";
  string part = "Far";
  cout << phrase.find(part) << endl;
  cout << phrase.substr(0,3) << endl ;
}

void numbers(){
  float num = 8.99;
  cout << floor(num) << endl;
}

void input(){
  int age;
  cin >> age;
  cout << "you are " << age << " years old" << endl ;
}
int main(){
  // numbers();
  // numbers();
  input();
}