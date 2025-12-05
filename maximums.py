def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    max_val = x
    if y > max_val:
        max_val = y
    if z > max_val:
        max_val = z
        
    return max_val