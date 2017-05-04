

arr = [{'Hotel':'Hotel 1', 'Room':'Room 1', 'Board':'Board 1', 'Precio':100},
       {'Hotel':'Hotel 1', 'Room':'Room 1', 'Board':'Board 2', 'Precio':130},
       {'Hotel':'Hotel 1', 'Room':'Room 2', 'Board':'Board 1', 'Precio':230},
       {'Hotel':'Hotel 1', 'Room':'Room 2', 'Board':'Board 2', 'Precio':300},
       {'Hotel':'Hotel 2', 'Room':'Room 4', 'Board':'Board 1', 'Precio':111},
       {'Hotel':'Hotel 2', 'Room':'Room 2', 'Board':'Board 2', 'Precio':400},
       {'Hotel':'Hotel 2', 'Room':'Room 1', 'Board':'Board 2', 'Precio':230}
       ]

def array_to_dict(arr, keys):
    d = dict()
    for e in arr:
        if e.has_key(keys[0]) and e.has_key(keys[1]) and e.has_key(keys[2]):
            d.setdefault(e[keys[0]], {}).setdefault(e[keys[1]], {}).setdefault(e[keys[2]], []).append(e)
        elif not e.has_key(keys[0]):
            print keys[0] + " no encontrada"
            return array_to_dict(arr,['Hotel','Room','Board'])
        elif not  e.has_key(keys[1]):
            print keys[1] + " no encontrada"

            return array_to_dict(arr,['Hotel','Room','Board'])
        else:
            print keys[2] + " no encontrada"
            return array_to_dict(arr,['Hotel','Room','Board'])

    return d

def array_to_dict2(arr, keys):
    d = dict()
    d12 = dict()
    d2 = dict()
    d3 = dict()
    for e in arr:
        if e.has_key(keys[0]) and e.has_key(keys[1]) and e.has_key(keys[2]):




            d.setdefault(e[keys[0]], {}).setdefault(e[keys[1]], {}).setdefault(e[keys[2]], [e]).append(e)

        elif not e.has_key(keys[0]):

            print keys[0] + " no encontrada"

            return array_to_dict(arr,['Hotel','Room','Board'])

        elif not  e.has_key(keys[1]):

            print keys[1] + " no encontrada"

            return array_to_dict(arr,['Hotel','Room','Board'])

        else:

            print keys[2] + " no encontrada"

            return array_to_dict(arr,['Hotel','Room','Board'])

    return d



result = array_to_dict2(arr,['Hotel','Room','Board'])
print(result)