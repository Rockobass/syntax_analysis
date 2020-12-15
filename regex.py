import re

# # 关键词
# Keyword = r'(?P<Keyword>(main){1}|(double){1}|(int){1}|(void){1}|(if){1}|(else){1}|' \
#                   r'(end){1}|(return){1}|(char){1})'


# # 运算符
# Operator = r'(?P<Operator>\+\+|\+=|\+|--|-=|-|\*|\*=|/=|/|%=|%|==|=|!=|!|&&|&)'

# # 分隔符/界符
# Separator = r'(?P<Separator>[,:\{};)(<>])'

# # 常数
# Constant = r"(?P<Constant>(\d+[.]?\d+)|('\D*')|(\d+))"




# # 变量名 不能使用关键字命名
# ID = r'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'

# # 方法名 {1} 重复n次
# Method = r'(?P<Method>(main){1}|(printf){1}|(cout){1}|(cin){1})'

# nonedefine = r'(?P<None_define>[\S*])'

# patterns = re.compile('|'.join([Keyword, Type, Method, ID, Number, Separator, Operator, nonedefine]))


Keyword = r'(?P<Keyword>(main){1}|(end){1})'

Type = r'(?P<Type>(int){1}|(double){1}|(float){1})'

EQ = r'(?P<EQ>=)'

Operator = r'(?P<Operator>\+|-|\*|/|%)'

Separator = r'(?P<Separator>[,:;])'

Number = r"(?P<Number>(\d+[.]?\d+)|(\d+))"

ID = r'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'


nonedefine = r'(?P<None_define>[\S*])'

patterns = re.compile('|'.join([Keyword, Type, EQ, ID, Number, Separator, Operator, nonedefine]))