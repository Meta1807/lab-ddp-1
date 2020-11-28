'''
    DDP-1 - WEEK 2 - LAB 2: MEONG BROSSS
    BY: ADRIAN ARDIZZA - 2006524896 - DDP1 CLASS C

    This project was made as a demonstration of branching and looping in Python. For this lab project, I decided to use a single class
    to centralize all of the variables (since coordinate of player can be stored in a class) and methods. 
    
    I have defined a Player() class that will hold all the variables and methods, the summary of which can be seen below: 
      [VARIABLES]
      On being instantiated, a Player object will have variables x and y assigned to itself by the __init__ function.

      [METHODS]
      - The move method takes in commands from the user and translates it into movement by manipulating the coordinate variables of 
        the Player object. For the purpose of this challenge, after every step the method will store the coordinates of the Player.
      - The getLocation method returns the current position of the Player, this is useful for when we need to print the object's location 
        when the program ends.

    When the number of inputs is equal to the expected number of input (or if a HOME command is given), the program will get the value
    of Player.steps and prints it on the console.
'''

class Player():
    def __init__(self): # Initialize x and y values for Player (meong) object.
        self.x = 0
        self.y = 0
        self.steps = []
    def move(self, command): # Move function takes commands given by user, and manipulates the object's coordinate.
        if command == "U":
            self.y += 1
        elif command == "S":
            self.y -= 1
        elif command == "T":
            self.x += 1
        elif command == "B":
            self.x -= 1
        self.steps.append((self.x, self.y))
    def getLocation(self):
        return (self.x, self.y)
def main():
    meong = Player() # Instantiates "meong" as a Player() object.
    num_of_args = int(input("Banyak Perintah: "))
    i = 0
    while i < num_of_args:
        command = input("Masukkan Perintah ")
        if command in ['U', 'S', 'T', 'B']: # Checks if command is defined, if so then it is passed to "meong" object.
            meong.move(command)
            i += 1
        elif command == "HOME": # HOME command prints the current location of "meong", and breaks out of loop.
            break
        else:
            # If command is not defined, then counter will increase to reflect that a command has been inputted, but meong will not move.
            i += 1
    steps = "Jalur yang ditempuh meong bross adalah "
    print(steps, end = '')
    print(*meong.steps, sep="-") # Print all the steps that the "meong" object has taken. (used *args to return meong.steps as arguments)
    print("Distance from start = %f" % ((meong.x**2 + meong.y**2)**0.5))


if __name__ == "__main__":
        main()