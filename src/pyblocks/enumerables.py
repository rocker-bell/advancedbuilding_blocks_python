# enumerables.py
class Enumerable:

    @staticmethod
    def my_each(arr, callback):
        for i, val in enumerate(arr):
            callback(val, i, arr)
        return arr[0] if arr else None

    @staticmethod
    def my_each_with_index(arr, callback):
        for i, val in enumerate(arr):
            callback(val, i)
        return arr[0] if arr else None

    @staticmethod
    def my_select(arr, callback):
        return [val for val in arr if callback(val)]

    @staticmethod
    def my_all(arr, callback):
        return all(callback(val) for val in arr)

    @staticmethod
    def my_any(arr, callback):
        return any(callback(val) for val in arr)

    @staticmethod
    def my_none(arr, callback):
        return not any(callback(val) for val in arr)

    @staticmethod
    def my_count(arr, val=None, callback=None):
        if callback:
            return sum(1 for v in arr if callback(v))
        if val is not None:
            return sum(1 for v in arr if v == val)
        return len(arr)

    @staticmethod
    def my_map(arr, callback=None):
        if callback is None:
            return arr[:]
        return [callback(v) for v in arr]

    @staticmethod
    def my_inject(arr, start_val=None, callback_or_symbol=None):
        if callable(start_val) and callback_or_symbol is None:
            callback = start_val
            result = arr[0]
            for val in arr[1:]:
                result = callback(result, val)
            return result

        if callable(callback_or_symbol):
            callback = callback_or_symbol
            if start_val is None:
                result = arr[0]
                values = arr[1:]
            else:
                result = start_val
                values = arr
            for val in values:
                result = callback(result, val)
            return result

        operation = callback_or_symbol
        if start_val is None:
            result = arr[0]
            values = arr[1:]
        else:
            result = start_val
            values = arr

        for val in values:
            if operation == '+':
                result += val
            elif operation == '*':
                result *= val
            else:
                raise ValueError("Unsupported symbol for my_inject")

        return result
