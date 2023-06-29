# CAIE Code
CAIE Pseudocode Interpreter

## 安装与使用
1. 安装 `Python3` 环境
2. 克隆此项目 `git clone https://github.com/iewnfod/CAIE_Code.git`
3. 进入项目 `cd CAIE_Code`
4. 安装依赖 `pip install -r requirements.txt`
4. 若是`MacOS`或`Linux`，使用指令`./cpc`，或直接双击目录内`cpc`文件即可运行
5. 若是`Windows`，请使用`python main.py`运行

## 标准
### 基本标准
* 推荐使用驼峰命名发命名
* 源文件后缀名推荐使用 **.cpc**（CAIE Pseudo Code 的首字母简写）
* 源文件使用 **utf-8** 编码
* 所有保留字均为大写，并且程序有大小写区分
* 使用 `//` 进行注释

### 一些特性
~~（说实话就是我不想改了）~~
* 四则运算只会在可运算的相同类型间运算，乘法除法的返回结果必定是`REAL`
* 所有变量在声明后默认值均为`None`，请即刻对其赋值，以避免不必要的错误
* 单独书写某个变量会对其进行输出，打印其值以及类型
* 使用保留字以实现子空间 ~~（虽然官方文档要求有缩进，但是在此不做强制要求）~~
* 由于没有进行缩进的识别，`CASE`中的每一项末尾都需要添加`;`表达这一项结束了

### 基础数据类型
* **INTEGER** 整型
* **REAL** 浮点数
* **CHAR** 单个字符
* **STRING** 字符串
* **BOOLEAN** 布尔值
* **DATE** 任何合法的日期 (此类型暂时不会实现)
