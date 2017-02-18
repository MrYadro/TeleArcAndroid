filenames = [["arc","Arc"], ["arc_darker","Arc Darker"], ["arc_dark","Arc Dark"], ["colors", "Converted"]]

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
        if magicColor[0] == "switchTrack" or magicColor[0] == "switchTrackChecked":
            swapedColor = "88"+magicColor[1][1:7]
        elif magicColor[0] == "chat_selectedBackground":
            swapedColor = "66"+magicColor[1][1:7]
        elif magicColor[0] == "chat_messagePanelVoiceShadow":
            swapedColor = "D0"+magicColor[1][1:7]
        elif magicColor[0] == "contextProgressInner1" or magicColor[0] == "contextProgressInner2":
            swapedColor = "41"+magicColor[1][1:7]
        else:
            swapedColor = magicColor[1][-2:]+magicColor[1][1:7]
        i = convertFromSignedHex(swapedColor)
        theme.write(magicColor[0]+"="+str(i)+"\n")

    src.close()
    theme.close()
