import pokebase as pb
import random
import time
import pandas as pd


class GetPokemon:
    # get a random number of Pokemon from which to build a deck
    # there are currently 904 Pokemon in the pokebase library

    def __init__(self, num_poke: int, use_random: bool = False, generate_pokedex: bool = False):
        self.df = None
        self.num_poke = num_poke
        self.all_pokemon = list(range(1, 904))
        self.selection = []
        self.selected_pokemon = []
        self.pokedex_filename = 'pokedex_all.csv'

        if use_random:
            self.random_selection()
        else:
            if generate_pokedex:
                self.linear_selection()
            else:
                self.read_pokedex()

    def random_selection(self):
        for i in range(self.num_poke):
            choice = random.choice(self.all_pokemon)
            self.selection.append(choice)
            self.all_pokemon.remove(choice)
            self.make_dictionary_random(choice)

    def linear_selection(self):
        for i in range(1, self.num_poke):
            try:
                self.make_dictionary_random(i)
            except:
                pass

    def make_dictionary_random(self, choice):
        poke = pb.pokemon(choice)
        poke_dict = {'id_no': poke.id,
                     'name': poke.name,
                     'height': poke.height,
                     'base_xp': poke.base_experience,
                     'hp': poke.stats[0].base_stat,
                     'attack': poke.stats[1].base_stat,
                     'defence': poke.stats[2].base_stat,
                     'special-attack': poke.stats[3].base_stat,
                     'special-defence': poke.stats[4].base_stat,
                     'speed': poke.stats[5].base_stat,
                     'front_image': poke.sprites.front_default
                     }
        self.selected_pokemon.append(poke_dict)

    def export_pokemon(self):
        self.df = pd.DataFrame(self.selected_pokemon)
        self.df.to_csv(self.pokedex_filename, index=False)

    def read_pokedex(self):
        df = pd.read_csv(self.pokedex_filename)
        self.selected_pokemon = df.to_dict('records')


if __name__ == '__main__':
    tic = time.perf_counter()
    t = GetPokemon(2, use_random=False, generate_pokedex=False)
    toc = time.perf_counter()
    print(f"The scripts took {toc - tic:0.4f} seconds")
    print(t.num_poke)
