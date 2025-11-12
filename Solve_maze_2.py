#取得世界大小
ws = get_world_size()

#註記死路陣列初始化
die_road = []
for i in range(ws):
	sub_list = []
	for j in range(ws):
		sub_list.append(0)
	die_road.append(sub_list)

#初始化移動方向
goto = North 

#無限運行主程式
while True:

	#取得當前座標
	pos = [get_pos_x(),get_pos_y()]

	#到達寶箱位置，終止迴圈
	if pos[0] == measure()[0] and pos[1] == measure()[1]:
		break

	#註記死路
	count = 0
	for d in [East,North,West,South]:
		if not can_move(d):
			count += 1
		#往北
		elif pos[1] + 1 < ws and die_road[pos[0]][pos[1] +1] == "X" and d == North:
			count += 1
		#往南
		elif pos[1] - 1 > -1 and die_road[pos[0]][pos[1] -1] == "X" and d == South:
			count += 1
		#往西
		elif pos[0] - 1 > -1 and die_road[pos[0] -1][pos[1]] == "X" and d == West:
			count += 1
		#往東
		elif pos[0] + 1 < ws and die_road[pos[0] +1][pos[1]] == "X" and d == East:
			count += 1
		else:
			pass
		
	if count == 3:
		die_road[pos[0]][pos[1]] = "X"
		

	elif count == 4:
		print('ERROR')


	#開走
	goto = [East,North,West,South][random() * 4]
	
	if goto == North:
		if can_move(North) and pos[1] + 1 < ws and die_road[pos[0]][pos[1] +1] != "X":
			move(North)
		
	elif goto == South:
		if can_move(South) and pos[1] - 1 > -1 and die_road[pos[0]][pos[1] -1] != "X":
			move(South)
	
	elif goto == West:
		if can_move(West) and pos[0] - 1 > -1 and die_road[pos[0] -1][pos[1]] != "X":
			move(West)

	elif goto == East:
		if can_move(East) and pos[0] + 1 < ws and die_road[pos[0] +1][pos[1]] != "X":
			move(East)

	


	
	