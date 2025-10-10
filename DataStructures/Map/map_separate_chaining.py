from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
import random as rd

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(num_elements//load_factor)
    scale = rd.randint(1, prime-1)
    shift = rd.randint(0, prime-1)
    htable = {'prime': prime,
    'capacity': capacity,
    'scale': scale,
    'shift': shift,
    'table': al.new_list(),
    'size': 0,
    'limit_factor': load_factor,
    'current_factor': 0}
    for _ in range(capacity):
        al.add_last(htable['table'], sll.new_list())
    return htable
