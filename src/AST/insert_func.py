from .data import *
from random import randint
from ..AST_Base import *
from ..global_var import *
from ..quit import *

def _wrong_param_number(name: str, expect_num: str, get_num: str, obj):
    add_error_message(f'Function {name} expect {expect_num} parameters, but found {get_num}', obj)

def _wrong_param_type(name: str, expect_types: list, get_types: list, obj):
    expect_type_list = [f'`{i}`' for i in expect_types]
    expect_type_str = ', '.join(expect_type_list)
    get_type_list = [f'`{i}`' for i in get_types]
    get_type_str = ', '.join(get_type_list)

    add_error_message(f'Function {name} expect parameter with type {expect_type_str}, but found {get_type_str}', obj)

class Int_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'INTEGER_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter', self)
            return
        else:
            result = result[0]
        try:
            result = int(result[0])
            return (result, 'INTEGER')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `INTEGER`', self)

class Str_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'STRING_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter', self)
            return
        else:
            result = result[0]
        try:
            result = str(result[0])
            return (result, 'STRING')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `STRING`', self)

class Char_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'CHAR_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter', self)
            return
        else:
            result = result[0]


        try:
            result = str(result[0])
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `CHAR`', self)
            return

        # 判断长度，如果不是1，都不可以
        if len(result) != 1:
            add_error_message(f'Cannot convert `{result}` into `CHAR`', self)
        else:
            return (result, 'CHAR')

class Real_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'REAL_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter', self)
            return
        else:
            result = result[0]
        try:
            result = float(result[0])
            return (result, 'REAL')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `REAL`', self)

class Bool_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'BOOLEAN_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter', self)
            return
        else:
            result = result[0]
        try:
            result = bool(result[0])
            return (result, 'BOOLEAN')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `BOOLEAN`', self)


