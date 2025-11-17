# Задание 1

first_num = 9
second_num = 7.8
my_str = "start"
print(f"{first_num}.{second_num} {my_str}")
first_num = 5.2
print(f"{first_num} {type(first_num)}")
third_num = first_num + second_num
print(f"{third_num} {type(third_num)}")
first_num += 5
second_num += first_num
print(f"{first_num} {second_num}")
second_num = int(second_num)
print(f"{first_num} {second_num}")
my_str += "&stop"
print(my_str)
print(my_str * 5)
