STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    with open(file, 'r') as praise:
        song = praise.read()
        # print(song)

    new_words = song.lower().replace('.',' ').replace(',',' ').replace('?',' ').split()

    counted_words = []

    for word in new_words:
        if word not in STOP_WORDS:
            counted_words.append(word)
            #print(counted_words)

    i = {}

    for word in counted_words:
        if word not in i.keys():
            i[word] = 1
        else:
            i[word] += 1
    
    print(i)




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)