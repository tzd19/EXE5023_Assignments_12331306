#5.1
def find_operations(expression, current_index, current_value, target, result):
    if current_index == len(expression):
        if current_value == target:
            result.append(expression)
        return
    for i in range(current_index, len(expression)):
        for operator in ['+', '-']:
            new_expression = expression[:current_index] + operator + expression[current_index:i] + expression[i:]
            new_value = eval(new_expression)  # 计算新表达式的值
            find_operations(new_expression, i + 2, new_value, target, result)
def find_expression(target):
    result = []
    initial_expression = "123456789"
    find_operations(initial_expression, 0, 0, target, result)
    return result
find_expression(50)
#5.2
import numpy as np
Total_solutions = [0] * 100  # 列表索引从0到100
print(Total_solutions)
for i in range(1,101):
    expressions = find_expression(i)
    if expressions:
        Total_solutions[i-1] = len(expressions)
print(Total_solutions)
# 找到产生总数最大和最小的数字
max_solutions = np.max(Total_solutions)
index_of_max=1 + Total_solutions.index(max_solutions)
min_solutions = np.min(Total_solutions)
index_of_min=1 + Total_solutions.index(min_solutions)

print(f"数字{index_of_max}产生Total_solutions的最大值: {max_solutions}")
print(f"数字{index_of_min}产生Total_solutions的最小值: {min_solutions}")