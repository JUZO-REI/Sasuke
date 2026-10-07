import json#本文件只负责数据的存储和读取，其他逻辑不在此处理
from pathlib import Path

# 获取 data.json 的绝对路径
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

def load_tasks():
    """从 JSON 文件读取任务"""
    try:
        # 尝试打开文件读取
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 如果文件不存在，返回空列表
        return []
    except json.JSONDecodeError:
        # 如果文件内容不是合法的 JSON（比如被手动改坏了）
        print("警告：数据文件损坏，将重置为空列表。")
        return []

def save_tasks(tasks):
    """将任务保存到 JSON 文件"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            # ensure_ascii=False 保证中文正常显示，indent=4 让格式美观
            json.dump(tasks, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"保存数据失败: {e}")