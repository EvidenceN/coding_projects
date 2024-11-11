#include <stdio.h>
#include <stdbool.h>

int divide(int a, int b, bool *d) {
  int c = a / b;

  if (c * b == a) {
    *(d) = true;
  } else {
    *(d) = false;
  }
  return c;
}

int numerator = 10;
int denominator = 5;
bool divisible;

int main() {
  int result = divide(numerator, denominator, &divisible);

  printf("%d", result);

  return 0;
}