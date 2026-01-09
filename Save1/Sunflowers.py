clear()
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Sunflower)
		move(North)
	move(East)
while True:
	for x in range(15, 6, -1):

		for i in range(get_world_size()):
			for j in range(get_world_size()):
				while True:
					if get_water() <= .2:
						use_item(Items.Water)
					if can_harvest():
						if measure() == x:
							harvest()			
							#plant(Entities.Sunflower)
					break
				move(North)
			move(East)
	break