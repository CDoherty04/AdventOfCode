"""
Determine which games would have been possible if the bag had been loaded with only:
12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?

INPUT:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

OUTPUT:
1 + 2 + 5 = 8
"""

if __name__ == "__main__":

    total = 0

    with open("data.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for i in range(len(lines)):
        game_num = i + 1
        valid = True

        # List of comma separated die selections
        hands = lines[i].split(":")[1].strip().split(";")

        for hand in hands:
            items = hand.split(",")
            items = [item.strip() for item in items]

            for item in items:
                values = item.split(" ")

                # 12 red cubes, 13 green cubes, and 14 blue cubes.
                if values[1] == "red" and int(values[0]) > 12:
                    valid = False

                if values[1] == "green" and int(values[0]) > 13:
                    valid = False

                if values[1] == "blue" and int(values[0]) > 14:
                    valid = False

        if valid:
            total += game_num

    print(total)
