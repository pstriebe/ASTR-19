#Code Journal #1

#Prompt #2

#floats
float1 = 2.5
float2 = 4.5

#ints
int1 = 5
int2 = 3

#defining Prompt 2
def Prompt2():
    #Sum of two floats
    print("Sum of two floats: " + str(float1) + " + " + str(float2) + " = " + str(float1+float2))
    print("Data tpye of Sum: " + str(type(float1+float2)) + "\n")
    
    #Difference of two ints
    print("Difference of two ints: " + str(int1) + " - " + str(int2) + " = " + str(int1-int2))
    print("Data type of Difference: " + str(type(int1-int2)) + "\n")
    
    #Product of a float and int
    print("Product of float and int: " + str(float1) + " x " + str(int1) + " = " + str(float1 * int1))
    print("Data type of Difference: " + str(type(float1*int1)))

#defining main
def main():
    Prompt2()
    
#executing Prompt 2 first
if __name__ == "__main__":
    main()