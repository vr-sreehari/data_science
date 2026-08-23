S = input()

res = ""

for ch in S:
    res += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))

print(res)