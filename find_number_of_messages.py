from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    c=0
    ls=[]
    for i in data["messages"]:
        if i['text']!="" :
            c+=1
            ls.append(i['text'])
    print(ls) 
    return c
print(find_number_of_messages(read_data("data/result.json")))