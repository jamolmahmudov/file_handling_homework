def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for i in data:
        list.append(int(i))
    return list
data=open('txt_file/data01.txt')
r=data.read()
print(main(data=r))
    

# Read data from file