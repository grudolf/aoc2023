import logging
import re

RESULTS = []

LAMBDAS = {
    '<': {
        'x': lambda xmas, value: xmas[0] < value,
        'm': lambda xmas, value: xmas[1] < value,
        'a': lambda xmas, value: xmas[2] < value,
        's': lambda xmas, value: xmas[3] < value
    },
    '>': {
        'x': lambda xmas, value: xmas[0] > value,
        'm': lambda xmas, value: xmas[1] > value,
        'a': lambda xmas, value: xmas[2] > value,
        's': lambda xmas, value: xmas[3] > value
    }
}

LETTERS = list('xmas')


def eval_workflow(workflows, workflow_name, x, m, a, s):
    workflow = workflows[workflow_name]
    if workflow[0] == 'J':
        return workflow[1]
    lambada = workflow[5]
    result = (lambada((x, m, a, s), workflow[4]))
    if result:
        return workflow[1]
    ind = int(workflow_name[-1])
    return workflow_name[:-1] + str(ind + 1)


def part1(workflows: dict, data: list[tuple[int, int, int, int]]) -> int:
    total = 0
    for x, m, a, s in data:
        logging.debug((x, m, a, s))
        workflow_name = 'in1'
        found = False
        while not found:
            if workflow_name == 'A1':
                total += x + m + a + s
                found = True
            elif workflow_name == 'R1':
                found = True
            else:
                workflow_name = eval_workflow(workflows, workflow_name, x, m, a, s)
    return total


def dig(workflows, workflow_name, values, level, d):
    logging.info("%d %s %s %s", level, d, workflow_name, values)
    if workflow_name == 'A1':
        RESULTS.append((workflow_name, values))
        combinations = (values[1] - values[0] + 1) * (values[3] - values[2] + 1) * (values[5] - values[4] + 1) * (values[7] - values[6] + 1)
        # combinations = (values[1] - values[0]) * (values[3] - values[2]) * (values[5] - values[4]) * (values[7] - values[6])
        logging.info(combinations)
        return combinations
    if workflow_name == 'R1':
        return 0
    workflow = workflows[workflow_name]
    if workflow[0] == 'J':
        return dig(workflows, workflow[1], values, level+1, 'X')
    letter_index = LETTERS.index(workflow[2]) * 2
    op = workflow[3]
    value = workflow[4]
    logging.info((workflow_name, workflow[2], workflow[3], workflow[4]))
    if op == '<':
        # true
        # lower max:
        v = list(values)
        v[letter_index + 1] = min(v[letter_index + 1], value)
        left = dig(workflows, workflow[1], tuple(v), level + 1, 'L')
        #false
        next_name = workflow_name[:-1] + str(int(workflow_name[-1])+1)
        if next_name in workflows:
            v = list(values)
            v[letter_index] = max(v[letter_index], value + 1)
            right = dig(workflows, next_name, tuple(v), level + 1, 'R')
        else:
            logging.info("%s missing?", next_name)
            right=0
        return left + right
    else:
        # raise min
        v = list(values)
        v[letter_index] = max(v[letter_index], value + 1)
        left = dig(workflows, workflow[1], tuple(v), level + 1, 'l')
        #false
        next_name = workflow_name[:-1] + str(int(workflow_name[-1])+1)
        if next_name in workflows:
            v = list(values)
            v[letter_index + 1] = min(v[letter_index + 1], value)
            right = dig(workflows, next_name, tuple(v), level + 1, 'r')
        else:
            logging.info("%s missing?", next_name)
            right=0
        return left + right


def part2(workflows: dict, data: list[tuple[int, int, int, int]], min_value: int, max_value: int) -> int:
    workflow_name = 'in1'
    values = (min_value, max_value, min_value, max_value, min_value, max_value, min_value, max_value)
    result = dig(workflows, workflow_name, values, 0, '*')
    return result


def parse_input(lines) -> (list, list):
    workflows = {}
    data = []
    stage = 1
    for line in lines:
        if line == '':
            stage = 2
            continue
        if stage == 1:
            name, content = line.split('{')
            steps = re.findall(r"(([amsx])([<>])(\d+):(\w+))|(\w+)[,*}]+", content)
            ind = 1
            for step in steps:
                if step[0]:
                    param = step[1]
                    op = step[2]
                    value = int(step[3])
                    next_workflow = step[4] + '1'
                    lambada = LAMBDAS[op][param]
                    workflows[name + str(ind)] = ['I', next_workflow, param, op, value, lambada]
                    logging.debug("%s: %s", name + str(ind), ['I', next_workflow, param, op, value])
                else:
                    next_workflow = step[5] + '1'
                    workflows[name + str(ind)] = ['J', next_workflow]
                    logging.debug("%s: %s", name + str(ind), ['J', next_workflow])
                ind += 1
        elif stage == 2:
            values = [int(v) for v in re.findall(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}+", line)[0]]
            data.append(tuple(values))
    logging.info("Number of workflows: %d", len(workflows))
    return workflows, data


def test1():
    print('Test')
    lines = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".split('\n')
    workflows, data = parse_input(lines)
    result = part1(workflows, data)
    print("Part 1", 19114 == result, result)
    result = part2(workflows, data, 1, 4000)
    print("Part 2", 167409079868000 == result, result)
    #               167243992900803 off by something
    #               167642389617600
    #               167459205617600
    print(repr(RESULTS))
                    
def main():
    print('Main')
    with open('aoc2023_day19.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    workflows, data = parse_input(lines)
    result = part1(workflows, data)
    print("Part 1", result)
    # result = part2(seeds, maps)
    # print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    #main()
