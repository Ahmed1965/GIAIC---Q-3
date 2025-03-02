# class 02 String and fstring

name : str = "Ahmed"
print (f"My name is {name}")

a: list[str] = [i for i in  dir(str) if "--" not in i]
print(len(a))