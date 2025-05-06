def num_of_words(text):
    return len(text.split())

def sort_on(dict):
    return dict["num"]

def num_of_chars(text):
    my_list = list(text.lower())

    #initialize dict with list and 0.  this will have all characters once (because of set) and num initialized to 0
    my_dict = dict.fromkeys(set(my_list), 0)

    #loop through text (my list) and then loop through dict to find match then add 1
    for char in my_list :
        for n in my_dict:
            if char == n:
                my_dict[n] +=1   
                break 
    return my_dict

def sort_dict(my_dict):
    sorted_list =[]
    for char in my_dict:
        if char.isalpha():
            sorted_list.append({"char":char, "num":my_dict[char]})
            
    return sorted_list
