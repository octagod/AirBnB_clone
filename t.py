'''Test'''
# BaseModel.update(ab4225f3-2e71-4804-8d5c-0ddf08d21a9d, name, Nicklaus)


def reg_split(line):
    '''Parse line'''
    if "(" in line and ")" in line:
        x = line.split(".")[1].split("(")[0]
        if f".{x}(" in line:
            line = line.replace(f".{x}(", " ").replace(")", "")
            if "," in line:
                line = line.replace(",", "")
            if "{" in line:
                line = line.replace("{", "").replace("}", "").replace(":", "")
    return line.split(" ")


# def reg_split(line):
#     x = line.split(".")[1].split("(")[0]
#     if f".{x}(" in line:
#         line = line.replace(f".{x}(", " ")
#         line = line.replace(")", "")
#     command = line.split(" ")
#     return command


# if ".show(" in line:
#     line = line.replace(".show(", " ")
#     line = line.replace(")", "")
print(reg_split("Classname id"))
print(reg_split("Classname.show(id)"))
print(reg_split("BaseModel.show(123gsh-y3utb3-yu2ebka0-9374)"))
print(reg_split("BaseModel.update(ab4225f3-2e71-4804-8d5c-0ddf08d21a9d," +
                "name, Nicklaus)"))
print(reg_split("User.update(User1, {attribute: email@email.com})"))
print(reg_split("User some_id attribute value@gmail.com"))
