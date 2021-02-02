# Exercise01_Vineyard
# Used Formula: V = (R-2E)/S
# V: number of grapevines, R: length of the row in feet, E: amount of space in feet, used by an end point assembly
# S: space between vines, in feet.

print("Enter the following quantities in feet.")
r = float(input("\tHow long is this row? "))
e = float(input("\tHow wide is the end-post assembly? "))
s = float(input("\tHow much space should be between the vines? "))

numberOfGrapeVines = (r - 2 * e) / s
print(f"\nThis row has enough space for {int(numberOfGrapeVines)} vine(s)")