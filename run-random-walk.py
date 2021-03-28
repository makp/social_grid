from random_walk import RandomWalk

randw = RandomWalk(4)

arr = randw.make_grid(10, 4)
randw.walk_and_update_multi(arr, 10)
