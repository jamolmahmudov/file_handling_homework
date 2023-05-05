def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    a=data.split('\n')
    for i in a:
        list.append(len(i))
     
    return list
data=open("txt_file/data06.txt")
r=data.read()
print(main(data=r))
# Read data from file