Hot Potato
==========
#In this game (see Figure 2) children line up in a circle and pass an item from neighbor to neighbor as fast as they can. At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. Play continues until only one child is left.



from queue import Queue

def hotpotato(namelist,num):
	q = Queue()
	for name in q:
		q.enqueue(name)

	while q.size()
		for i in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()

	return q.dequeue()
