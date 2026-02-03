class PartidoTenis:
    def __init__(self):
        self.points_player_1 = 0
        self.points_player_2 = 0

    def _check_game_situation(self):
        return self.points_player_1 >= 4 or self.points_player_2 >= 4

    def _get_endgame_score(self):
        deuce = self._check_deuce()
        if deuce:
            return deuce
        advantage = self._check_advantage()
        if advantage:
            return advantage
        game_won = self._check_game_won()
        if game_won:
            return game_won
        return None

    def _check_deuce(self):
        is_deuce = (self.points_player_1 >= 3 and
                    self.points_player_2 >= 3 and
                    self.points_player_1 == self.points_player_2)
        return 'Deuce' if is_deuce else None

    def _check_advantage(self):
        if (self.points_player_1 >= 4 and
                self.points_player_1 == self.points_player_2 + 1):
            return 'Adv | -'
        elif (self.points_player_2 >= 4 and
              self.points_player_2 == self.points_player_1 + 1):
            return '- | Adv'
        return None

    def _check_game_won(self):
        if (self.points_player_1 >= 4 and
                self.points_player_1 >= self.points_player_2 + 2):
            return 'Game | -'
        elif (self.points_player_2 >= 4 and
              self.points_player_2 >= self.points_player_1 + 2):
            return '- | Game'
        return None

    def score(self):
        score_map = {0: "0", 1: "15", 2: "30", 3: "40"}

        if self._check_game_situation():
            return self._get_endgame_score()

        if self._check_deuce():
            return 'Deuce'

        p1_score = score_map[self.points_player_1]
        p2_score = score_map[self.points_player_2]
        return f"{p1_score} | {p2_score}"

    def point_won_by(self, player):
        if not isinstance(player, str):
            return 'El jugador debe ser el string "jugador 1" o "jugador 2"'
        if player not in ["jugador 1", "jugador 2"]:
            return 'El jugador debe ser "jugador 1" o "jugador 2"'
        if player == "jugador 1":
            self.points_player_1 += 1
        else:
            self.points_player_2 += 1
