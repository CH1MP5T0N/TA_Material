#include <stdio.h>
int main(){
    float subtotal, tipamount, tip, total;
    printf("Enter the subtotal: ");
    scanf("%f", &subtotal);
    printf("Enter the tip amount: ");
    scanf("%f", &tip);
    tipamount = tip/100 * subtotal;
    printf("Subtotal: $%0.2f\n", subtotal);
    printf("Tip: $%0.2f\n", tipamount);
    total = subtotal + tipamount;
    printf("Total: $%0.2f", total);
}