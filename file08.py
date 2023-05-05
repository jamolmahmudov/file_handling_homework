def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=0
    list=[]
    for i in data:
        if i.isdigit():
            list.append(int(i))
            if int(i)>a:
                a=int(i)
            
            
            
    return a
data=open("txt_file/data08.txt")
r=data.read()
print(main(data=r))



# Read data from file