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

void mad_lib(){
  string color, plural_noun, celebrity;
  cout << "enter a color:" << endl;
  cin >> color;
  cout << "enter a plural noun:" << endl;
  cin >> plural_noun;
  cout << "enter a celebrity:" << endl;
  cin >> celebrity;
  
  cout << "Roses are "<< color << endl;
  cout << "Mountains are "<< plural_noun << endl;
  cout << "I love "<< celebrity << "!" << endl; 
}

void arrs(){
  int arr [] = {};
  arr[0] = 1;
  cout << arr[0] << endl;
}

// int factorial(int num){
//   int result = 1;
//   while (num >= 1){
//     result *= num;
//     num --;
//   } 
// }

void calculator(){
    float num1, num2, res;
    string op;
    cout << "Num1:" << endl;
    cin >> num1;
    cout << "op:" << endl;
    cin >> op;
    cout << "Num2:" << endl;
    cin >> num2;


    if (op == "+"){
      cout << num1 + num2 << endl;
    }
    else if (op == "-"){
      cout << num1 - num2 << endl;
    }
    else if (op == "*"){
      cout << num1 * num2 << endl;
    }
    else if (op == "/"){
      cout << num1 / num2 << endl;
    }
    else{
      cout << "input not expected!" << endl;
    }
  }

  // int pow(int base, int pow){
  //   int res = 1;
  //   for (int i = 0; i < pow; i++){
  //     res *= base;
  //   }
  //   return res;
  // }

  void arr_2d (){
    int number_grid [3][2] = {{1,2},{3,4},{5,6}};
    cout << number_grid[1][0] << endl;
  }

int main(){
  // numbers();
  // numbers();
  // input();
  // mad_lib();
  // arrs();
  // cout << factorial(4) << endl;
  // calculator();
  // cout << pow(2,3) << endl;
  // arr_2d();

  return 0;
}