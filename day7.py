from functools import reduce, total_ordering
from collections import Counter
from enum import Enum

from pkg_resources import resource_stream

enumHandType = Enum("EnumHandType", [
                    "HIGH", "ONE_PAIR", "TWO_PAIR", "THREE", "FULL_HOUSE", "FOUR", "FIVE"])


@total_ordering
class Day7_hand:
    handCards = []
    handType = None

    def __init__(self, input: str) -> None:
        self.handCards = [self.convertValue(c) for c in input]
        counter = Counter(self.handCards)
        flagThree = False
        flagPair = False
        for key in counter:
            match counter[key]:
                case 5:
                    self.handType = enumHandType.FIVE
                case 4:
                    self.handType = enumHandType.FOUR
                    break
                case 3:
                    flagThree = True
                case 2:
                    if flagPair:
                        self.handType = enumHandType.TWO_PAIR
                        break
                    flagPair = True
        if not self.handType:
            match (flagThree, flagPair):
                case (True, True):
                    self.handType = enumHandType.FULL_HOUSE
                case (True, False):
                    self.handType = enumHandType.THREE
                case(False, True):
                    self.handType = enumHandType.ONE_PAIR
                case _:
                    self.handType = enumHandType.HIGH

    def convertValue(self, char):
        match char:
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "5":
                return 5
            case "6":
                return 6
            case "7":
                return 7
            case "8":
                return 8
            case "9":
                return 9
            case "T":
                return 10
            case "J":
                return 11
            case "Q":
                return 12
            case "K":
                return 13
            case "A":
                return 14
            case _:
                raise ValueError(f"{char} is not a valid chr")

    def _is_valid_operand(self, other):
        return hasattr(other, "handCards")

    def __eq__(self, __value: object) -> bool:
        if not self._is_valid_operand(__value):
            return NotImplemented
        return self.handCards == __value.handCards

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        if self.handType == other.handType:
            for i in range(len(self.handCards)):
                if self.handCards[i] == other.handCards[i]:
                    continue
                return self.handCards[i] < other.handCards[i]
        else:
            return self.handType.value < other.handType.value

    def __repr__(self) -> str:
        return f"{self.handType.name}:{self.handCards}"


class Day7:
    hands = []

    def __init__(self, puzzleInput: str) -> None:
        with resource_stream('input', puzzleInput) as textInput:
            for l in textInput.readlines():
                l = l.decode().strip().split()
                self.hands.append((Day7_hand(l[0]), int(l[1])))

    def part1(self):
        self.hands.sort()
        bidValues = [(i+1)*self.hands[i][1] for i in range(len(self.hands))]
        return reduce(lambda a, b: a+b, bidValues)
