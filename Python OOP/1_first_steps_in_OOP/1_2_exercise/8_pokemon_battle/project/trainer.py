class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, new_pokemon):

        if new_pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(new_pokemon)
        return f"Caught {new_pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        is_pokemon = list(filter(lambda x: x.name == pokemon_name, self.pokemons))

        if is_pokemon:

            pokemon = is_pokemon[0]
            pokemon_name = pokemon.name
            self.pokemons.remove(pokemon)

            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):

        res = []

        res.append(f"Pokemon Trainer {self.name}")
        res.append(f"Pokemon count {len(self.pokemons)}")
        [res.append(f"- {x.pokemon_details()}") for x in self.pokemons]

        return "\n".join(res)

