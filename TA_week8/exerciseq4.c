#include <stdio.h>
#include <math.h>
int main(){
    float side;
    printf("Enter the side length of the hexagon: ");
    scanf("%f", &side);
    float formula = 3*sqrt(3)/2*pow(side, 2);
    printf("%0.3f", formula);
}