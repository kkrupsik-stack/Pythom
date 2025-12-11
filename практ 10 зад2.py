def punct(txt):

    target_chars = {'!', '?', '.', ',', '('}
    

    count = 0
  
    for char in txt:
        if char in target_chars:
            count += 1
    
  
    return count

print(punct('(Как дела?)'))  
