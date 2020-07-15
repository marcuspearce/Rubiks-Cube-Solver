def Front(cube, orientation):

	# Turning front side
	front = cube[orientation.index("FRONT")]
	temp = front[:3] + front[:5:-1]
	temp.insert(3, front[5])
	temp.append(front[3]) # clockwise list w/out center

	temp = temp[6:] + temp[:6] # 'turning' the side (moving back 2 to front of list)
	temp.insert(4, front[4]) # putting center back

	stickers = temp[:3] + temp[7:4:-1] # reformatting back to cube
	stickers.insert(3, temp[8])
	stickers.insert(4, temp[4])
	stickers.insert(5, temp[3])

	cube[orientation.index("FRONT")] = stickers

	# Turning the sides (of the front layer)
	top, left, bottom, right = cube[orientation.index("TOP")], cube[orientation.index("LEFT")], cube[orientation.index("BOTTOM")], cube[orientation.index("RIGHT")]
	top_3_stickers = top[6:]
	top[6], top[7], top[8] = left[8], left[5], left[2] # left -> top
	left[2], left[5], left[8] = bottom[0], bottom[1], bottom[2] # bottom -> left
	bottom[0], bottom[1], bottom[2] = right[6], right[3], right[0] # right -> bottom
	right[0], right[3], right[6] = top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] # top -> right

def Right(cube, orientation):

	# Turning right side
	right = cube[orientation.index("RIGHT")]
	temp = right[:3] + right[:5:-1]
	temp.insert(3, right[5])
	temp.append(right[3]) # clockwise list w/out center

	temp = temp[6:] + temp[:6] # 'turning' the side (moving back 2 to front of list)
	temp.insert(4, right[4]) # putting center back

	stickers = temp[:3] + temp[7:4:-1] # reformatting back to cube
	stickers.insert(3, temp[8])
	stickers.insert(4, temp[4])
	stickers.insert(5, temp[3])

	cube[orientation.index("RIGHT")] = stickers

	# Turning the sides (as if right was front side)
	top, left, bottom, right = cube[orientation.index("TOP")], cube[orientation.index("FRONT")], cube[orientation.index("BOTTOM")], cube[orientation.index("BACK")]
	top_3_stickers = ['', '', '']
	top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] = top[2], top[5], top[8]
	top[2], top[5], top[8] = left[2], left[5], left[8] # left -> top
	left[2], left[5], left[8] = bottom[2], bottom[5], bottom[8] # bottom -> left
	bottom[2], bottom[5], bottom[8] = right[6], right[3], right[0] # right -> bottom
	right[0], right[3], right[6] = top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] # top -> right

def Left(cube, orientation):

	# Turning right side
	left = cube[orientation.index("LEFT")]
	temp = left[:3] + left[:5:-1]
	temp.insert(3, left[5])
	temp.append(left[3]) # clockwise list w/out center

	temp = temp[6:] + temp[:6] # 'turning' the side (moving back 2 to front of list)
	temp.insert(4, left[4]) # putting center back

	stickers = temp[:3] + temp[7:4:-1] # reformatting back to cube
	stickers.insert(3, temp[8])
	stickers.insert(4, temp[4])
	stickers.insert(5, temp[3])

	cube[orientation.index("LEFT")] = stickers

	# Turning the sides (as if left was front side)
	top, left, bottom, right = cube[orientation.index("TOP")], cube[orientation.index("BACK")], cube[orientation.index("BOTTOM")], cube[orientation.index("FRONT")]
	top_3_stickers = ['', '', '']
	top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] = top[0], top[3], top[6]
	top[0], top[3], top[6] = left[8], left[5], left[2] # left -> top
	left[2], left[5], left[8] = bottom[6], bottom[3], bottom[0] # bottom -> left
	bottom[6], bottom[3], bottom[0] = right[6], right[3], right[0] # right -> bottom
	right[0], right[3], right[6] = top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] # top -> right

def Back(cube, orientation):

	# Turning right side
	back = cube[orientation.index("BACK")]
	temp = back[:3] + back[:5:-1]
	temp.insert(3, back[5])
	temp.append(back[3]) # clockwise list w/out center

	temp = temp[6:] + temp[:6] # 'turning' the side (moving back 2 to front of list)
	temp.insert(4, back[4]) # putting center back

	stickers = temp[:3] + temp[7:4:-1] # reformatting back to cube
	stickers.insert(3, temp[8])
	stickers.insert(4, temp[4])
	stickers.insert(5, temp[3])

	cube[orientation.index("BACK")] = stickers

	# Turning the sides (as if back was front side)
	top, left, bottom, right = cube[orientation.index("TOP")], cube[orientation.index("RIGHT")], cube[orientation.index("BOTTOM")], cube[orientation.index("LEFT")]
	top_3_stickers = ['', '', '']
	top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] = top[2], top[1], top[0]
	top[2], top[1], top[0] = left[8], left[5], left[2] # left -> top
	left[2], left[5], left[8] = bottom[8], bottom[7], bottom[6] # bottom -> left
	bottom[8], bottom[7], bottom[6] = right[6], right[3], right[0] # right -> bottom
	right[0], right[3], right[6] = top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] # top -> right

def Up(cube, orientation):

	# Turning right side
	top = cube[orientation.index("TOP")]
	temp = top[:3] + top[:5:-1]
	temp.insert(3, top[5])
	temp.append(top[3]) # clockwise list w/out center

	temp = temp[6:] + temp[:6] # 'turning' the side (moving back 2 to front of list)
	temp.insert(4, top[4]) # putting center back

	stickers = temp[:3] + temp[7:4:-1] # reformatting back to cube
	stickers.insert(3, temp[8])
	stickers.insert(4, temp[4])
	stickers.insert(5, temp[3])

	cube[orientation.index("TOP")] = stickers

	# Turning the sides (as if back was front side)
	top, left, bottom, right = cube[orientation.index("BACK")], cube[orientation.index("LEFT")], cube[orientation.index("FRONT")], cube[orientation.index("RIGHT")]
	top_3_stickers = ['', '', '']
	top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] = top[0], top[1], top[2]
	top[0], top[1], top[2] = left[0], left[1], left[2] # left -> top
	left[0], left[1], left[2] = bottom[0], bottom[1], bottom[2] # bottom -> left
	bottom[0], bottom[1], bottom[2] = right[0], right[1], right[2] # right -> bottom
	right[0], right[1], right[2] = top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] # top -> right

def Bottom(cube, orientation):

	# Turning right side
	bottom = cube[orientation.index("BOTTOM")]
	temp = bottom[:3] + bottom[:5:-1]
	temp.insert(3, bottom[5])
	temp.append(bottom[3]) # clockwise list w/out center

	temp = temp[6:] + temp[:6] # 'turning' the side (moving back 2 to front of list)
	temp.insert(4, bottom[4]) # putting center back

	stickers = temp[:3] + temp[7:4:-1] # reformatting back to cube
	stickers.insert(3, temp[8])
	stickers.insert(4, temp[4])
	stickers.insert(5, temp[3])

	cube[orientation.index("BOTTOM")] = stickers

	# Turning the sides (as if back was front side)
	top, left, bottom, right = cube[orientation.index("FRONT")], cube[orientation.index("LEFT")], cube[orientation.index("BACK")], cube[orientation.index("RIGHT")]
	top_3_stickers = ['', '', '']
	top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] = top[6], top[7], top[8]
	top[6], top[7], top[8] = left[6], left[7], left[8] # left -> top
	left[6], left[7], left[8] = bottom[6], bottom[7], bottom[8] # bottom -> left
	bottom[6], bottom[7], bottom[8] = right[6], right[7], right[8] # right -> bottom
	right[6], right[7], right[8] = top_3_stickers[0], top_3_stickers[1], top_3_stickers[2] # top -> right
