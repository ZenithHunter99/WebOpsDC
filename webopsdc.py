def flatten_array(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_array(item))
        else:
            result.append(item)
    return result

input_array = [1, [2, [3, [4, 5]], 6], 7]
print(flatten_array(input_array))
