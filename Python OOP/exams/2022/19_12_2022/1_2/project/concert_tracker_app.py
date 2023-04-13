from project.band import Band
from project.concert import Concert
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type in ["Guitarist", "Drummer", "Singer"]:

            is_musician = list(filter(lambda mus: mus.name == name, self.musicians))
            if is_musician:
                raise Exception(f"{name} is already a musician!")

            musician_dict = {"Guitarist": Guitarist(name, age), "Drummer": Drummer(name, age), "Singer": Singer(name, age)}
            musician = musician_dict[musician_type]

            self.musicians.append(musician)
            return f"{name} is now a {musician_type}."

        raise ValueError("Invalid musician type!")

    def create_band(self, name: str):

        is_band = list(filter(lambda b: b.name == name, self.bands))
        if is_band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        is_same_place = list(filter(lambda cnt: cnt.place == place, self.concerts))
        if is_same_place:

            concert = is_same_place[0]

            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        try:
            musician = next(filter(lambda mus: mus.name == musician_name, self.musicians))

        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda bdn: bdn.name == band_name, self.bands))

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        try:
            band = next(filter(lambda bdn: bdn.name == band_name, self.bands))

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda mus: mus.name == musician_name, band.members))

        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        concert = next(filter(lambda cnt: cnt.place == concert_place, self.concerts))
        band = next(filter(lambda bnd: bnd.name == band_name, self.bands))

        band_members_dict = {"Guitarist": [], "Drummer": [], "Singer": []}
        [band_members_dict[member.__class__.__name__].append(member) for member in band.members]

        if not all(band_members_dict.values()):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        def validate_musicians_skills(drummer_skills, singer_skills, guitarist_skills):

            d = [drm for drm in band_members_dict["Drummer"] if set(drummer_skills).issubset(drm.skills)]
            s = [sng for sng in band_members_dict["Singer"] if set(singer_skills).issubset(sng.skills)]
            g = [gtr for gtr in band_members_dict["Guitarist"] if set(guitarist_skills).issubset(gtr.skills)]

            if not all([d, s, g]):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        concert_genre = concert.genre

        if concert_genre == "Rock":

            drummer = ["play the drums with drumsticks"]
            singer = ["sing high pitch notes"]
            guitarist = ["play rock"]

            validate_musicians_skills(drummer, singer, guitarist)

        elif concert_genre == "Metal":

            drummer = ["play the drums with drumsticks"]
            singer = ["sing low pitch notes"]
            guitarist = ["play metal"]

            validate_musicians_skills(drummer, singer, guitarist)

        elif concert_genre == "Jazz":

            drummer = ["play the drums with drum brushes"]
            singer = ["sing low pitch notes", "sing high pitch notes"]
            guitarist = ["play jazz"]

            validate_musicians_skills(drummer, singer, guitarist)

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert_genre} concert in {concert_place}."