def sum_even_rows(row):
    # define a result list to store our list of rows
    result = []

    # loop from 1 to the row number passed to the function
    for row_num in range (1, row + 1):
        # on each loop, create the list for the current loop numbered row and append it to the result list
        row_list = []
        cur_row = 1
        for integer in range(2, 10000, 2):
            if len(row_list) < cur_row:
                row_list.append(integer)
            else:
                result.append(row_list)
                row_list = []
                cur_row += 1
            if len(result) == row:
                break
    
    # sum all the numbers in the last list in our result list
    row_sum = sum(result[-1])

    # return that sum
    return row_sum