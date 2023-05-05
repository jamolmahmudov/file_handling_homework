def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=1
    list=[]
    for i in data:
        if i.isdigit():
            list.append(int(i))
            if int(i)<a:
                a=int(i)
            
            
            
    return a
data=open("txt_file/data09.txt")
r=data.read()
print(main(data=r))
# Read data from file