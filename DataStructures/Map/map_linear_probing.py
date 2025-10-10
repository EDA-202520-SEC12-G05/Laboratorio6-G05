from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al
import random as rd

def new_map (num_elements, load_factor, prime=109345121):

    mapa = {
        "prime": 109345121,
        "capacity": mf.next_prime(num_elements // load_factor),
        "scale": rd.radint(1, prime-1),
        "shift": rd.radint(0, prime-1),
        "table": al.new_list(),
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
    }

    for i in range(mapa["capacity"]):
        entry = me.new_map_entry(None,None)
        al.add_last(mapa["table"], i)

    return mapa

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def put(my_map, key, value):

    hash = mf.hash_value(key, my_map["capacity"])
    pos = find_slot(my_map, key, hash)
    if my_map["table"][pos] == None:
        my_map["table"][pos] = (key, value)
        my_map["size"] += 1
    else: 
        my_map["table"][pos] == (key, value)

    my_map["current_factor"] =  my_map["size"] / my_map["capacity"]

    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map

def size (my_map):

    return my_map["size"]


def is_empty (my_map):
    
    if my_map["size"] == 0:
        return True
    else:
        return False
    
def key_set (my_map):

    lista = al.new_list()   

    for i in my_map["table"]["elements"]:
        al.add_last(lista, me.get_key(i))
    return lista

def value_set (my_map):

    lista = al.new_list()

    for i in my_map["table"]["elements"]:
        al.add_last(lista, me.get_value(i))
    return lista