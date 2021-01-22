def read_file_list(filename):
    evenList = []
    oddList = []

    with open(filename) as f:
        for line in f:
            # remove newline at end of line!
            line = line.strip()
            if line:
                if (int(line) % 2 == 0):
                    print(f"{line}", end=",")
                else :
                    print(f"{line}", end=",")


if __name__ == "__main__":
    read_file_list("numFile")