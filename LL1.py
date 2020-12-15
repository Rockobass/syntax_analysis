from prettytable import PrettyTable
from anna import *

"""
文法:
    <MAIN> -> main:<BLOCK>end
    <BLOCK> -> <DEC>;<BLOCK>|<FORMULA>;<BLOCK>|e (e为空)
    <DEC> -> type<IDLIST>
    <IDLIST> -> id<IDN>
    <IDN> -> ,id<IDN>|e
    <FORMULA> -> id=<CALCULATIONS>
    <CALCULATIONS> -> <OBJ><CAL>
    <CAL> -> op<OBJ><CAL>|e
    <OBJ> -> id|num
    
    num -> [0-9]*|[0-9]+.[0-9]+
    type -> int|float|double
    id -> [a-zA-Z_][a-zA-Z_0-9]*
    op -> +|-|*|/
"""
"""
FIRST集
    FIRST(MAIN) = { main }
    FIRST(BLOCK) = { e type id}
    FIRST(DEC) = { type }
    FIRST(IDLIST) = { id }
    FIRST(IDN) = { , e}
    FIRST(FORMULA) = { id }
    FIRST(CALCULATIONS) = { id num }
    FIRST(CAL) = { op e }
    FIRST(OBJ) = { id num } 
"""
"""
FOLLOW集
    FOLLOW(MAIN) = { # }
    FOLLOW(BLOCK) = { end type id }
    FOLLOW(DEC) = { ; }
    FOLLOW(IDLIST) = { ; }
    FOLLOW(IDN) = { ; }
    FOLLOW(FORMULA) = { ; }
    FOLLOW(CALCULATIONS) = { ; }
    FOLLOW(CAL) = { ; op }
    FOLLOW(OBJ) = { ; op }
"""
"""
SELECT集
    SELECT(MAIN) = { main }
    SELECT(BLOCK) = { end type id }
    SELECT(DEC) = { type }
    SELECT(IDLIST) = { id }
    SELECT(IDN) = { , ; }
    SELECT(FORMULA) = { id }
    SELECT(CALCULATIONS) = { id num }
    SELECT(CAL) = { op ; }
    SELECT(OBJ) = { id num }
"""
"""
LL(1)分析表
+-------------------+-----------------+---+-----+---+--------------+-------------------+------------+---------------+----------+---+---+
| 非终结符\输入符号 |       main      | : | end | = |      op      |         id        |    num     |      type     |    ,     | ; | # |
+-------------------+-----------------+---+-----+---+--------------+-------------------+------------+---------------+----------+---+---+
|        MAIN       | main:<BLOCK>end |   |     |   |              |                   |            |               |          |   |   |
|       BLOCK       |                 |   |  e  |   |              | <FORMULA>;<BLOCK> |            | <DEC>;<BLOCK> |          |   |   |
|        DEC        |                 |   |     |   |              |                   |            |  type<IDLIST> |          |   |   |
|       IDLIST      |                 |   |     |   |              |      id<IDN>      |            |               |          |   |   |
|        IDN        |                 |   |     |   |              |                   |            |               | ,id<IDN> | e |   |
|      FORMULA      |                 |   |     |   |              | id=<CALCULATIONS> |            |               |          |   |   |
|    CALCULATIONS   |                 |   |     |   |              |     <OBJ><CAL>    | <OBJ><CAL> |               |          |   |   |
|        CAL        |                 |   |     |   | op<OBJ><CAL> |                   |            |               |          | e |   |
|        OBJ        |                 |   |     |   |              |         id        |    num     |               |          |   |   |
+-------------------+-----------------+---+-----+---+--------------+-------------------+------------+---------------+----------+---+---+

+-------------------+-------------------------+---+------------+---+---------------------+------------------------------+----------------------------+------------------------+-----------------+----------+-------+
| 非终结符\输入符号 |           main          | : |    end     | = |          op         |              id              |            num             |          type          |        ,        |    ;     |   #   |
+-------------------+-------------------------+---+------------+---+---------------------+------------------------------+----------------------------+------------------------+-----------------+----------+-------+
|        MAIN       | <MAIN>->main:<BLOCK>end |   |            |   |                     |                              |                            |                        |                 |          | synch |
|       BLOCK       |                         |   | <BLOCK>->e |   |                     |  <BLOCK>-><FORMULA>;<BLOCK>  |                            | <BLOCK>-><DEC>;<BLOCK> |                 |          |       |
|        DEC        |                         |   |            |   |                     |                              |                            |     type$<IDLIST>      |                 |  synch   |       |
|       IDLIST      |                         |   |            |   |                     |      <IDLIST>->id<IDN>       |                            |                        |                 |  synch   |       |
|        IDN        |                         |   |            |   |                     |                              |                            |                        | <IDN>->,id<IDN> | <IDN>->e |       |
|      FORMULA      |                         |   |            |   |                     | <FORMULA>->id=<CALCULATIONS> |                            |                        |                 |  synch   |       |
|    CALCULATIONS   |                         |   |            |   |                     |  <CALCULATIONS>-><OBJ><CAL>  | <CALCULATIONS>-><OBJ><CAL> |                        |                 |  synch   |       |
|        CAL        |                         |   |            |   | <CAL>->op<OBJ><CAL> |                              |                            |                        |                 | <CAL>->e |       |
|        OBJ        |                         |   |            |   |        synch        |          <OBJ>->id           |         <OBJ>->num         |                        |                 |  synch   |       |
+-------------------+-------------------------+---+------------+---+---------------------+------------------------------+----------------------------+------------------------+-----------------+----------+-------+
"""
tb = PrettyTable()
tb.field_names = [r"非终结符\输入符号", "main", ":", "end", "=", "op", "id", "num", "type", ",", ";", "#"]
tb.add_row(["MAIN", "main$:$<BLOCK>$end", " ", " ", " ", " ", " ", " ", " ", " ", " ", "synch"])
tb.add_row(["BLOCK", " ", " ", "e"," ", " ", "<FORMULA>$;$<BLOCK>"," ","<DEC>$;$<BLOCK>", " ", " ", " "])
tb.add_row(["DEC", " ", " ", " ", " ", " ", " ", " ", "type$<IDLIST>", " ", "synch", " "])
tb.add_row(["IDLIST", " ", " ", " ", " ", " ", "id$<IDN>", " ", " ", " ", "synch", " "])
tb.add_row(["IDN", " ", " ", " ", " ", " ", " ", " ", " ", ",$id$<IDN>", "e", " "])
tb.add_row(["FORMULA", " ", " ", " ", " ", " ", "id$=$<CALCULATIONS>", " ", " ", " ", "synch", " "])
tb.add_row(["CALCULATIONS", " ", " ", " ", " ", " ", "<OBJ>$<CAL>", "<OBJ>$<CAL>", " ", " ", "synch", " "])
tb.add_row(["CAL", " ", " ", " ", " ", "op$<OBJ>$<CAL>", " ", " ", " ", " ", "e", " "])
tb.add_row(["OBJ", " ", " ", " ", " ", "synch", "id", "num", " ", " ", "synch", " "])
# tb = PrettyTable()
# tb.field_names = [r"非终结符\输入符号", "main", ":", "end", "=", "op", "id", "num", "type", ",", ";", "#"]
# tb.add_row(["MAIN", "<MAIN>->main:<BLOCK>end", " ", " ", " ", " ", " ", " ", " ", " ", " ", "synch"])
# tb.add_row(["BLOCK", " ", " ", "<BLOCK>->e"," ", " ", "<BLOCK>-><FORMULA>;<BLOCK>"," ","<BLOCK>-><DEC>;<BLOCK>", " ", " ", " "])
# tb.add_row(["DEC", " ", " ", " ", " ", " ", " ", " ", "type$<IDLIST>", " ", "synch", " "])
# tb.add_row(["IDLIST", " ", " ", " ", " ", " ", "<IDLIST>->id<IDN>", " ", " ", " ", "synch", " "])
# tb.add_row(["IDN", " ", " ", " ", " ", " ", " ", " ", " ", "<IDN>->,id<IDN>", "<IDN>->e", " "])
# tb.add_row(["FORMULA", " ", " ", " ", " ", " ", "<FORMULA>->id=<CALCULATIONS>", " ", " ", " ", "synch", " "])
# tb.add_row(["CALCULATIONS", " ", " ", " ", " ", " ", "<CALCULATIONS>-><OBJ><CAL>", "<CALCULATIONS>-><OBJ><CAL>", " ", " ", "synch", " "])
# tb.add_row(["CAL", " ", " ", " ", " ", "<CAL>->op<OBJ><CAL>", " ", " ", " ", " ", "<CAL>->e", " "])
# tb.add_row(["OBJ", " ", " ", " ", " ", "synch", "<OBJ>->id", "<OBJ>->num", " ", " ", "synch", " "])
# projection = {
#     "<MAIN>": 0,
#     "<BLOCK>": 1,
#     "<DEC>": 2,
#     "<IDLIST>": 3,
#     "<IDN>": 4,
#     "<FORMULA>": 5,
#     "<CALCULATIONS>": 6,
#     "<CAL>": 7,
#     "<OBJ>": 8
# }

