def d7nd5(start, end):

    if start%7 != 0:
        start = start + (7 - start%7)

    result = []
    while start <= end:
        if start%35 != 0:
            result.append(start)
        start += 7

    return result