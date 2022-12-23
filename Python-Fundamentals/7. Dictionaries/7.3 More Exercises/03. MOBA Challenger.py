player_pool = {}

while True:
    line = input()
    if line == "Season end":
        break
    if "->" in line:
        line = line.split(" -> ")
        player, position, skill = line[0], line[1], int(line[2])
        if player not in player_pool.keys():
            player_pool[player] = {position: skill}
        else:
            if position not in player_pool[player].keys():
                player_pool[player][position] = skill
            else:
                if skill > player_pool[player][position]:
                    player_pool[player][position] = skill

    elif "vs" in line:
        line = line.split(" vs ")
        player_1, player_2 = line[0], line[1]
        if player_1 in player_pool.keys() and player_2 in player_pool.keys():
            p_1_total_points = sum([val for val in player_pool[player_1].values()])
            p_2_total_points = sum([val for val in player_pool[player_2].values()])
            for key in player_pool[player_1].keys():
                if key in player_pool[player_2].keys() and p_1_total_points > p_2_total_points:
                    player_pool.pop(player_2)
                    break
                elif key in player_pool[player_2].keys() and p_1_total_points < p_2_total_points:
                    player_pool.pop(player_1)
                    break
                elif key in player_pool[player_2].keys() and p_1_total_points == p_2_total_points:
                    continue

player_pool_tp = {key: sum([v for v in player_pool[key].values()]) for key, val in player_pool.items()}
player_pool_tp = dict(sorted(player_pool_tp.items(), key=lambda x: (-x[1], x[0])))
for key, val in player_pool_tp.items():
    print(f"{key}: {val} skill")
    player_results = sorted(player_pool[key].items(), key=lambda x: (-x[1], [0]))
    for k, v in player_results:
        print(f"- {k} <::> {v}")