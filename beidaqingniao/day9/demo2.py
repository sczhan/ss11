f = open("1.txt", "r+",)
# print("欢迎使用Python", file=f)
# f.write("hello欢迎")
# f.writelines(["cs", "b萨克斯b"])
# f.writelines(["\ncs", "\nb萨克斯b"])
# t = f.read()
# print(type(t), t)
# t1 = f.read(10)
# print(type(t1), t1)

# t2 = f.readline()
# print(type(t2), t2)

t3 = f.readlines()
print(type(t3), t3)
f.close()