def upper(t):
    result = ""  
    for char in t: 
        if char.isupper(): 
            result += char  
    if result:  
        print(result)  
    else:  
        pass 

upper('PriVet') 
