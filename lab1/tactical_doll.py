'''
    LAB 1 - DOLL GUARD/TACTICAL DOLL - By: Adrian Ardizza (NPM: 2006524896) - DDP1 Kelas C
    This project is made as a demonstration of variables and data types, mainly string, int, and float.
    However to simplify the project, I have applied some principals from Object Oriented Programming, such as
    Classes (to define all functions related to Dolls in the Doll class itself) and also Dictionaries (to simplify
    variable assignment in the Doll class.)
'''

'''
    THIS SECTION OF THE CODE IS FOR DEFINING THE DOLL CLASS
    This is the Doll class. Classes are similar to object in that it stores data, but it can also have methods that can be used
    to alter the data. In this case, i defined two methods to get DPS and Effectiveness based on the formula given.
    When called, the method will return the value of the computed values so that it can be printed into the console (STDOUT).
    
    EXTRA NOTES: The self value in a class refers to the class object itself. In most parts, assigning values to self is similar
    to how once would assign values to a JSON object/Python dictionary.
'''
class Doll():
    def __init__(self, stats): # This function expects stats to be a dictionary with the corresponding key-value pair.
        self.name = stats['name']
        self.firepower = int(stats['firepower'])
        self.rof = int(stats['rof'])
        self.accuracy = int(stats['accuracy'])
        self.evasion = int(stats['evasion'])
    def getDPS(self):
        return round((self.firepower * self.rof) / 60, 2) 
    def getEffectiveness(self):
        combat_effectiveness = 30 * self.firepower + 40 * (self.rof ** 2 / 120) + 15*(self.accuracy + self.evasion)
        return int(combat_effectiveness)

#####                  END OF CLASS SECTION                   #####

print("##### FRIENDLY DOLL'S STATS #####")
friendlyDollStats = {} # Variable assignment from input is store in a Dictionary for ease of access by the Class.
friendlyDollStats['name'] = input("Input the Tactical Doll's name: ")
friendlyDollStats['firepower'] = input("Input Firepower: ")
friendlyDollStats['rof'] = input("Input Rate of Fire: ")
friendlyDollStats['accuracy'] = input("Input Accuracy: ")
friendlyDollStats['evasion'] = input("Input Evasion: ")

friendlyDoll = Doll(friendlyDollStats)

print("\n### REQUEST SUCCESSFUL ###\n")
print(friendlyDoll.name.upper())
print("Firepower: %d" % (friendlyDoll.firepower))
print("Rate of Fire: %d" % (friendlyDoll.rof))
print("Accuracy: %d" % (friendlyDoll.accuracy))
print("Evasion: %d" % (friendlyDoll.evasion))
print("Damage per Second: %.2f" % (friendlyDoll.getDPS()))
print("Combat Effectiveness: %d" % (friendlyDoll.getEffectiveness()))