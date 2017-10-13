import operator

number = input('Please Enter Count of Total Players (Preferably Even Number): ')
number = int(number)

n = 1
player_list = list()
player_dict = dict()

while n <= number:
	player_name = input('Enter Player Name for player {}: '.format(n))
	player_list.append(player_name)
	n += 1

print(player_list)

for player in player_list:
	point = input('Enter This Players Point Between 1-5 for {}: '.format(player))
	point = int(point)
	player_dict[player] = point

sorted_player_list = sorted(player_dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_player_list)

team_a = list()
team_b = list()

team_a_point = 0
team_b_point = 0

listing_count = 1

for player, point in sorted_player_list:
	if listing_count % 4 == 1:
		team_a.append(player)
		team_a_point += point
		listing_count  +=1
	elif listing_count % 4 == 2:
		team_b.append(player)
		team_b_point += point
		listing_count  +=1
	elif listing_count % 4 == 3:
		team_b.append(player)
		team_b_point += point
		listing_count  +=1
	else:
		team_a.append(player)
		team_a_point += point
		listing_count  +=1

print('Team A will be {} and have {} points'.format(team_a, team_a_point))
print('Team B will be {} and have {} points'.format(team_b, team_b_point))