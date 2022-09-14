#include <iostream>

int main() {
  int input1{0};
  std::string input2{""};
  std::cout << "Please enter input 1: ";
  std::cin >> input1;
  std::cout << "Please enter input 2: ";
  std::cin >> input2;
  std::cout << "Input 1: " << input1 << "\n";
  std::cout << "Input 2: " << input2 << "";
  return 0;
}
