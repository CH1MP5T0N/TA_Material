#include <stdio.h>
int main()
{
    float x1, y1, x2, y2, formula;
    printf("Enter the x-coordinate for point1: ");
    scanf("%f", &x1);
    printf("Enter the y-coordinate for point1: ");
    scanf("%f", &y1);
    printf("Enter the x-coordinate for point2: ");
    scanf("%f", &x2);
    printf("Enter the y-coordinate for point2: ");
    scanf("%f", &y2);
    printf("The slope that connects the two points (%.1f, %.1f) and (%.1f, %.1f) is %0.5f",x1, x2, y1, y2, (y2-y1) / (x2-x1));
    return 0;
}