def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for i in data:
        if i.isdigit():
            list.append(i)
    return list
data=open("txt_file/data03.txt")
r=data.read()
print(main(data=r))

# Read data from file
