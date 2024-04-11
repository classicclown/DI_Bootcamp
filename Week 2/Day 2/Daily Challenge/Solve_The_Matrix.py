grid_string ='''
    7ii
    Tsx
    h%?
    i #
    sM.
    $a.
    #t%
    ^r!
    '''
split_list = grid_string.strip().split("\n")
grid_list = [list(split_list.strip()) for split_list in split_list]
decoder =""
counter=0
for column in range(len(grid_list[counter])):
    for row in grid_list:
        if row[column].isalpha():
            decoder+=row[column]
            counter+=1
        elif not row[column].isalpha():
            decoder+=" "
            counter+=1
print(decoder)
