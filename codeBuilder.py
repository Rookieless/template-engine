class CodeBuilder(object):
    """模板渲染编译类"""

    def __init__(self, indent=0):
        """
        初始化一个存放转换后Python代码，
        :param indent:代码缩进级别,默认为0
        """
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        """添加一行代码到code列表中"""
        self.code.extend([" " * self.indent_level, line, "\n"])

    def add_section(self):
        """将其他的CodeBuilder生成的code添加到self.code"""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    INDENT_STEP = 4

    def indent(self):
        """缩进"""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """取消缩进"""
        self.indent_level -= self.INDENT_STEP

    def get_globals(self):
        """执行code代码,返回全局的字典"""
        # 检查所有代码块是否执行完毕
        assert self.indent_level == 0
        # 把解析后的代码转换成str
        python_source = str(self)
        # 执行代码,定义全局的字典
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace
