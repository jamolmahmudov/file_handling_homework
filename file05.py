def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=0
    b=0
    list=[]
    for i in data:
        if i.isdigit():
            a+=1
        else:
            b+=1
            
    return [a,b]
data=open("txt_file/data05.txt")
r=data.read()
print(main(data=r))


        
# Read data from file