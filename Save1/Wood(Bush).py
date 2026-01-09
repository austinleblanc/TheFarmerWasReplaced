clear()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			while True:
				if get_water() <= .2:
					use_item(Items.Water)
				if can_harvest():
					harvest()			
					plant(Entities.Bush)
					break
			move(North)
		move(East)