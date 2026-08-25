# ExtractStrings.py
# Ghidra Jython script: 导出可定义字符串到文本文件
# 使用方法：在 Ghidra Script Manager 中运行，或通过 analyzeHeadless 的 -postScript 调用

from ghidra.program.model.listing import CodeUnit
from ghidra.util import Msg

import os

output_name = "ghidra_strings.txt"
current_program = getCurrentProgram()
listing = current_program.getListing()
strings = []

# 获取已定义字符串（包括 Unicode）
for data in listing.getDefinedData(True):
    if data is None:
        continue
    data_type = data.getDataType()
    try:
        # 仅抓取字符串类型的 data
        if data_type.getName().lower().find("string") != -1:
            addr = data.getMinAddress()
            s = data.getDefaultValueRepresentation()
            strings.append((str(addr), s))
    except Exception as e:
        Msg.info(None, "Skipped data due to: {}".format(e))

# 写出到脚本运行目录
out = open(os.path.join(getScriptArgs()[0] if getScriptArgs() else os.getcwd(), output_name), 'w')
for addr, s in strings:
    out.write("{}\t{}\n".format(addr, s))
out.close()
print("Exported {} strings to {}".format(len(strings), output_name))
