from one_a import PatternCount


def FrequentWords(text, k):
    k = int(k)
    kmers = set()
    for i in range(0, len(text)-k+1):
        kmers.add(text[i:i+k])
    freq = set()
    for i in kmers:
        freq.add((i, PatternCount(text, i)))
    maxmers = {}
    max_sq = max(freq, key=lambda a: a[1])
    for i in freq:
        if i[1] == max_sq[1]:
            maxmers[i[0]] = i[1]
    return maxmers


if __name__ == "__main__":
    pass
