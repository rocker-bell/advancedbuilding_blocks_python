from src.pyblocks.enumerables import Enumerable as E

arr = [1, 2, 3, 4]
print(E.my_select(arr, lambda x: x % 2 == 0))  # [2, 4]
