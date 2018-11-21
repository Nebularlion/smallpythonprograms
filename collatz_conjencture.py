def get_cycle_length(n):

    # takes an integer 0 < n < 10000 returns the number of steps it will take to get to 1

    i = 1
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            i += 1
        else:
            n = int(3 * n + 1)
            i += 1
    return i

def get_cycle_length_range(start, end):

    lenght_max = 0
    a = start
    b = end
    if start > end:
        end = a
        start = b
    for i in range(start, end + 1):
        length = get_cycle_length(i)
        if length > lenght_max:
            lenght_max = length
    return lenght_max
