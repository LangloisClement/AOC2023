from functools import reduce
from pkg_resources import resource_stream
import re


def part1():
    print("day 19")
    workflows, parts = {}, []
    flagEmpty = False
    with resource_stream('input', 'D19.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            if not line:
                flagEmpty = True
                continue
            if not flagEmpty:
                # ie: 'px{a<2006:qkq,m>2090:A,rfg}'=[('px', 'a<2006:qkq,m>2090:A,rfg')]
                regexFind = re.findall(r"(\w+)\{(.*)\}", line)
                key, value = regexFind[0]
                workflows[key] = value
            else:
                # line=line.strip("{}")
                parts.append({kv.split("=")[0]: int(
                    kv.split("=")[1]) for kv in line[1:-1].split(",")})
    res = 0
    for part in parts:
        if accepted(part, workflows):
            res += reduce(lambda a, b: a+b, part.values())
    return res


def accepted(part: dict, workflows: dict):
    state = "in"
    while True:
        if state == "R":
            return False
        if state == "A":
            return True
        rules = workflows[state].split(",")
        for rule in rules:
            if ":" in rule:
                test, res = rule.split(":")
                val, operation, limits = test[0], test[1], int(test[2:])
                if operation == ">":
                    if part[val] > limits:
                        state = res
                        break
                else:
                    if part[val] < limits:
                        state = res
                        break
            else:
                state = rule
