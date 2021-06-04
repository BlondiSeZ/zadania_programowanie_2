with open("pantadeusz.txt", "r") as readfile:
    for lines in readfile:
        print(lines.rsplit("\n"))