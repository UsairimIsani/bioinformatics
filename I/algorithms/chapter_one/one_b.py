# Attempt One
# def frequent_count(text, pattern):
#     count = 0
#     len_f_text = len(text)
#     len_f_pattern = len(pattern)
#     ran = len_f_text-len_f_pattern
#     for p in range(0, ran+1):
#         st_sl = text[p:p+len_f_pattern]
#         if(st_sl == pattern):
#             count = count+1
#     return count


# Attempt Two
# import operator
# def FrequentWords(text, k):
#     len_f_text = len(text)
#     ran = len_f_text-k
#     freq_cou = dict()
#     for p in range(0, ran+1):
#         st_sl = text[p:p+k]
#         freq = freq_cou.get(st_sl)+1 if freq_cou.get(st_sl) else 1
#         freq_cou[st_sl] = freq
#     ma = max(freq_cou.items(), key=operator.itemgetter(1))
#     return ma


# Attempt Three
def PatternCount(text, pattern):
    count = 0
    len_f_text = len(text)
    len_f_pattern = len(pattern)
    ran = len_f_text-len_f_pattern
    for p in range(0, ran+1):
        st_sl = text[p:p+len_f_pattern]
        if(st_sl == pattern):
            count = count+1
    return count


def FrequentWords(text, k):
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
    print(FrequentWords("ATCGTGTG", 2))
