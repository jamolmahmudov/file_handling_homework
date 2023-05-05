def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    for i in data:
        if i.isdigit():
            a+=int(i)
            
    return a
data=open("txt_file/data07.txt")
r=data.read()
print(main(data=r))
#     n = 0
#     for i in data:
#         if i.isdigit():
#             n += int(i)
#     return n
# data=open('txt_file/data07.txt')
# r=(data).read()

# print(main(data=r))
# Read data from file