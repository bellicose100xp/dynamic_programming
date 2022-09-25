def all_construct(target: str, words: list[str], memo: dict[str, list[list[str]]] | None = None) -> list[list[str]]:

    ways_to_construct: list[list[str]] = []

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    for word in words:
        if target.startswith(word):

            word_len = len(word)
            remainder = target[word_len:]
            
            result = all_construct(remainder, words, memo)
            
            for word_arr in result:
                    ways_to_construct.append([word, *word_arr])
                
    memo[target] = ways_to_construct
    return ways_to_construct


print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # [["abc", "def"]]
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # [["ab", "cd", "ef"], ["ab", "c", "def"], ["abc", "def"], ["abcd", "ef"]]
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))  # [["purp", "le"], ["p", "ur", "p", "le"]]
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "aka", "sk", "boar"]))  # []
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # [...]
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeeeeeee",
]))  # []
