str1 = "Line1-abcdef \n Line2-abc \n Line3-def \nLine4-ads"
substrings= ['ab', 'bc', 'cd', 'de', 'ef']
str2= ""

# join函数：
# 以下的方法拼接字符串效率很低，所以我们一般用join方法来实现字符串的拼接
for substring in substrings:
    str2 += substring
print('字符串：', str2)
str2 = ', 
'.join(substrings)
print('字符串：', str2)

# count函数：用于统计字符串里某个字符或子字符串出现的次数。可选参数为在字符串搜索的开始与结束位置
# 语法：str.count(sub, start=0, end=len(string))
print('count:', str1.count(' '))

# split函数：通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
# 语法：str.split(sep="", num=string.count(str))
print(str1.split())
print(str1.split(' ', 2))
print(str1.split(' ', 1))