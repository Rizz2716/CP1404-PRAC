color_name={"ALICEBLUE": "#f0f8ff","ANTIQUEWHITE": "#faebd7","BEIGE": "#f5f5dc","BLUEVIOLET": "#8a2be2","BROWN": "#a52a2a","BURYWOOD": "#deb887","CADETBLUE": "#5f9ea0","CHOCOLATE": "#d2691e","CORAL": "#ff7f50","CORNFLOWERBBLUE": "#6495ed"}

color = input("Enter color name: ").upper()
while color != "":
    if color in color_name:
        print(color, "is", color_name[color])
    else:
        print("Invalid color name")
    color = input("Enter color name: ")