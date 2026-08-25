# Headless Ghidra 分析 模板

以下为在本地（隔离环境）使用 Ghidra headless analyzer 的示例模板。请将 `<PROJECT_DIR>` 与 `<INPUT_FILE>` 替换为你本地受控环境中的路径。示例仅用于展示如何批量运行分析并导出结果。

示例（Linux / macOS / WSL）

```bash
# 假设 ghidra 安装目录为 /opt/ghidra
GHIDRA_HOME=/opt/ghidra
PROJECT_DIR=/path/to/your/ghidra_projects
INPUT_FILE=/path/to/MEMZ.exe
PROJECT_NAME=MEMZ-analysis

# 导入并分析（示例）
${GHIDRA_HOME}/support/analyzeHeadless ${PROJECT_DIR} ${PROJECT_NAME} -import ${INPUT_FILE} -postScript ExtractStrings.py -scriptPath ghidra/ghidra_scripts -deleteProject

# 说明：
# - 这个命令在本地运行，会把输入文件导入到本地 Ghidra 项目并运行指定脚本。
# - 请勿将 INPUT_FILE 指向任何联网或共享目录，也不要把分析产生的样本复制到公网位置。
```

注意事项
- 上述命令为模板示例，不会自动下载或上传样本；请确保在受控环境中手动提供输入文件。 
- `-postScript` 与 `-scriptPath` 用于调用本仓库内的 Ghidra 脚本（需先把脚本放到 Ghidra 的 scriptPath 或在命令中指定）。
- Ghidra 的具体路径和参数请参照你本地 Ghidra 版本的文档。