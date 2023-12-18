"""
For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48.
In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.
"""

if __name__ == "__main__":

    powers = []
    total = 0

    # Get data
    with open("data.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    # For every game/line in data
    for i in range(len(lines)):

        max_red = 0
        max_green = 0
        max_blue = 0

        game_num = i + 1
        valid = True

        # List of comma separated die selections
        hands = lines[i].split(":")[1].strip().split(";")

        # Parsing
        for hand in hands:
            items = hand.split(",")
            items = [item.strip() for item in items]

            # More parsing
            for item in items:
                values = item.split(" ")

                # 12 red cubes, 13 green cubes, and 14 blue cubes.
                if values[1] == "red":
                    if int(values[0]) > max_red:
                        max_red = int(values[0])
                    if int(values[0]) > 12:
                        valid = False

                if values[1] == "green":
                    if int(values[0]) > max_green:
                        max_green = int(values[0])
                    if int(values[0]) > 13:
                        valid = False

                if values[1] == "blue":
                    if int(values[0]) > max_blue:
                        max_blue = int(values[0])
                    if int(values[0]) > 14:
                        valid = False

        powers.append(max_red*max_green*max_blue)
        if valid:
            total += game_num

    print(f"{sum(powers)} is the sum of powers")
    print(f"{total} is the total")
