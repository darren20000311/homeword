import sys


def main(files):
    """
    Summarizes Poems
    """
    print(files)
    # Try blocks to handle possible failures
    try:
        out = open("results.txt", "w")
    except OSError as e:
        print("Can't open results.txt for writing")
        exit()

    for filename in files:
        try:
            f = open(filename, "r", encoding="utf-8")
        except OSError as e:
            print(f"Can't open {filename}")
            exit()

        title = f.readline().strip()

        # This line splits the byline and removes the word "By"
        author = ' '.join(f.readline().strip().split()[1:])

        line_count = 0
        for line in f:
            if len(line) > 1:
                line_count += 1

        out.write("Processed poem:\n")
        out.write(f"Title: {title}\n")
        out.write(f"Author: {author}\n")
        out.write(f"Line count: {line_count}\n")
        out.write("\n")

        f.close()


main(sys.argv[1:])