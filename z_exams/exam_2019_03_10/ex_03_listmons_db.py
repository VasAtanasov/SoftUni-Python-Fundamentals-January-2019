class Player:
    def __init__(self, name, points):
        self.__name = name
        self.__points = points

    @property
    def name(self):
        return self.__name

    @property
    def total_points(self):
        return sum(self.__points)

    @property
    def number_of_games(self):
        return len(self.__points)


players = []


def by_score_desc_name_asc(array):
    for player in sorted(array, key=lambda p: (-p.total_points, p.name)):
        print(f"{player.name}: {player.total_points}")


def by_score_asc_name_asc(array):
    for player in sorted(array, key=lambda p: (p.total_points, p.name)):
        print(f"{player.name}: {player.total_points}")


def by_games_count_desc_name_asc(array):
    for player in sorted(array, key=lambda p: (-p.number_of_games, p.name)):
        print(f"{player.name}: {player.number_of_games}")


def by_games_count_asc_name_asc(array):
    for player in sorted(array, key=lambda p: (p.number_of_games, p.name)):
        print(f"{player.name}: {player.number_of_games}")


actions = {
    "score descending": by_score_desc_name_asc,
    "score ascending": by_score_asc_name_asc,
    "numberOfGames descending": by_games_count_desc_name_asc,
    "numberOfGames ascending": by_games_count_asc_name_asc
}

while True:
    line = input()
    if "report" == line:
        break

    tokens = line.split(" -> ")
    player_name = tokens[0]

    results = [int(x) for x in tokens[1].split(", ")]

    players.append(Player(player_name, results))

while True:
    line = input()
    if "end" == line:
        break

    actions[line](players)
