import pokebase as pb
import random
import numpy as np
import pandas as pd


def random_selection_api(num_choices: int, num_pokemon: int):
    all_pokemon = list(range(1, num_pokemon))
    selected_ids = []
    selected_pokemon = []

    for i in range(1, num_choices):
        random_choice = random.choice(all_pokemon)

        selected_ids.append(random_choice)
        all_pokemon.remove(random_choice)
        selected_pokemon.append = dict_from_pokemon(random_choice)

    return selected_pokemon


def random_selection_csv(filename: str = 'pokedex_all.csv', num_choices: int = 50):
    all_list = read_pokedex_csv(filename)
    selected_ids = []
    selected_pokemon = []

    for i in range(num_choices):
        random_choice = random.choice(all_list)

        selected_ids.append(random_choice)
        all_list.remove(random_choice)
        selected_pokemon.append(random_choice)

    print("Finished Selection")
    selected_pokemon = sorted(selected_pokemon, key=lambda x: x['random_int'])
    return selected_pokemon


def dict_from_pokemon(pokemon_id):
    pokemon = pb.pokemon(pokemon_id)
    att_dict = {'id_no': pokemon.id,
                'name': pokemon.name,
                'height': pokemon.height,
                'base_xp': pokemon.base_experience,
                'hp': pokemon.stats[0].base_stat,
                'attack': pokemon.stats[1].base_stat,
                'defence': pokemon.stats[2].base_stat,
                'special-attack': pokemon.stats[3].base_stat,
                'special-defence': pokemon.stats[4].base_stat,
                'speed': pokemon.stats[5].base_stat,
                'front_image': pokemon.sprites.front_default,
                'random_sorter': random.randint(1, 999999)
                }
    return att_dict


def write_pokedex_csv(filename: str, num_pokemon: int):
    selected_ids = []
    selected_pokemon = []
    for i in range(1, num_pokemon):
        try:
            selected_ids.append(i)
            selected_pokemon.append(dict_from_pokemon(i))
            df = pd.DataFrame(selected_pokemon)
            df.to_csv(filename, index=False)
        except Exception as error:
            print(error)
            pass


def read_pokedex_csv(filename):
    df = pd.read_csv(filename)
    random_int = np.random.randint(1, 999999, size=len(df))
    df['random_int'] = random_int
    att_dict = df.to_dict('records')
    return att_dict


if __name__ == '__main__':
    random_selection_csv()
    print("hello")
