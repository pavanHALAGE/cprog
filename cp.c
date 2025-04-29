#include <stdio.h>

int main() {
    int num1, num2;

    printf("Enter two integers:\n");
    scanf("%d %d", &num1, &num2);

    
    if (num1 % 2 == 0)
        printf("%d is Even\n", num1);
 else
        printf("%d is Odd\n", num1);



