import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]    # matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):

            if len(self.photos[i]) < 4:

                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(self.photos[i])}"

        return "No more free slots"

    def display(self):

        result = []
        result.append(11*"-")
        [result.append(f"{' '.join('[]' for _ in range(len(r)))}\n{'-' * 11}") for r in self.photos]
        return '\n'.join(result)

