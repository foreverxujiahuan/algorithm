from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fc = {}
        self.fr = {}
        self.cr = defaultdict(SortedSet)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fc[f] = c
            self.fr[f] = r
            self.cr[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        s = self.cr[self.fc[food]]
        s.remove((-self.fr[food], food))
        s.add((-newRating, food))
        self.fr[food] = newRating


    def highestRated(self, cuisine: str) -> str:
        return self.cr[cuisine][0][1]



if __name__ == '__main__':

    foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
    a1 = foodRatings.highestRated("korean")
    a2 = foodRatings.highestRated("japanese")
    foodRatings.changeRating("sushi", 16)
    a3 = foodRatings.highestRated("japanese")
    foodRatings.changeRating("ramen", 16)
    a4 = foodRatings.highestRated("japanese")
    print(a1, a2, a3, a4)
