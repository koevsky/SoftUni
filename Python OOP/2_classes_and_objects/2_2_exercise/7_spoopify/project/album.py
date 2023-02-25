class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song):
        if song in self.songs:

            return "Song is already in the album."

        elif self.published:

            return "Cannot add songs. Album is published."

        elif song.single:

            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return 'Cannot remove songs. Album is published.'

        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
            self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."

        except StopIteration:
            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):

        result = [f"Album {self.name}"]
        [result.append(f"== {s.get_info()}") for s in self.songs]
        return '\n'.join(result)
