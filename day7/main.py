from utils.read import file


def part1(bag_list: list, looking_for: str) -> list:
    found_list = []
    for bag in bag_list:
        sep = bag.find(' bags contain')
        if looking_for in bag[sep:]:
            found_list.append(bag[:sep])
            found_list.extend(part1(bag_list, bag[:sep]))
    return found_list


def part2(bag_list: dict, looking_for: str):
    bag_count = 1
    for bag_type in bag_list[looking_for]:
        bag_count += bag_type[0] * part2(bag_list, bag_type[1])
    return bag_count


def reformat(bag_list: list):
    list_to_dict = {}
    for bag in bag_list:
        sep = bag.find(' bags contain')
        key = bag[:sep]
        contents = bag[sep + 14:]
        bag_instance = []
        if contents[-14:] != 'no other bags.':
            con_list = contents.split(' ')
            for i in range(0, len(con_list), 4):
                bag_num = int(con_list[i])
                bag_type = f'{con_list[i + 1]} {con_list[i + 2]}'
                bag_instance.append([bag_num, bag_type])
        list_to_dict[key] = bag_instance
    return list_to_dict


if __name__ == '__main__':
    input = file("day7")
    exampleInput = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                    "bright white bags contain 1 shiny gold bag.",
                    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                    "faded blue bags contain no other bags.",
                    "dotted black bags contain no other bags.", ]

    print("Example Part 1")
    print(f'The shiny gold bag can go in {len(set(part1(exampleInput, "shiny gold")))} bags.')
    print("------------------------------------------------------")
    print("Part 1")
    print(f'The shiny gold bag can go in {len(set(part1(input, "shiny gold")))} bags.')
    print("------------------------------------------------------")
    print("Example Part 2")
    print(f'The shiny gold bag contains {part2(reformat(exampleInput), "shiny gold") - 1} bags.')
    print("------------------------------------------------------")
    print("Part 2")
    print(f'The shiny gold bag contains {part2(reformat(input), "shiny gold") - 1} bags.')
    print("------------------------------------------------------")
