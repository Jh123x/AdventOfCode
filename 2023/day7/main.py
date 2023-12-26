from typing import List, Dict
from types import LambdaType

FILE_NAME: str = "input.txt" 
# Expected testcase result: 6440
RANKING: List[str] = "AKQJT98765432"
RANKING: List[str] = RANKING[::-1]
HIERARCHY_MAP: Dict[int, LambdaType] = {
    5: lambda _: (20,),
    4: lambda _: (19,),
    3: lambda x: (17,) if 2 in set(x.values()) else (18,),
    2: lambda x: (14,) if list(x.values()).count(2) == 1 else (15,),
    1: lambda x: tuple(map(lambda y: RANKING.index(y), x.keys())),
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
        return HIERARCHY_MAP.get(max(freq.values()))(freq)

    def to_alt_rep(self: "Bet") -> str:
        return (
            self.cards.replace("A", "E")
            .replace("T", "A")
            .replace("J", "B")
            .replace("Q", "C")
            .replace("K", "D")
        )

    def __lt__(self: "Bet", __value: "Bet") -> bool:
        if self.strength == __value.strength:
            return self.to_alt_rep() < __value.to_alt_rep()
        return self.strength < __value.strength

    def __eq__(self, __value: "Bet") -> bool:
        return (
            self.strength == __value.strength
            and self.to_alt_rep() == __value.to_alt_rep()
        )

    def __str__(self: "Bet") -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.cards} ({self.strength}): {self.bet}"


def part1(data_str: str) -> int:
    hands = data_str.split("\n")
    vals: List[Bet] = []
    for hand in hands:
        cards, value = hand.split(" ")
        bet = Bet(cards, int(value))
        vals.append(bet)
    vals.sort()
    score = 0
    for idx, bet in enumerate(vals):
        curr_bet = (idx + 1) * bet.bet
        score += curr_bet

    return score


if __name__ == "__main__":
    with open(FILE_NAME) as f:
        data_str = f.read()
    res = part1(data_str)
    print("Part 1:", res)
