f = open("manifestos.txt")
n = open("manifestos-lower.txt", "w")
for line in open("manifestos.txt"):
    n.write(line.lower())