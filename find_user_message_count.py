from read_data import read_data
from find_all_users_id import find_all_users_id as ids

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
    for i in data["messages"]:
        if "from_id" in i and "channel" not in i['from_id']:
            c[i['from_id']]=c.get(i['from_id'],0)+1
    return c
data=read_data("data/result.json")
ids=ids(data)
print(find_user_message_count(data,ids))