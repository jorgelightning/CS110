#1 Recursive Printing - print_upto_n(num)
def print_upto_n(num):
    if num == 0:
        return
    else:
        print(num)
        print_upto_n(num-1)
print('#1 Recursive Printing - print_upto_n(num)')
print_upto_n(5)

#2 Recursive Multiplication - rec_mul(x, y) 
def rec_mul(x, y):
    if y == 0:
        return 0
    else:
        return x + rec_mul(x, y - 1)
print('#2 Recursive Multiplication - rec_mul(x, y) ')
print(rec_mul(2,2))

#3 Recursive Lines - rec_n_asterisks (n)
def rec_n_asterisks(n):
    if n > 0:
        print('*'*n)
        rec_n_asterisks(n-1)
print('#3 Recursive Lines - rec_n_asterisks (n)')
rec_n_asterisks(3)

#4 Largest List Item - largest_in_list(input_list)
def largest_in_list(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        new_list = input_list[0:-1]
        current_max = largest_in_list(new_list)
        if input_list[-1] > current_max:
            return input_list[-1]
        else:
            return current_max
print('#4 Largest List Item - largest_in_list(input_list)')
input_list = [1,2,3,4,5]
print(largest_in_list(input_list))

#5 Recursive List Sum - rec_list_sum(input_list)
def rec_list_sum(input_list):
    if len(input_list) == 0:
        return 0
    else:
        return input_list[0] + rec_list_sum(input_list[1:])
input_list = [100, 200, 300, 400, 500]
print('#5 Recursive List Sum - rec_list_sum(input_list)')
print(input_list)
print(rec_list_sum(input_list))

#6 Sum of Numbers - rec_sum_to_n(num) 
def sum_up_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_up_to_n(n - 1)
print('#6 Sum of Numbers - rec_sum_to_n(num) ')
print(sum_up_to_n(2))


#7 Recursive Power Method rec_power(num, exponent)
def rec_power(num, exponent):
  if exponent == 0:
    return 1
  else:
    return num * rec_power(num, exponent - 1)

num = 2
exponent = 4
print('#7 Recursive Power Method rec_power(num, exponent)')
print(rec_power(num, exponent))
