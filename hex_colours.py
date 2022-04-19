while True:
    colors = {"ZAbsolute Zero": "#0048ba", "AliceBlue": "#f0f8ff",
              "YellowGreen": "#9acd32", "Yellow4": "#8b8b00",
              "Yellow3": "#cdcd00", "Yellow2": "#eeee00", "Yellow1": "#ffff00",
              "Yellow Pantone": "#fedf00", "Yellow Orange": "#ffae42",
              "Xanadu": "#738678"}
    choice_of_color = input("Enter a name of color:")
    if choice_of_color == " ":
        break
    elif choice_of_color in choice_of_color:
        print(colors[choice_of_color])
    else:
        print("Invalid colour name.")
        continue








