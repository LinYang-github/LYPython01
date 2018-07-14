import sys

# argv 命令行参数，包括脚本名称
# exit([arg]) 退出当前的程序，可选参数为给定的返回值或者错误信息
# modules 映射模块名称到载入模块的字典
# path 查找模块所在目录的目录名列表
# platform 类似sunos5或者win32的平台标识符
# stdin 标准输入流-一个类文件（file-like）对象
# stdout 标准输出流-一个类文件对象
# stderr 标准错误流-一个类文件对象

args = sys.argv[1:]
args.reverse()
print ' '.join(args)
