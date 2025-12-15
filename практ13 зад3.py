def bin_sys(start, end):

    total_sum = 0

    for num in range(start, end + 1):

        print(bin(num)[2:])

        total_sum += num
    
    print(f"сумма: {bin(total_sum)[2:]}")

bin_sys(3, 6)
