def capitalizeTitle(title):
    outStr = ""

    x = title.split()

    for char in x: 
        if len(char) > 2:
            outStr = outStr + char.title() + " "
        else:
            outStr = outStr + char.lower() + " "

    return outStr.rstrip() 

capitalizeTitle("capiTalIze tHe titLe")