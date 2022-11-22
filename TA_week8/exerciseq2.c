#include <stdio.h>
#include <math.h>
int main(){
    float speed;
    float acc;
    printf("Enter the plane's take off speed in m/s: ");
    scanf("%f", &speed);
    printf("Enter the plane's acceleration in m/s**2: ");
    scanf("%f", &acc);
    double formula = pow(speed, 2) / (2*acc);
    printf("The minimum runway length needed for this airplaine is %0.4f meters", formula);
    return 0;
}