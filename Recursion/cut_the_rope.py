import sys
listOfLens = []
def maximumProduct(rope_len: int):
    if rope_len == 3:
        return (2)
    if rope_len == 4:
        return (4)
    product = 1
    while (rope_len > 4):
        product *= 3
        rope_len -= 3
    return (product * rope_len)
for counter, i in enumerate(sys.stdin):
    if counter == 0:    
        numberOfCases = int(i)
    else:
        listOfLens.append(i)
        
for i in listOfLens:
    print(maximumProduct(int(i)) % 1000)
