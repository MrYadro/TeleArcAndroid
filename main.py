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
        magicColor = line.strip().split("=")
        swapedColor = magicColor[1][-2:]+magicColor[1][1:7]
        i = convertFromSignedHex(swapedColor)
        theme.write(magicColor[0]+"="+str(i)+"\n")

    src.close()
    theme.close()
