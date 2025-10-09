#Función New list
def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

#Función Get Element
def get_element(my_list, index):
    return my_list["elements"][index]

#Función Is present
def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

#Función add_first()
def add_first(my_list, element):
    if my_list["size"] == 0:
        my_list["elements"].append(element)
    elif my_list["size"] > 0:
        my_list["elements"].insert(0, element)
    my_list["size"] += 1

    return my_list

#Función add_last()
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

#Función size()
def size(my_list):
    return my_list["size"]

#Función fist_element()
def first_element(my_list):
    return my_list["elements"][0]

#Función is_empty()
def is_empty(my_list):
    return my_list["size"] == 0 

#Función delete_element()
def delete_element(my_list, pos):
    if pos >= 0 and pos < my_list["size"]:
     my_list["elements"].pop(pos)
     my_list["size"] -= 1
    
    return my_list

#Función remove_first()
def remove_first(my_list):
     if my_list["size"] > 0:
         my_list["size"] -= 1
         return my_list["elements"].pop(0) 

#Función remove_last()
def remove_last(my_list):
    if my_list["size"] > 0:
        my_list["size"] -= 1
    return my_list["elements"].pop()

#Función insert_element()
def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

#Función change_info()
def change_info(my_list, pos, new_info):
    my_list["elements"][pos] = new_info
    return my_list

#Función exchange()
def exchange(my_list, i, j):
    my_list["elements"][i], my_list["elements"][j] = my_list["elements"][j], my_list["elements"][i]
    return my_list

#Función sub_list()
def sub_list (my_list, pos_i, num_elements):
    sublist = my_list['elements'][pos_i : pos_i + num_elements]
    
    return {
        'elements': sublist,
        'size': len(sublist)
    }

#SORT 

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

#Sorts iterativos
def selection_sort(lst, sort_crit):

    if lst["size"] == 0 or lst["size"] == 1:
        return lst
    else:
        for i in range(0, lst["size"]-1):
            p_ch = i
            min_ = lst["elements"][i]
            for ch in range(i+1, lst["size"]):
                if sort_crit(lst["elements"][ch], min_):
                    p_ch = ch 
                    min_ = lst["elements"][ch]

            exchange(lst, i, p_ch)
        
        return lst

def insertion_sort(my_list, sort_crit):
    
    if my_list["size"] == 0 or my_list["size"]==1:
        return my_list
    else:
        for pos_i in range(1, my_list["size"]):
            pos_ch = pos_i - 1
            while pos_ch >= 0 and sort_crit(my_list["elements"][pos_i], my_list["elements"][pos_ch]):
                exchange(my_list, pos_i, pos_ch)
                pos_i = pos_ch
                pos_ch -= 1

        return my_list

def shell_sort(my_list, sort_crit):
    size = my_list["size"]

    if size == 0:
        return my_list
    else:
        elements = my_list["elements"]
        
        # Generar h Knuth
        h = 1
        while h < size // 3:
            h = 3 * h + 1

        # Recorrido por gaps
        while h >= 1:
            # Recorrido total izq a der
            for pos_inicial in range(h, size):  
                pos_actual = pos_inicial
                # comparación hacia atrás con gap h
                while pos_actual >= h and sort_crit(elements[pos_actual], elements[pos_actual - h]):
                    exchange(my_list, pos_actual, pos_actual - h)
                    pos_actual -= h
            
            #Reducción de h
            h = h // 3

    return my_list

#Ordanemientos Recursivos
def merge_sort(L, sort_crit):

    if L["size"] <= 1:   
        return L
    
    im = L["size"] // 2

    izq = sub_list(L, 0, im)
    der = sub_list(L, im, L["size"] - im)

    izord = merge_sort(izq, sort_crit)
    derord = merge_sort(der, sort_crit)

    return merge(izord, derord, sort_crit)


def merge(L1, L2, sort_crit):
    i1 = 0
    i2 = 0
    NL = new_list()

    while i1 < L1["size"] and i2 < L2["size"]:
        if sort_crit(L1["elements"][i1], L2["elements"][i2]) <= 0:
            add_last(NL, L1["elements"][i1])
            i1 += 1
        else:
            add_last(NL, L2["elements"][i2])
            i2 += 1

    # Sobran elementos de L1
    if i1 < L1["size"]:
        SL = sub_list(L1, i1, L1["size"] - i1)
        NL["elements"] += SL["elements"]
        NL["size"] = len(NL["elements"])

    # Sobran elementos de L2
    if i2 < L2["size"]:
        SL = sub_list(L2, i2, L2["size"] - i2)
        NL["elements"] += SL["elements"]
        NL["size"] = len(NL["elements"])

    return NL

def qsort(lst, i, f, sort_crit):
    if i >= f:
        return lst

    prev = i - 1
    ppivot = f
    pivot = lst["elements"][ppivot]

    for recorr in range(i, f):
        if sort_crit(lst["elements"][recorr], pivot):
            prev += 1
            exchange(lst, prev, recorr)

    exchange(lst, prev + 1, ppivot)
    ppivot = prev + 1

    qsort(lst, i, ppivot - 1, sort_crit)
    qsort(lst, ppivot + 1, f, sort_crit)

    return lst


def quick_sort(lst, sort_crit):
    if lst["size"] <= 1:   
        return lst
    
    qsort(lst, 0, lst["size"] - 1, sort_crit)
    return lst