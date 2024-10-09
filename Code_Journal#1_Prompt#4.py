#Code Journal #1

#Prompt #4

#creating the favorite animal class
class FavAnimal:
    #initialization of all of the attributes of my favorite animal
    def __init__(self, arm_length, leg_length, num_eyes, tail, furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.tail = tail
        self.furry = furry
        
    #method that prints out the attributes of my favorite animal
    def attributes(self):
        has_tail = "does" if self.tail else "does not"
        is_furry = "is" if self.furry else "does not"
        print(f"My favorite animal's arms are {self.arm_length} inches long, its legs are {self.leg_length} inches long, it has {self.num_eyes} eyes, it {has_tail} have a tail, and it {is_furry} furry.")

#defining main
def main():
    #setting the values of my favorite animal
    animal = FavAnimal(23.5, 23.5, 2, True, True)
        
    animal.attributes()
#executing Prompt 4 first
if __name__ == "__main__":
    main()