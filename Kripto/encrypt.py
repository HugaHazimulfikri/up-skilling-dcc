alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"

pean = "DNCC{r3v3rs1ng_cust0m_m4th_c1ph3r}"
shift = 17
out = ""

for c in plain:
    if c in alphabet:
        out += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
    else:
        out += c

print("Ciphertext:", out)