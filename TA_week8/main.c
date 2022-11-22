//Stands for Standard Input Output and is a library used for input and output for C
#include <stdio.h>
// This is a function
void funct(){
    printf("Yo, whats popping im a function but this time in c\n");
}
//Main function
int main(){
    //String
    char name[] = "James";
    printf("%s\n", name);
    //Integers and If statements
    int num = 5;
    if(num == 5){
        printf("It is 5\n");
    }
    //Arithmetic operations
    int number = 69;
    number = number + 1;
    printf("%i\n", number);
    //For loops
    int i;
    //First argument is declaring the value, then the condition and increment
    for(i = 0; i < 5; i++){
        printf("%i\n",i);
    }
    //Calling function from line 1
    funct();
    /*Char, a string is essentially an array of characters.
    Only use '' when working with characters but use "" 
    when working with strings*/
    char character = 'c';
    printf("%c\n", character);
    //Input in C
    int input;
    printf("Enter a number\n");
    //This is the same as input() in python
    scanf("%i", &input);
    if(input == 4){
        printf("That's 4");
    }
    //There are no boolean values, this means that if we want to do a while(True) function we use
    while(1){
        printf("LOOPING");
    }
    //or
    for(;;){
        printf("LOOPING ALSO");
    }
    return 0;
}

