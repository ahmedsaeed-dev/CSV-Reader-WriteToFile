import csv


# prints the player and round they didn't participate in
def print_disqualified(player):
    # find all occurrences of -1 per curr player
    disq_indices = [i for i, x in enumerate(player) if x == "-1"]
    output = open("first_output.txt", "a")
    for i in disq_indices:
        input = ("%s %s didn't participate in round %d" % (player[0], player[1], i - 1))
        output.write(input)
        output.write("\n")


# prints second output file that contains name and total score (excluding -1) of all participants, sorted
def print_totals(players, count):
    totals = []
    dict = {}
    for i in range(0, count):
        totals.append(0)
    for i in players:
        disq_rounds = [i for i, x in enumerate(players[i]) if x == "-1"]
        for j in disq_rounds:
            players[i][j] = 0
        totals[i] = get_totals(players[i])

    for i in players:
        full_name = players[i][0] + ' ' + players[i][1]
        dict[full_name] = totals[i]
    print(dict)
    output = open("second.txt", "a")
    # TODO: MAKE IT SORT ALPHABETICAL IF TIE
    s = [(k, dict[k]) for k in sorted(dict, key=dict.get, reverse=True)]
    for key, value in s:
        input = ("%s - %s\n" % (key, value))
        output.write(input)



# check if curr player didn't play a round
def is_disqualified(player):
    if '-1' in player:
        return False
    else:
        return True

# calculate total scores
def find_all_total_score(players, count):
    high_score_list = []
    for i in range(0, count):
        curr_player = players.get(i)
        high_score = int(curr_player[2]) + int(curr_player[3]) + int(curr_player[4]) + int(curr_player[5])
        high_score_list.append(high_score)
    # print(high_score_list)
    return high_score_list


def get_totals(curr_player):
    return int(curr_player[2]) + int(curr_player[3]) + int(curr_player[4]) + int(curr_player[5])

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def average(lst):
    return sum(lst) / len(lst)

def get_round_total(curr_player, round):
    if curr_player[round] != '-1':
        return int(curr_player[round])
    else:
        return 0

if __name__ == "__main__":
    with open('file.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        count = 0
        h_scores_arr = []
        players = {}
        for row in reader:
            # store each row of players as a list into a dict using line count as key
            players[count] = row

            # print each disqualified player
            print_disqualified(players[count])

            # increment keys
            count += 1

        # get disqualified players indices
        disq_players = [a for a, b in players.items() if '-1' in b]
        # print(disq_players)

        # get qualified players indices
        qual_players = [a for a, b in players.items() if not '-1' in b]
        # print(qual_players)

        # find total scores
        index_w_total_scores = find_all_total_score(players, count)
        # find highest score
        highest_score = max(index_w_total_scores)
        # find indices containing highest score
        max_indices = [i for i, j in enumerate(index_w_total_scores) if j == highest_score]
        # print fname and lname of people who have the highest scores
        for index in max_indices:
            print('%s %s has the highest score of %s' % (players[index][0], players[index][1], highest_score))
        # find lowest score
        lowest_score = min(index_w_total_scores)
        # find indices containing lowest score
        min_indices = [i for i, j in enumerate(index_w_total_scores) if j == lowest_score]
        # print fname and lname of people who have the lowest scores
        for index in min_indices:
            print('%s %s has the lowest score of %s' % (players[index][0], players[index][1], lowest_score))
        # get totals for qualified players
        total = []
        for i in qual_players[:]:
            total.append(get_totals(players[i]))
        # print(total)
        # find mean of all good players
        median = "{:.1f}".format(median(total))
        # print(median)
        # find average of all good players
        average = "{:.1f}".format(average(total))
        # Print median and mean of all qualified players
        print('Median and mean of all qualified players are %s and %s (respectively)' % (median, average))

        # get mean score for each round
        round_total = [0, 0, 0, 0]
        round_count = [0, 0, 0, 0]
        val = 0
        for i in range(0, count):
            for round in range(2, 6):
                val = get_round_total(players[i], round)
                if round == 2: # round 1
                   round_total[0] += val
                   # checks to see if valid participate so can accomadate average score
                   if val != 0:
                       round_count[0] += 1
                elif round == 3: # round 2
                    round_total[1] += val
                    if val != 0:
                        round_count[1] += 1
                elif round == 4: # round 3
                    round_total[2] += val
                    if val != 0:
                        round_count[2] += 1
                elif round == 5: # round 4
                    round_total[3] += val
                    if val != 0:
                        round_count[3] += 1
        # set and print mean for each round
        round_averages = [0, 0, 0, 0]
        for i in range(0, 4):
            round_averages[i] = "{:.1f}".format(round_total[i]/round_count[i])
            print('Round %s mean: %s' % (i + 1, round_averages[i]))

        print_totals(players, count)
