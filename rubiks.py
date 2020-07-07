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
	[[Y,R,R],
	 [O,R,W],
	 [W,O,Y]],
 	[[G,B,G],
 	 [G,Y,R],
 	 [R,Y,B]],
 	[[O,O,W],
 	 [B,B,Y],
 	 [O,R,B]],
 	[[G,W,B],
 	 [B,W,Y],
 	 [W,W,R]],
 	[[R,Y,O],
 	 [R,G,O],
 	 [W,W,G]],
 	[[B,G,Y],
 	 [B,O,G],
 	 [O,G,Y]]
]

face_names = ["TOP", "SIDE 1", "SIDE 2", "SIDE 3", "SIDE 4", "BOTTOM"]


# logic to solve cube -> maybe make it an object/class?
	# my approach would be to create sub-functions for like L', R etc. and apply those in the simple algorithm
	# feel free to re-orient the cube as you want!



def main():

	print()
	for i in range(6):
		print(face_names[i])
		print(cube_1[i][0])	# first row
		print(cube_1[i][1])	# second row
		print(cube_1[i][2])	# third row
		print()


if __name__ == "__main__":
    main()