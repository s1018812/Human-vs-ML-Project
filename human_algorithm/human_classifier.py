def human_classify(odor): 
    if odor == 'a':  
        return 'edible' 
    elif odor == 'l': 
        return 'edible' 
    elif odor == 'n': 
        return 'edible' 
    else: 
        return 'poisonous'

print(human_classify('a'))  # Should return 'edible'