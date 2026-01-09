#clear()
while True:
	for i in range(0, get_world_size(), 2):
		for j in range(0, get_world_size(), 2):

			#if i%2 == 0 and j%2 == 0:
			if get_water() <= .2:
				use_item(Items.Water)
			if can_harvest():
				harvest()			
				plant(Entities.Tree)
			move(North)
			move(North)
		move(East)
		move(East)
