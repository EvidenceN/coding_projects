#include <stdio.h>

void max(int x, int y) {
  if (x > y)
    printf("%d is the bigger number\n", x);
  else
    printf("%d is the bigger number\n", y);
}

int main() {
  int a = 20;
  int b = 30;

  max(a, b);

  return 0;
}