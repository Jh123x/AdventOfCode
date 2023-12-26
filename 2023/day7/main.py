from typing import List, Dict, Tuple
from types import LambdaType

FILE_NAME: str = "input.txt"
# Expected testcase result: 6440
# Result != 250247386
RANKING: List[str] = "AKQJT98765432"
RANKING: List[str] = RANKING[::-1]
HIERARCHY_MAP: Dict[int, LambdaType] = {
    5: lambda _: 20,
    4: lambda _: 19,
    3: lambda x: 18 if 2 in set(x.values()) else 17,
    2: lambda x: 14 if list(x.values()).count(2) == 1 else 15,
    1: lambda _: 0,
}


class Bet:
    def __init__(self: "Bet", cards: str, bet: int) -> None:
        self.cards = cards
        self.bet = bet
        self.strength = self.calc_strength(self.cards)

    def calc_strength(self: "Bet", cards: str) -> int:
        freq = {}
        for card in cards:
            freq[card] = freq.get(card, 0) + 1
        start_weight = HIERARCHY_MAP.get(max(freq.values()))(freq),
        arr=[start_weight]
        arr.extend([RANKING.index(letter) for letter in self.cards])
        return tuple(arr)


    def __lt__(self: "Bet", __value: "Bet") -> bool:
        return self.strength < __value.strength

    def __eq__(self: "Bet", __value: "Bet") -> bool:
        return self.cards == __value.cards

    def __str__(self: "Bet") -> str:
        return self.__repr__()

    def __repr__(self: "Bet") -> str:
        return f"{self.cards} ({self.strength}): {self.bet}"


def part1(data_str: str) -> int:
    hands = data_str.split("\n")
    vals: List[Bet] = []
    for hand in hands:
        cards, value = hand.split(" ")
        bet = Bet(cards, int(value))
        vals.append(bet)
    vals.sort()
    print(vals)
    score = 0
    for idx, bet in enumerate(vals):
        score += (idx + 1) * bet.bet

    return score


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data_str = f.read()
    res = part1(data_str)
    print("Part 1:", res)
