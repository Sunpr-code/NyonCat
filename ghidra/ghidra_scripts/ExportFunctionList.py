# ExportFunctionList.py
# Ghidra Jython script: 导出函数列表（名称、入口地址、大小）
# 使用方法：在 Ghidra Script Manager 中运行，或通过 analyzeHeadless 的 -postScript 调用

from ghidra.util import Msg
from ghidra.program.model.listing import Function
import os

output_name = "ghidra_functions.txt"
funcs = currentProgram.getFunctionManager().getFunctions(True)

# 输出到当前目录或脚本参数指定目录
out = open(os.path.join(getScriptArgs()[0] if getScriptArgs() else os.getcwd(), output_name), 'w')
count = 0
for f in funcs:
    try:
        name = f.getName()
        entry = f.getEntryPoint()
        size = f.getBody().getNumAddresses()
        out.write("{}\t{}\t{}\n".format(name, entry, size))
        count += 1
    except Exception as e:
        Msg.info(None, "Skipped function due to: {}".format(e))
out.close()
print("Exported {} functions to {}".format(count, output_name))
