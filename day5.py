from pkg_resources import resource_stream


class Day5:
    seedNumbers = []
    seedToSoil = {}
    soilToFert = {}
    fertToWater = {}
    waterToLight = {}
    lightToTemp = {}
    tempToHumidity = {}
    humidityToLoc = {}

    def __init__(self, puzzleInput: str) -> None:
        with resource_stream('input', puzzleInput) as textInput:
            lines = [l.decode().strip() for l in textInput.readlines()]
            self.seedNumbers = [int(nb)
                                for nb in lines[0].split(":")[1].split()]
            i = 3
            print("compiling seed to soil")
            self.seedToSoil, i = self.day5_xToY_tuples_list(lines, i)
            print("compiling soil to fert")
            self.soilToFert, i = self.day5_xToY_tuples_list(lines, i+2)
            print("compiling fert to water")
            self.fertToWater, i = self.day5_xToY_tuples_list(lines, i+2)
            print("compiling water to light")
            self.waterToLight, i = self.day5_xToY_tuples_list(lines, i+2)
            print("compiling light to temp")
            self.lightToTemp, i = self.day5_xToY_tuples_list(lines, i+2)
            print("compiling temp to humi")
            self.tempToHumidity, i = self.day5_xToY_tuples_list(lines, i+2)
            print("compiling humi to loc")
            self.humidityToLoc, i = self.day5_xToY_tuples_list(lines, i+2)

    def day5_xToY_tuples_list(self, lines: list[str], i: int):
        xToY = []
        while i < len(lines) and lines[i] != "":
            dest, source, ran = lines[i].split()
            dest, source, ran = int(dest), int(source), int(ran)
            xToY.append((dest, source, ran))
            i += 1
        return xToY, i

    def part1(self):
        print("Day 5")
        locList = []
        for seed in self.seedNumbers:
            soil = day5_findNumber(seed, self.seedToSoil)
            fert = day5_findNumber(soil, self.soilToFert)
            water = day5_findNumber(fert, self.fertToWater)
            light = day5_findNumber(water, self.waterToLight)
            temp = day5_findNumber(light, self.lightToTemp)
            hum = day5_findNumber(temp, self.tempToHumidity)
            loc = day5_findNumber(hum, self.humidityToLoc)
            locList.append(loc)

        locList.sort()
        return min(locList)

    def part2(self):
        res = 1000000000000
        seedNumber = 0
        for i in range(0, len(self.seedNumbers), 2):
            print(f'dealing with pair nb: {i/2}')
            start = self.seedNumbers[i] if self.seedNumbers[i] > seedNumber else seedNumber
            for seeds in range(self.seedNumbers[i], self.seedNumbers[i]+self.seedNumbers[i+1]):
                soil = day5_findNumber(seeds, self.seedToSoil)
                fert = day5_findNumber(soil, self.soilToFert)
                water = day5_findNumber(fert, self.fertToWater)
                light = day5_findNumber(water, self.waterToLight)
                temp = day5_findNumber(light, self.lightToTemp)
                hum = day5_findNumber(temp, self.tempToHumidity)
                loc = day5_findNumber(hum, self.humidityToLoc)
                res = loc if loc < res else res
                seedNumber = seeds
        return res

# 550427451 min pair 1
# 125675349 min pair 2


def day5_findNumber(n: int, tupleList: list(tuple())):
    for t in tupleList:
        if n >= t[1] and n <= t[1]+t[2]:
            diff = n-t[1]
            return diff+t[0]
    return n
