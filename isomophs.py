# In poker, suits do not have intrinsic order or value — only the pattern of ranks
# and suit groupings matter when comparing hands or boards.

# Problem description
# We define two sets of cards (we'll call them boards) 
#                              to be isomorphic if there exists a one-to-one mapping between the suits such that replacing each suit in the
#                              first board using this mapping produces the second board.
def boards_isomorphic(s1, s2):
    if len(s1) > 1 and len(s2) > 1 and len(s1) == len(s2):
        s1_dl = [ char + s1[i+1]  for i, char in enumerate(s1) if i % 2 == 0  ]
        s2_dl = [ char + s2[i+1]  for i, char in enumerate(s2) if i % 2 == 0  ]
        ranks = [bd1[0] for bd1 in s1_dl ]
        ranks_ = [bd2[0] for bd2 in s2_dl ]
        ptn = [bd1[1] for bd1 in s1_dl ]
        ptn2 = [bd2[1] for bd2 in s2_dl ]
        my_dict = [ ptn.count(i)  for i in ptn]
        my_dict2 = [ ptn2.count(i) for i in ptn2]
        count1 = [s1_dl.count(bd1[0]) for bd1 in s1_dl ]
        count2 = [s2_dl.count(bd2[0]) for bd2 in s2_dl ]

        
        if my_dict == my_dict2 and ranks == ranks_ :
            return True
        if my_dict == my_dict2 and count1 == count2 :
            return True
        return False
    elif(s1 == "" and s2 == ""):
        return True
    else:
        return False
    
    
        
print(boards_isomorphic("6s9h", "9s6c"))
# h,h,h,h
# s,s,s,s

        
# print(boards_isomorphic("QdQh2h3h", "QcQs2s4s"))
# d, h, h, h
# c, s ,s, s