def can_construct(target: str, words: list[str], memo: dict[str, bool] | None = None) -> bool:
    
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    
    if target == "":
        return True
    
    for word in words:
        if target.startswith(word):
            l = len(word)
            remainder = target[l:]
            result = can_construct(remainder, words, memo)

            if result:
                memo[target] = True
                return True
    
    memo[target] = False
    return False

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "aka", "sk", "boar"])) # False
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeeeeeee",
])) # False



