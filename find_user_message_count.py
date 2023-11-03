from read_data import read_data
#from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    c={}
    a=0
    for i in data["messages"]:
        if i.get("id")==users_id:
            c[i.get("actor")]=(i.get("id"))
            a+=1
    print(a)
    return c
print(find_user_message_count(read_data("data/result.json"),users_id=-999814828))