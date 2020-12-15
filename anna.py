from regex import *


# 读文件
def read_file(path):
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


# 单行分析
def word_analysis(line):
    for match in re.finditer(patterns, line):
        match_item = match.group()
        if match.lastgroup == 'ID':
            match_item = match_item[0:10]
        yield match.lastgroup, match_item


if __name__ == '__main__':
    lines = read_file('test1.txt')

    for index, line in enumerate(lines):
        for res in word_analysis(line):
            print("line %d :" % (index+1), res)
