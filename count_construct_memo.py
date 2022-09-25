def count_construct(target: str, words: list[str], memo: dict[str, int] | None = None) -> int:

    count = 0

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    for word in words:
        if target.startswith(word):
            word_len = len(word)
            remainder = target[word_len:]
            result = count_construct(remainder, words, memo)
            count += result

    memo[target] = count
    return count


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "aka", "sk", "boar"]))  # 0
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeeeeeee",
]))  # 0
