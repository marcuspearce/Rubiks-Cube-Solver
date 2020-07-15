from cube_moves import *

R = "red"
O = "orange"
Y = "yellow"
G = "green"
B = "blue"
W = "white"

## below is random valid permutation of a rubik's cube
	# arbitrarily, lets say 1st is top, 2-5 is sides rotating clockwise, 6 is bottom
	# from current face: turn up, turn left 3x, turn up (to find all sides)
cube_1 = [
	[Y,R,R,
	 O,R,W,
	 W,O,Y],
 	[G,B,G,
 	 G,Y,R,
 	 R,Y,B],
 	[O,O,W,
 	 B,B,Y,
 	 O,R,B],
 	[G,W,B,
 	 B,W,Y,
 	 W,W,R],
 	[R,Y,O,
 	 R,G,O,
 	 W,W,G],
 	[B,G,Y,
 	 B,O,G,
 	 O,G,Y]
]

orientation = ["BOTTOM", "BACK", "RIGHT", "FRONT", "LEFT", "TOP"]

# logic to solve cube -> maybe make it an object/class?
	# my approach would be to create sub-functions for like L', R etc. and apply those in the simple algorithm
	# feel free to re-orient the cube as you want!

def printCube(cube):
	print()
	for i in range(6):
		print('\n' * 2 + orientation[i])
		for x in range(9):
			if x % 3 == 0:
				print()
				print(cube_1[i][x], end=" ")
			else:
				print(cube_1[i][x], end=" ")


def main():

	printCube(cube_1)
	Bottom(cube_1, orientation)
	print('\n-----------------------------------------------')
	printCube(cube_1)

if __name__ == "__main__":
    main()
