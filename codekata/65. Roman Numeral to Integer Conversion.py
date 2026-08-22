def roman_to_int(s):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    valid = {
        'I': ['V', 'X'],
        'X': ['L', 'C'],
        'C': ['D', 'M']
    }

    total = 0
    i = 0

    while i < len(s):
        if s[i] not in values:
            return -1

        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            if s[i + 1] not in valid.get(s[i], []):
                return -1

            total += values[s[i + 1]] - values[s[i]]
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total


N = input().strip()
print(roman_to_int(N))