projection_v = [
    "<MAIN>",
    "<BLOCK>",
    "<DEC>",
    "<IDLIST>",
    "<IDN>",
    "<FORMULA>",
    "<CALCULATIONS>",
    "<CAL>",
    "<OBJ>",
    "type",
    "id",
    "num",
    "op"
]


def get_input():
    lines = read_file('test1.txt')
    input_list = []
    for index, line in enumerate(lines):
        for res in word_analysis(line):
            if res[0] != "None_define":
                input_list.append(res)
    return input_list


def get_stack_str(stack):
    res = ""
    s = stack.copy()
    s.reverse()
    for i in range(0,len(s)):
        res += s[i]
    return res


def get_input_str(list):
    res = ""
    for i in range(0, len(list)):
        res += list[i][1]+" "
    return res


# 判断是否为非终结符
def v_index(top):
    for i in range(0, len(projection_v)):
        if top == projection_v[i]:
            return i
    return 100


def add_row(tb1, step1, stack1_str, input1_str, output1_str):
    tb1.add_row([step1, stack1_str, input1_str, output1_str])


if __name__ == '__main__':
    # 输入缓冲区
    input_list = get_input()
    input_list.append(("Separator","#"))
    # 栈
    stack = ["#", "<MAIN>"]
    # 输出
    output_tb = PrettyTable()
    output_tb.field_names = ["步骤", "栈", "剩余输入", "输出"]

    print(tb)
    step = 1
    output_str = " "
    add_row(output_tb,step,get_stack_str(stack),get_input_str(input_list),output_str)
    while True:
        if len(stack)==1 and stack[0]=="#" and len(input_list)==1 and input_list[0][1]=="#":
            break

        if len(input_list) == 0:
            break
        # 分析步数
        step += 1
        # 栈顶元素
        top = stack[len(stack)-1]
        # 当前输入
        first = input_list[0][1]
        index = v_index(top)

        # 如果栈顶是终结符
        if index == 100:
            # 错误检测
            # 3.栈顶终结符与输入符号不匹配，弹出栈顶终结符
            if top != first:
                output_str = "error，弹出栈顶终结符 " + top
                add_row(output_tb,step,get_stack_str(stack),get_input_str(input_list),output_str)
                stack.pop()
                continue
            # 终结符匹配上，弹出栈
            else:
                output_str = " "
                input_list.remove(input_list[0])
                stack.pop()
                add_row(output_tb, step, get_stack_str(stack), get_input_str(input_list), output_str)
                continue
        # 如果栈顶是非终结符
        else:
            if top == "num" or top == "id" or top == "op" or top == "type":
                output_str = top + "->" + first
                stack.pop()
                stack.append(first)
                add_row(output_tb, step, get_stack_str(stack), get_input_str(input_list), output_str)
                continue
            start = index
            end = start + 1
            fields = []
            t = input_list[0][1]
            s = input_list[0][0]
            if s == "ID":
                fields.append("id")
            elif s == "Number":
                fields.append("num")
            elif s == "Type":
                fields.append("type")
            elif s == "Keyword" or s == "Separator" or s == "EQ":
                fields.append(t)
            elif input_list[0][0] == "Operator":
                fields.append("op")
            expression = tb.get_string(fields=fields, start=start, end=end, header=False, border=False).strip()

            # 错误检测
            # 1.如果M[A,a]为空，则忽略a
            if len(expression) == 0:
                output_str = "error，ignore " + input_list[0][1].__str__()
                add_row(output_tb, step, get_stack_str(stack), get_input_str(input_list), output_str)
                input_list.remove(input_list[0])
                continue
            # 2.如果M[A,a]为synch，弹出A，继续分析
            elif expression == "synch":
                output_str = "error，pop " + top
                add_row(output_tb, step, get_stack_str(stack), get_input_str(input_list), output_str)
                stack.pop()
                continue
            else:
                output_str = top + "->" + expression.replace("$", "")
                exps = expression.split("$")
                if len(exps) == 1 and exps[0] == 'e':
                    stack.pop()
                    add_row(output_tb, step, get_stack_str(stack), get_input_str(input_list), output_str)
                    continue
                exps.reverse()
                stack.pop()
                stack.extend(exps)
                add_row(output_tb, step, get_stack_str(stack), get_input_str(input_list), output_str)
                continue

    if len(input_list) == 1:
        output_tb.add_row([step+1,"#","#","acc"])
    elif len(input_list) == 0:
        output_tb.add_row([step + 1, get_stack_str(stack), get_input_str(input_list), "refuse"])
    print(output_tb)