class Left(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'LEFT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 2:
            add_error_message(f'Function `{self.type}` expect 2 parameters, but found `{len(parameters)}`', self)
            return

        s = parameters[0]
        x = parameters[1]
        if s[1] == 'STRING' and x[1] == 'INTEGER':
            return (s[0][0:x[0]], 'STRING')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` and `INTEGER`, but found `{s[1]}` and `{x[1]}`', self)

class Right(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'RIGHT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 2:
            add_error_message(f'Function `{self.type}` expect 2 parameters, but found `{len(parameters)}`', self)
            return

        s = parameters[0]
        x = parameters[1]
        if s[1] == 'STRING' and x[1] == 'INTEGER':
            return (s[0][len(s[0])-x[0]:], 'STRING')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` and `INTEGER`, but found `{s[1]}` and `{x[1]}`', self)

class Length(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'LENGTH'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`', self)
            return

        s = parameters[0]
        if s[1] == 'STRING':
            return (len(s[0]), 'INTEGER')
        elif s[1] == 'ARRAY':
            return (len(s), 'INTEGER')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` or `ARRAY`, but found `{s[1]}`', self)

class Mid(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'MID'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 3:
            add_error_message(f'Function `{self.type}` expect 3 parameters, but found `{len(parameters)}`', self)
            return

        s = parameters[0]
        x = parameters[1]
        y = parameters[2]
        if s[1] == 'STRING' and x[1] == 'INTEGER' and y[1] == 'INTEGER':
            return (s[0][x[0]-1:x[0]+y[0]-1], 'STRING')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` and `INTEGER` and `INTEGER`, but found `{self.s[1]}` and `{self.x[1]}` and `{self.y[1]}`', self)

class Lcase(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'LCASE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) != 1:
                add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`', self)
                return

            c = parameters[0]
            if c[1] == 'CHAR':
                return (c[0].lower(), 'CHAR')
            elif c[1] == 'STRING':
                return (c[0].lower(), 'STRING')
            else:
                add_error_message(f'Function `{self.type}` expect `CHAR`, but found `{c[1]}`', self)
        else:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found 0', self)

class Ucase(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'UCASE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) != 1:
                add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`', self)
                return

            c = parameters[0]
            if c[1] == 'CHAR':
                return (c[0].upper(), 'CHAR')
            elif c[1] == 'STRING':
                return (c[0].upper(), 'STRING')
            else:
                add_error_message(f'Function `{self.type}` expect `CHAR`, but found `{c[1]}`', self)
        else:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found 0', self)


class Rand(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'RAND'
        self.parameters = parameters
        self.rate = 100

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`', self)
            return

        n = parameters[0]
        if n[1] == 'INTEGER':
            return ( randint(0, n[0]*self.rate)/self.rate , "REAL")
        else:
            add_error_message(f'Function `{self.type}` expect `CHAR`, but found `{n[1]}`', self)


class Eof(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'EOF'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`', self)
            return

        fp = parameters[0]
        if fp[1] == 'STRING':
            f = stack.get_file(fp[0])
            eof = stack.get_eof(fp[0])
            if f.tell() >= eof:
                return (True, 'BOOLEAN')
            else:
                return (False, 'BOOLEAN')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` for a file path, but found `{fp[1]}`', self)

class Pow(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'POW'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        try:
            return (parameters[0][0] ** parameters[1][0], 'REAL')
        except:
            add_error_message(f'Cannot power `{parameters[0][1]}` with `{parameters[1][1]}`', self)

class Exit(AST_Node):
    def __init__(self, parameters=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'EXIT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters != None:
            parameters = self.parameters.exe()
            try:
                exit_code = int(parameters[0][0])
            except:
                exit_code = 0
        else:
            exit_code = 0

        quit(exit_code)

class Round(AST_Node):
    def __init__(self, parameters=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ROUND'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 1:
                return (round(parameters[0][0]), 'INTEGER')
            elif len(self.parameters) == 2:
                return (round(parameters[0][0], parameters[1][0]), 'REAL')
            else:
                add_error_message(f'Round only have 1 or 2 parameters, but found {len(self.parameters)}', self)
        else:
            add_error_message(f'Round only have 1 or 2 parameters, but found 0', self)

class Python(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'PYTHON'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            code = parameters[0][0]
            global_space = {}

            # 尝试导入参数
            for i in range(1, len(parameters)):
                try:
                    global_space[self.parameters.parameters[i].id] = parameters[i][0]
                except:
                    add_error_message(f'Pythons interface only accept variables with basic data types', self)

            return_name = '_result'
            global_space[return_name] = None

            try:
                exec(code, global_space)
            except Exception as e:
                add_python_error_message(e, self)
                # global_space[return_name] = None

            return (global_space[return_name], None)  # None 表示未知类型
        else:
            add_error_message(f'Python interface only have 1 parameters, but found 0', self)

class Mod(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'MOD'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 2:
                return (parameters[0][0] % parameters[1][0], 'REAL')
            else:
                add_error_message(f'Mod only have 2 parameters, but found {len(self.parameters)}')
        else:
            add_error_message(f'Mod only have 2 parameters, but found 0', self)

class Div(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DIV'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 2:
                return (parameters[0][0] // parameters[1][0], 'REAL')
            else:
                add_error_message(f'Mod only have 2 parameters, but found {len(self.parameters)}')
        else:
            add_error_message(f'Mod only have 2 parameters, but found 0', self)

class VarType(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'VAR_TYPE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                return (parameters[0][1], 'STRING')
            else:
                add_error_message(f'Type only have 1 parameters, but found {len(parameters)}', self)
        else:
            add_error_message(f'Type only have 1 parameters, but found 0', self)

class ToUpper(Ucase):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(parameters, *args, **kwargs)
        self.type = 'TO_UPPER'

class ToLower(Lcase):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(parameters, *args, **kwargs)
        self.type = 'TO_LOWER'

class Day(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DAY'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    return (int(p[0].split('/')[0]), 'INTEGER')
                else:
                    add_error_message(f'DAY expect a parameter with type `DATE`, but found `{p[1]}`', self)
            else:
                add_error_message(f'DAY only have 1 parameters, but found {len(parameters)}', self)
        else:
            add_error_message(f'DAY only have 1 parameters, but found 0', self)

class Month(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'MONTH'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    return (int(p[0].split('/')[1]), 'INTEGER')
                else:
                    add_error_message(f'MONTH expect a parameter with type `DATE`, but found `{p[1]}`', self)
            else:
                add_error_message(f'MONTH only have 1 parameters, but found {len(parameters)}', self)
        else:
            add_error_message(f'MONTH only have 1 parameters, but found 0', self)

class Year(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'YEAR'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    return (int(p[0].split('/')[2]), 'INTEGER')
                else:
                    add_error_message(f'YEAR expect a parameter with type `DATE`, but found `{p[1]}`', self)
            else:
                add_error_message(f'YEAR only have 1 parameters, but found {len(parameters)}', self)
        else:
            add_error_message(f'YEAR only have 1 parameters, but found 0', self)

class DayIndex(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DATE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    from datetime import datetime
                    return (datetime.strptime(p[0], '%d/%m/%Y').weekday() + 1) % 7 + 1
                else:
                    add_error_message(f'DAY expect a parameter with type `DATE`, but found `{p[1]}`', self)
            else:
                add_error_message(f'DAY only have 1 parameters, but found {len(parameters)}', self)
        else:
            add_error_message(f'DAY only have 1 parameters, but found 0', self)

class Today(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'TODAY'

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type

    def exe(self):
        from datetime import datetime
        return (datetime.now().strftime('%d/%m/%Y'), 'DATE')

insert_functions = {
    "INT": Int_convert,
    "INTEGER": Int_convert,
    "REAL": Real_convert,
    "STRING": Str_convert,
    "BOOLEAN": Bool_convert,
    "CHAR": Char_convert,
    "LEFT": Left,
    "RIGHT": Right,
    "LENGTH": Length,
    "MID": Mid,
    "LCASE": Lcase,
    "UCASE": Ucase,
    "RAND": Rand,
    "RANDOM": Rand,
    "EOF": Eof,
    "POW": Pow,
    "EXIT": Exit,
    "ROUND": Round,
    "PYTHON": Python,
    "MOD": Mod,
    "DIV": Div,
    "VARTYPE": VarType,
    "TO_UPPER": ToUpper,
    "TO_LOWER": ToLower,
    "DAY": Day,
    "MONTH": Month,
    "YEAR": Year,
    "DAYINDEX": DayIndex,
    "TODAY": Today
}
