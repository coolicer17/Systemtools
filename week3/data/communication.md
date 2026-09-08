## 1. 重写Issue（可执行Bug报告）
# Bug：传入空白`--name`参数时输出无意义问候语且退出码为0
**环境**：greetlab-25020007178 v0.1.0，Python≥3.8（Windows兼容性待确认）
**复现命令**：`sdt-greet --name "   "`（纯空格/空输入）
**实际结果**：输出`Hello !`，进程退出码`0`
**预期结果**：拒绝无效空白输入，打印错误提示，退出码非0

## 2. 重写Commit Message（祈使语气规范）
fix(cli): reject blank/whitespace-only `--name` arguments
此前空白name输入会生成无意义问候语，导致自动化调用拿到错误结果。
新增strip()非空校验：空白输入直接返回SystemExit(2)，补充对应单元测试用例。

## 3. 重写PR评审意见（带优先级）
> 针对`src/greetlab/cli.py`第7行参数解析后逻辑
**[Blocking] 缺失输入合法性校验**
空白输入返回成功结果会导致下游逻辑出错，不符合CLI工具基本规范。
建议：加`if not a.name.strip(): raise SystemExit(2)`，补充空输入测试用例后再合并。