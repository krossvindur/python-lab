# whenever applicable, all excercises must always pay 
# special attention to:
# 1. is there a faster way? (execution speed)
# 2. is there a simpler way? (code size and readability)
# 3. is there a lighter way? (memory footprint)

# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between n and m (both
# included).

def d7nd5(start, end):

    if start%7 != 0:
        start = start + (7 - start%7)

    result = []
    while start <= end:
        if start%35 != 0:
            result.append(start)
        start += 7

    return result