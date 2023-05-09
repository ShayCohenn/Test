"""
create a funtion that takes 2 arrays
and smashes them together such that it creates a new array
that the first item is the first item of both the arrays together as a pair
"""
def myzip(it1, it2):
    return tuple(zip(it1, it2)) #creates a zip object from the 2 arrays and than use tuple to make the object readable

array1_index = [1,2,3,4,5]
array2_names = ["yossi","shay","bob","dana","guy"]