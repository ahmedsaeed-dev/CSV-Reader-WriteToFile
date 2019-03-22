import csv


# prints the player and round they didn't participate in
def print_disqualified(player):
    # find all occurrences of -1
    indices = [i for i, x in enumerate(player) if x == "-1"]
    for i in indices:
        print("%s %s didn't participate in round %d" % (player[0], player[1], i - 1))


# check if curr player didn't play a round
def is_disqualified(player):
    if '-1' in player:
        return False
    else:
        return True


# determine person with highest scores
def find_highest_scores(players, count):



if __name__ == "__main__":
    with open('file.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        count = 0
        players = {}
        for row in reader:
            # store each row of players as a list into a dict using line count as key
            players[count] = row
            temp = players[count]
            # determine if any scores are negative
            if not is_disqualified(temp):
                print('%d Bad!' % count)

            else:
                print('%d Good!' % count)

            print_disqualified(temp)

            # increment keys
            count += 1



