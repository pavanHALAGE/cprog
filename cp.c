#include <stdio.h>

int main() {
    int num1, num2;

    printf("Enter two integers:\n");
    scanf("%d %d", &num1, &num2);

    
    if (num1 % 2 == 0)
        printf("%d is Even\n", num1);
 else
        printf("%d is Odd\n", num1);
 

 if (num2 % 2 == 0)
        printf("%d is Even\n", num2);
 else
        printf("%d is Odd\n", num2);

if (num1 > num2) {
        printf("Largest: %d\n", num1);
        printf("Smallest: %d\n", num2);

} else if (num2 > num1) {
        printf("Largest: %d\n", num2);
        printf("Smallest: %d\n", num1);

} else {
        printf("Both numbers are equal: %d\n", num1);
    }

    
if (num1 != 0 && num2 % num1 == 0)
        printf("%d is divisible by %d\n", num2, num1);
    else if (num1 != 0)
        printf("%d is not divisible by %d\n", num2, num1);
if (num2 != 0 && num1 % num2 == 0)
        printf("%d is divisible by %d\n", num1, num2);
    else if (num2 != 0)
        printf("%d is not divisible by %d\n", num1, num2);

	return 0;
}

