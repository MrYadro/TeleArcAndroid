filenames = [["arc","Arc"], ["arc_darker","Arc Darker"], ["arc_dark","Arc Dark"]]

def convertFromSignedHex(s):
    x = int(s,16)
    if x > 0x7FFFFFFF:
        x -= 0x100000000
    return x

for filename in filenames:
    src = open(filename[0] + ".atthemesrc", "r")
    theme = open(filename[1] + ".attheme", "w")

    for line in src:
        magicColor = line.strip().split("=")
        swapedColor = magicColor[1][-2:]+magicColor[1][1:7]
        i = convertFromSignedHex(swapedColor)
        theme.write(magicColor[0]+"="+str(i)+"\n")

    src.close()
    theme.close()
