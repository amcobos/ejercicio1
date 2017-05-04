import unittest
from ejercicio1 import array_to_dict2
class TestsBasicos(unittest.TestCase):
    def test_prueba_ejercicio_1(self):
        arr = [{'Hotel':'Hotel 1', 'Room':'Room 1', 'Board':'Board 1', 'Precio':100},
            {'Hotel':'Hotel 1', 'Room':'Room 1', 'Board':'Board 2', 'Precio':130},
            {'Hotel':'Hotel 1', 'Room':'Room 2', 'Board':'Board 1', 'Precio':230},
            {'Hotel':'Hotel 1', 'Room':'Room 2', 'Board':'Board 2', 'Precio':300},
            {'Hotel':'Hotel 2', 'Room':'Room 4', 'Board':'Board 1', 'Precio':111},
            {'Hotel':'Hotel 2', 'Room':'Room 2', 'Board':'Board 2', 'Precio':400},
            {'Hotel':'Hotel 2', 'Room':'Room 1', 'Board':'Board 2', 'Precio':230}
            ]
        keys=['Hotel','Room','Board']
        diccionario=array_to_dict2(arr, keys)
        resultado={'Hotel 1': {'Room 2': {'Board 2': [{'Hotel': 'Hotel 1', 'Precio': 300, 'Room': 'Room 2', 'Board': 'Board 2'}], 'Board 1': [{'Hotel': 'Hotel 1', 'Precio': 230, 'Room': 'Room 2', 'Board': 'Board 1'}]}, 'Room 1': {'Board 2': [{'Hotel': 'Hotel 1', 'Precio': 130, 'Room': 'Room 1', 'Board': 'Board 2'}], 'Board 1': [{'Hotel': 'Hotel 1', 'Precio': 100, 'Room': 'Room 1', 'Board': 'Board 1'}]}}, 'Hotel 2': {'Room 4': {'Board 1': [{'Hotel': 'Hotel 2', 'Precio': 111, 'Room': 'Room 4', 'Board': 'Board 1'}]}, 'Room 2': {'Board 2': [{'Hotel': 'Hotel 2', 'Precio': 400, 'Room': 'Room 2', 'Board': 'Board 2'}]}, 'Room 1': {'Board 2': [{'Hotel': 'Hotel 2', 'Precio': 230, 'Room': 'Room 1', 'Board': 'Board 2'}]}}}
        self.assertEqual(resultado,diccionario)