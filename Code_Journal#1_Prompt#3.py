#Code Journal #1

#Prompt #3

#defining f(x)
def f(x):
    return x**3 + 8
    
#defining main
def main():
    x = float(input("Enter x value: ")) #asks user to input a value for x
    
    result = f(x) #value that equals the result to simply everything
    
    if result > 27:
        print(str(result) + ", YAY!") #if the result is greater than 27, it prints the result and "YAY!"
    
    else:
        print(result) #else it just prints the result

#executing Prompt 3 first
if __name__ == "__main__":
    main()