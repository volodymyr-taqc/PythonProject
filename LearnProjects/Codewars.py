#ls = [0, 1, 3, 6, 10]
ls = [1, 2, 3, 4, 5, 6]

def parts_sums(ls):
    res = []
    for i in range(0, len(ls)+1):
        newls = ls[i:len(ls)]
        sum = 0        
        for j in newls:
            sum+=j
        res.append(sum)
    return res     


parts_sums(ls)       