from functools import reduce
from pkg_resources import resource_stream


def part1():
    print("day 15")
    hashStrings = []
    with resource_stream('input', 'D15.txt') as textInput:
        hashStrings = textInput.readline().decode().strip().split(",")
    res = []
    for hashString in hashStrings:
        res.append(hashCal(hashString))
    return reduce(lambda a, b: a+b, res)


def hashCal(string: str):
    res = 0
    for c in string:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def part2():
    print("day 15")
    hashStrings = []
    with resource_stream('input', 'D15.txt') as textInput:
        hashStrings = textInput.readline().decode().strip().split(",")
    boxes = {}

    for hashString in hashStrings:
        label, lens = "", ""
        if "=" in hashString:
            label, lens = hashString.split("=")
            boxNb = hashCal(label)
            box: list = boxes.setdefault(boxNb, [])
            present = False
            for i in range(len(box)):
                if label in box[i]:
                    box[i][label] = int(lens)
                    present = True
                    break
            if not present:
                box.append({label: int(lens)})
            boxes[boxNb] = box
        elif "-" in hashString:
            label = hashString.removesuffix("-")
            boxNb = hashCal(label)
            if boxNb in boxes:
                box: list = boxes[boxNb]
                for i in range(len(box)):
                    if label in box[i]:
                        del box[i]
                        boxes[boxNb] = box
                        break

    res = 0
    for k, v in boxes.items():
        for i in range(len(v)):
            val: dict = v[i]
            for lensSize in val.values():
                lensPower = lensSize*(i+1)*(k+1)
                res += lensPower

    return res
