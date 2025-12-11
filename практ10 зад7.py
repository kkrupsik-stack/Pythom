def custom_filter(data_list):

    total_sum = 0

    for item in data_list:

        if isinstance(item, int):
   
            if item % 7 == 0:
                total_sum += item 

    print(f"сумма: {total_sum}")

    return total_sum <= 83

print(custom_filter([7, 10.5, 'txt', 14, 2, 56]))
