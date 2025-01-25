import pandas as pd
def append_to_list(original_list, item):
    original_list.append(item)
    return original_list

def slice_list(original_list, start, end):
    return original_list[start:end]

def reverse_list(original_list):
    return original_list[::-1]
