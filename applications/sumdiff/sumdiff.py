"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

matches = []
simple_solns = {}
add_solns = {}
sub_solns = {}

def sumdiff(nums):
    # build simple solutions dictionary
    for num in nums:
        simple_solns[num] = f(num)
    
    # build addition solutions dictionary 
    for a in nums:
        for b in nums:
            ab = (a, b)
            add_solns[ab] = simple_solns[a] + simple_solns[b]
            
    # build subtraction solutions dictionary
    for c in nums:
        for d in nums:
            cd = (c, d)
            sub_solns[cd] = simple_solns[c] - simple_solns[d]
            
    
    # find matches
    for i in add_solns.items():
        for j in sub_solns.items():
            if i[1] == j[1]:
                matches.append(i[0] + j[0])
                
    for nums in matches:
        print(f'a:{nums[0]}, b:{nums[1]}, c:{nums[2]}, d:{nums[3]}')

sumdiff(q)
                
    
            
    