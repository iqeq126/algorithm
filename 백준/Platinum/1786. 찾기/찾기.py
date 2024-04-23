def kmp_table(pattern):
    table = [0 for i in range(0, len(pattern))]

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table



def knuth_morris_pratt(pattern, word):
    table = kmp_table(pattern)
    count, pattern_idx = 0, 0
    result_list = []

    for idx in range(len(word)):
        while pattern_idx > 0 and word[idx] != pattern[pattern_idx]:
            pattern_idx = table[pattern_idx-1]

        if word[idx] == pattern[pattern_idx]:
            if pattern_idx == len(pattern)-1:
                result_list.append(idx-len(pattern)+2)
                count += 1
                pattern_idx = table[pattern_idx]
            else:
                pattern_idx += 1

    print(count)
    return result_list

t_string = input()
p_string = input()
print(*knuth_morris_pratt(p_string, t_string))