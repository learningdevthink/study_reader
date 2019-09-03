str_me = "abcd"
str_arr = ["a","b","c","d"]

for s in str_arr[::]:
    print("{}".format(s), end="")
print("")
print("<< This is same >>")
for s in str_me[::]:
    print("{}".format(s), end="")
print("")