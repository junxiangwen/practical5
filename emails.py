NAME = []
email = input("Your Email:").split("@")
while email != " ":
    the_first_part = " ".join((str(email[0])).tital()).split(".")
    name = str(input("is it your name{}?(Y/N)".format(the_first_part))
    if name == "N":
        your_name=input("your name is:")
        NAME[your_name] = "@".join(email)
    elif name == "Y":
        NAME[the_first_part] = "@".join(email)
    email = input("Your Email:").split("@")
    print({},{}.format(name,email))






