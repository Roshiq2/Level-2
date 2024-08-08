def ss(data):
    subsets = []
    subsets.append([])
    for num in data:
        new_subsets = []
        for s in subsets:
            new_subset = s + [num]
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    return subsets

def bag(a, w, p):
    mall = ss(weights)
    ros = []
    for i in mall:
        if sum(i) == a:
            ros.append(i)
    print(ros)
    sam=[]
    for x in ros:
        rq=0
        for y in x:
            rq+=p[w.index(y)]
        sam.append(rq)
    return(max(sam))

weights = [1,5,3,4]
prices = [15,10,9,4]
W = 8

print(bag(W, weights, prices))