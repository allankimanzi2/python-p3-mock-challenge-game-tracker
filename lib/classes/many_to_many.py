class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if len(title) == 0:
            raise ValueError("Title must be longer than 0 characters")
        self.__title = title
        self.__results = []

    @property
    def title(self):
        return self.__title

    def results(self):
        return self.__results

    def players(self):
        return list(set(result.player for result in self.__results))

    def average_score(self, player):
        player_results = [result.score for result in self.__results if result.player == player]
        if not player_results:
            return None
        return sum(player_results) / len(player_results)

    def results(self):
        return self.__results

    def players(self):
        return list(set(result.player for result in self.__results))

    def average_score(self, player):
        player_results = [result.score for result in self.__results if result.player == player]
        if not player_results:
            return None
        return sum(player_results) / len(player_results)

    def highest_scored(game):
        player_scores = {player: game.average_score(player) for player in game.players()}
        if not player_scores:
            return None
        return max(player_scores, key=player_scores.get)


class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be of type str")
        if not 2 <= len(username) <= 16:
            raise ValueError("Username must be between 2 and 16 characters, inclusive")
        self.__username = username
        self.__results = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be of type str")
        if not 2 <= len(value) <= 16:
            raise ValueError("Username must be between 2 and 16 characters, inclusive")
        self.__username = value

    def results(self):
        return self.__results

    def games_played(self):
        return list(set(result.game for result in self.__results))

    def played_game(self, game):
        return any(result.game == game for result in self.__results)

    def num_times_played(self, game):
        return sum(1 for result in self.__results if result.game == game)


class Result:
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("Player must be of type Player")
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game")
        if not isinstance(score, int):
            raise TypeError("Score must be of type int")
        if not 1 <= score <= 5000:
            raise ValueError("Score must be between 1 and 5000, inclusive")
        self.__player = player
        self.__game = game
        self.__score = score
        self.__player.results().append(self)
        self.__game.results().append(self)

    @property
    def score(self):
        return self.__score

    @property
    def player(self):
        return self.__player

    @property
    def game(self):
        return self.__game
