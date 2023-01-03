import pokebase as pb
import datetime as dt
import time


tic = time.perf_counter()

charmander = pb.pokemon('charmander')

pokelist = []


pokedict = {'name': charmander.name,
            'height': charmander.height,
            'base_xp': charmander.base_experience,
            'hp': charmander.stats[0].base_stat,
            'attack': charmander.stats[1].base_stat,
            'defence': charmander.stats[2].base_stat,
            'special-attack': charmander.stats[3].base_stat,
            'special-defence': charmander.stats[4].base_stat,
            'speed': charmander.stats[5].base_stat
            }

pokelist.append(pokedict)

print(pokelist)

toc = time.perf_counter()
print(f"The scripts took {toc - tic:0.4f} seconds")
