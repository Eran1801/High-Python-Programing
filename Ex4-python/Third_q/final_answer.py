import collections

abc = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
       'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
       'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}


def morse_encode(word: str) -> str:
    return ''.join(abc[i] for i in word)


# gets the first input, the morse code without spaces
morse = input()
# dict : {morse_code :number of times that he showed}, because: cats = _._..__..., text = _._..__...
words = collections.Counter()

# getting the amount of words and the words themselves
for i in range(int(input())):
    words[morse_encode(input())] += 1

# contains in index i the number of possibilities to decode the prefix of length i
num_of_possib = [0 for _ in range(len(morse) + 1)]

# index zero start with 1 because the empty string which has a single encoding
num_of_possib[0] = 1

for prefix_len in range(1, len(morse) + 1):
    for gap_len in range(1, min(76, len(morse) + 1)):
        gap = morse[prefix_len - gap_len:prefix_len]
        if gap in words:
            num_of_possib[prefix_len] += words[gap] * num_of_possib[prefix_len - gap_len]

# print the last value which is the most possibilities to encode morse variable
print(num_of_possib[-1])
