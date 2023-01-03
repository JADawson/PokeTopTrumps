import cards


class Game:
    # the main class to operate the game

    def __init__(self, player_name: str, deck_source: str = 'Pokedex', num_cards: int = 50):
        self.players = {}
        self.player_name = player_name
        self.deck = cards.Deck(source=deck_source)
        self.init_players()
        self.deal_cards()
        print("Yay")

    def init_players(self):
        self.players['Player 1'] = {'Name': 'Computer',
                                    'Type': 'Computer',
                                    'Hand': []}

        self.players['Player 2'] = {'Name': self.player_name,
                                    'Type': 'Human',
                                    'Hand': []}

    def deal_cards(self):
        while len(self.deck.cards) > 1:

            self.players['Player 1']['Hand'].append(self.deck.cards.pop())
            self.players['Player 2']['Hand'].append(self.deck.cards.pop())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = Game(player_name='James')
    print("Finished")
