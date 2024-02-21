clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

clothes_dict={}
answer=1
for cloth in clothes:
    if cloth[1] not in clothes_dict:
        clothes_dict[cloth[1]]=[cloth[0]]
    else:
        clothes_dict[cloth[1]].append(cloth[0])

# none이있다고 생각하면
for k,v in clothes_dict.items():
    answer*= (len(v)+1)

print(answer-1)