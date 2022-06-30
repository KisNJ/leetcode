def encode(strs):
    decode(":;".join(strs))
    #return ":;".join(strs)
def decode(str):
    print(str.split(":;"))
print(encode(["we", "say", ":", "yes"]))