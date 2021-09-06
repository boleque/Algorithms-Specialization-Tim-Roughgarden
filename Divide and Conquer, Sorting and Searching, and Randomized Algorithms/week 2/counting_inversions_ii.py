def sort_and_count(arr): # 
    if len(arr) == 1:
        return 0
    
    left_part = None
    right_part = None
    
    # b, c, d - sorted version of original arr
    b, x = sort_and_count(left_part)
    c, y = sort_and_count(right_part)
    
    d, z = merge_and_count_split_inversion(b, c) # O(n)
    
    return x + y + z

def merge_and_count_split_inversion(arr):
    pass