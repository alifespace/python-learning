from openai import OpenAI

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key="sk-94c3efc401af4b87be01a4ecce532bcc", base_url="https://api.deepseek.com")
print(client.models.list())

# 生成格式化显示九九乘法表
def generate_multiplication_table():
    table = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            table += f"{j}*{i}={i*j}\t"
        table += "\n"
    return table

# 调用函数生成九九乘法表
multiplication_table = generate_multiplication_table()
print(multiplication_table)

# 生成九九乘法表，并格式化显示
def generate_multiplication_table():
    table = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            table += f"{j}*{i}={i*j}\t"
        table += "\n"
    return table

# 调用函数生成九九乘法表
multiplication_table = generate_multiplication_table()
print(multiplication_table)

# 对象封装
print()

# 序列化和反序列化
# 序列化是指将对象转换为可存储或可传输的格式，反序列化是指将序列化的对象转换为原始对象
# 序列化是指将对象转换为可存储或可传输的格式，反序列化是指将序列化的对象转换为原始对象
# 序列化是指将对象转换为可存储或可传输的格式，反序列化是指将序列化的对象转换为原始对象
# 乘法表
def generate_multiplication_table():
    table = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            table += f"{j}*{i}={i*j}\t"
        table += "\n"
    return table

# 序列化是
