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


if __name__ == "__main__":
    print(PatternCount("ATCGTGTG", "GTG"))
