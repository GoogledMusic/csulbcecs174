#functions
#built in funciton
#function_name ([0 or more parameter ])
print(print()) # none is an empty object
#input (0 or more parameter) and returns back a string
# print(input("Hit any key j\key"))
# input(print()) # will return none
#user defined function
def salute(): # header
# body of the function
    print("Hello")
#function call
salute()
#parameter argument

#definition of a function that has one parameter and returns nothing
def fun1(names):
    print("Hello", names)

name = input("What is your name? ")
fun1(name)

import math
print(math.pow(2, 3)) # pow is a method

#pass by value
'''
C++
include <iostream>
int main(){
    cout << "Hello"
}

#Java
public class myFirstJava{
    public static void main(String[] args){
        System.out.println("Hello");
    }
}
'''
def add():
    num1 = eval(input("Please enter operand1"))
    num2 = eval(input("Please enter operand2"))
    sum = num1 + num2
    return sum

def main():
    # all the coed that you are going to write
    pass
    salute()
    name = input("What is your name? ")
    fun1(name)
    #build a calculator
    operation = input("What operation do you want to perform? ")
    #validate
    if operation == "+":
        print("add")
    elif operation == "-":
        print("subtract")
    elif operation == "*":
        print("multiply")
    elif operation == "/":
        print("divide")
    else:
        print("exponent")
main()
