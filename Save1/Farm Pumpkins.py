clear()
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)

while True:
	good_tiles = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			while True:
				if get_water() <= .2:
					use_item(Items.Water)
				if not can_harvest():
					harvest()			
					plant(Entities.Pumpkin)
					break
				else:
					good_tiles += 1
					#Good pumpkin
					break
	
			move(North)
		move(East)
		if good_tiles >= get_world_size()*get_world_size():
			harvest()