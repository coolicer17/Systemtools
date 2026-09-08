import sys
import pytest
from greetlab.cli import main

# 测试1：name全是空白 → 退出码2
def test_blank_name_exits_with_code2(monkeypatch):
    # 模拟命令行输入：--name 是全空格
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   \t\n"])
    with pytest.raises(SystemExit) as exit_info:
        main()
    assert exit_info.value.code == 2

# 测试2：正常name → 保持原有功能不破坏
def test_valid_name_prints_correctly(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "赵均临"])
    main()
    assert "Hello 赵均临!" in capsys.readouterr().out
