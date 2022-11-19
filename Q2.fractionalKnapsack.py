def knapSackProb(m, p, w):
    ratio = []
    dict1 = {}
    current_wt = m
    max_profit = 0
    for i in range(len(p)):
        ratio.append(p[i]/w[i])
        dict1[p[i]/w[i]] = {'profit': p[i], 'weight': w[i]}
        print(dict1)
    ratio.sort()
    ratio.reverse()
    for i in range(len(p)):
        if current_wt == 0:
            break
        if dict1[ratio[i]]['weight'] <= current_wt:
            max_profit += dict1[ratio[i]]['profit']
            current_wt -= dict1[ratio[i]]['weight']
        else:
            fraction = current_wt/dict1[ratio[i]]['weight']
            max_profit += fraction * dict1[ratio[i]]['profit']
            current_wt -= fraction * dict1[ratio[i]]['weight']
    print(dict1)
    return max_profit


m = int(input("Enter max weight"))
w = list(map(int, input("Enter values of weight").split()))
p = list(map(int, input("Enter values of profit").split()))

print(knapSackProb(m, p, w))