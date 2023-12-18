"""
Find the sum of gear ratios

Gear ratios are the product of two parts adjacent to any one star (*)
"""

#####################
#### NOT STARTED ####
######################
#####################
#### NOT STARTED ####
######################
#####################
#### NOT STARTED ####
######################
#####################
#### NOT STARTED ####
######################
#####################
#### NOT STARTED ####
######################
#####################
#### NOT STARTED ####
######################



if __name__ == "__main__":

    FILE_NAME = "engine_schematics.txt"
    parts = []  # 2D array of all parts
    valid_parts = []  # 1D array of valid parts to sum later

    # Create a 2D array
    with open(FILE_NAME) as file:
        engine = file.readlines()
    engine = [line.strip() for line in engine]

    # Go through a row to identify the beginning and ending index of a number
    for line in engine:

        # Create a row in 2D array "parts"
        parts.append([])
        char_index = 0

        while char_index < len(line):

            # set indices for part number
            if line[char_index].isdigit():
                beginning_index = char_index
                ending_index = char_index

                while True:
                    # Check for out of bounds error
                    if ending_index+1 <= len(line)-1:
                        if not line[ending_index+1].isdigit():
                            ending_index += 1
                            char_index += 1
                            break
                    else:
                        ending_index += 1
                        break
                    ending_index += 1
                    char_index += 1

                parts[-1].append(line[beginning_index:ending_index])

            char_index += 1

    # If scanned not isInt and scanned != "."
    for row_index in range(len(parts)):
        temp_parts = parts[row_index]

        # If a part exists on this row
        if len(temp_parts) > 0:
            last_index = 0
            for temp_part in temp_parts:
                # If set to true, temp_part will be added to valid parts
                valid = False

                # Get index for the part
                beginning_index = engine[row_index].index(temp_part, last_index)
                ending_index = beginning_index + len(temp_part)
                print(beginning_index, ending_index)

                # Check for symbol on the same row check
                # Set as period by default, meaning invalid
                left_char = "."
                right_char = "."
                # Find left/right characters
                if beginning_index - 1 >= 0:
                    left_char = engine[row_index][beginning_index - 1]
                if ending_index + 1 < len(engine[row_index]):
                    right_char = engine[row_index][ending_index]

                # If either left or right character is a symbol, it's a valid part
                if (not left_char.isdigit() and left_char != ".") or (not right_char.isdigit() and right_char != "."):
                    valid = True  # Same row check complete

                # Scan (beginning - 1) to (end + 1) of above rows if possible
                # Above row check
                if row_index > 0:
                    for char_index in range(len(engine[row_index - 1])):
                        if beginning_index - 1 <= char_index <= ending_index:
                            char = engine[row_index - 1][char_index]
                            if not char.isdigit() and char != ".":
                                valid = True  # Above row check complete

                # Below row check
                if row_index+1 < len(engine):
                    for char_index in range(len(engine[row_index+1])):
                        if beginning_index-1 <= char_index <= ending_index:
                            char = engine[row_index + 1][char_index]
                            if not char.isdigit() and char != ".":
                                valid = True  # Below row check complete

                # Add part to valid parts
                if valid:
                    valid_parts.append(int(temp_part))

                last_index = ending_index

    # Sum all gear ratios
    print(gear_ratios)
    print(sum(gear_ratios))
