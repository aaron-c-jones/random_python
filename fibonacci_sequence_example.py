def RecurseFib(position):  # recursive function
    if position == 0:
        return 0  # defining zero position of sequence
    elif position == 1:
        return 1  # defining 1st position of sequence
    else:
        # code for the 2nd position on of the sequence
        return RecurseFib(position - 1) + RecurseFib(position - 2)


def FibSeq(position):
    # function for printing sequence up to some position
    seq = list(map(RecurseFib, range(0, position)))
    return seq


position = 15  # number of elements of sequence desired
print(FibSeq(position))