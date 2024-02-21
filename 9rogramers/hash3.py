participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


p_dict={}
for p in participant:
    if p in p_dict:
        p_dict[p] += 1
    else:
        p_dict[p] = 1
for c in completion:
    p_dict[c] -=1
for k,v in p_dict.items():
    if v==1:
        answer= k