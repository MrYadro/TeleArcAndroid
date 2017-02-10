filenames = ["arc", "arc_darker", "arc_dark"]

def convertFromSignedHex(s):
    x = int(s,16)
    if x > 0x7FFFFFFF:
        x -= 0x100000000
    return x

for filename in filenames:
    src = open(filename + ".atthemesrc", "r")

    theme = open(filename + ".attheme", "w")

    for line in src:
        ohh = line.split("=")

        i = convertFromSignedHex(ohh[1])
        theme.write(ohh[0]+"="+str(i)+"\n")

    src.close()
    theme.close()
