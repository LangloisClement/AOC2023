from functools import reduce
from pkg_resources import resource_stream


def part1():
    print("Day 4")
    res = []
    with resource_stream('input', 'D4.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            numbers = line.split(":")[1].split("|")
            winningNumbers, givenNumbers = numbers[0].split(
            ), numbers[1].split()
            power = -1
            for givenNumber in givenNumbers:
                if givenNumber in winningNumbers:
                    power += 1
            if power >= 0:
                res.append(pow(2, power))
    return reduce(lambda a, b: a+b, res)


def part2():
    print("Day 4")
    with resource_stream('input', 'D4.txt') as textInput:
        lines = textInput.readlines()
        cardnumbers = [1 for line in lines]
        for i in range(len(cardnumbers)):
            line = lines[i].decode().strip()
            numbers = line.split(":")[1].split("|")
            winningNumbers, givenNumbers = numbers[0].split(
            ), numbers[1].split()
            nbValide = 0
            for givenNumber in givenNumbers:
                if givenNumber in winningNumbers:
                    nbValide += 1
            for j in range(i+1, i+1+nbValide):
                if j > len(cardnumbers):
                    break
                cardnumbers[j] += cardnumbers[i]
    return reduce(lambda a, b: a+b, cardnumbers)
