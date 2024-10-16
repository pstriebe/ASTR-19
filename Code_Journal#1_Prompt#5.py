#Code Journal #1

#Prompt #5

import numpy as np

#defining main
def main():
    
    #defining the range of 0-2pi with 1000 entries in between them
    x_values = np.linspace(0, 2 * np.pi, 1000)
    
    #making the headers for each row
    print(f"{'x':<15} {'sin(x)':<15}")
    
    #calculating each x value in sin(x)
    for x in x_values:
        print(f"{x:<15.6f} {np.sin(x):<15.6f}")

#executing Prompt 5 first
if __name__ == "__main__":
    main()