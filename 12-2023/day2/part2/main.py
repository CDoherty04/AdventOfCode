"""
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48.
In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
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
