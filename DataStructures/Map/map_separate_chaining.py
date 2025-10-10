from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
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

def put(mp, key, value):
    h = mf.hash_value(mp, key)
    entry = me.new_map_entry(key, value)

    #Acceder al bucket del índice
    bucket = mp['table']['elements'][h]

    #Esta función devuelve la pos en la que encuentra el elemento de búsqueda o -1 si no está
    pos = sll.is_present(bucket, me.get_key(entry), default_compare)

    #Si no está en la sll
    if pos == -1:
        sll.add_last(bucket, entry)
        #Actualizar size y current factor
        mp['size'] += 1
        mp['current_factor'] = mp['size']/mp['capacity']
    #Sisí, solo actualizar el valor
    else:
        sll.change_info(bucket, pos, entry)
    
    if mp['current_factor'] > mp['limit_factor']:
        rehash(mp)
    
    return mp

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def contains(mp, key):

    if mp['size'] == 0:
        return False
    else:
        h = mf.hash_value(mp, key)
        bucket = mp['table']['elements'][h]

        node = bucket['first']
        while node is not None and me.get_key(node['info']) != key:
            node = node['next']

        if node == None:
            return False
        else: 
            return True

def remove(mp, key):
    
    if mp['size'] == 0 or not contains(mp, key):
        return mp
    else:
        h = mf.hash_value(mp, key)
        bucket = mp['table']['elements'][h]
        node = bucket['first']
        pos = 0

        while default_compare(key, node['info']) != 0:
            node = node['next']
            pos +=1
        
        sll.delete_element(bucket, pos)
        mp['size'] -= 1

        return mp

def get(mp, key):

    if mp['size'] == 0 or not contains(mp, key):
        return None
    else:
        h = mf.hash_value(mp, key)
        bucket = mp['table']['elements'][h]

        node = bucket['first']
        while default_compare(key, node['info']) != 0:
            node = node['next']
        
        return me.get_value(node['info'])
        
def size(mp):
    return mp['size']

def is_empty(mp):
    return mp['size'] == 0

def key_set(mp):
    ks = al.new_list()

    if mp['size'] != 0:
        for bucket in mp['table']['elements']:
            node = bucket['first']
            while node is not None:
                al.add_last(ks, me.get_key(node['info']))
                node = node['next']
    return ks

def value_set(mp):
    vs = al.new_list()

    if mp['size'] != 0:
        for bucket in mp['table']['elements']:
            node = bucket['first']
            while node is not None:
                al.add_last(vs, me.get_value(node['info']))
                node = node['next']
    return vs

def rehash(mp):
    capacity = mf.next_prime(mp['capacity']*2)
    temp_htable = {'prime': mp['prime'],
    'capacity': capacity,
    'scale': mp['scale'],
    'shift': mp['shift'],
    'table': al.new_list(),
    'size': 0,
    'limit_factor': mp['limit_factor'],
    'current_factor': mp['size']/capacity}

    #Primer for para llenar de buckets vacíos
    for _ in range(capacity):
        al.add_last(temp_htable['table'], sll.new_list())

    #Segundo for para traer los elementos del antiguo 
    for bucket in mp['table']['elements']:
        node = bucket['first']
        while node is not None:
            put(temp_htable, node['info']['key'], node['info']['value'])
            node = node['next']

    mp['capacity'] = temp_htable['capacity']
    mp['table'] = temp_htable['table']
    mp['size'] = temp_htable['size']
    mp['current_factor'] = temp_htable['current_factor']

    return mp