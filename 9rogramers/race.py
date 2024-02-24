players = ["mumu", "soe", "poe", "kai", "mine"]
callings=["kai", "kai", "mine", "mine"]
player_dict = {}

for i,p in enumerate(players):
    player_dict[p] = i

for call in callings:
    before_idx = player_dict[call]
    after_idx = player_dict[call]-1
    players[before_idx],players[after_idx] = players[after_idx],players[before_idx]
    player_dict[players[before_idx]],player_dict[players[after_idx]] = player_dict[players[after_idx]] ,player_dict[players[before_idx]]
