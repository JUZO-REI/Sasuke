#本文件负责任务的业务逻辑
class Task:
    """任务类，定义单个任务的基本属性"""
    def __init__(self, task_id, title, completed=False):#给Task类初始化，表示任务的ID，标题和是否完成
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        """将对象转换为字典，方便保存为 JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

class TodoManager:
    """任务管理器，处理核心业务逻辑"""
    def __init__(self, tasks_data):#与上同理，传参只需要传self后面，一般在主程序新建变量并调用，让变量自动获取值
        # 将从 JSON 读到的字典列表，转换为 Task 对象列表
        self.tasks = [Task(t['id'], t['title'], t['completed']) for t in tasks_data]#调用Task类，把从json文件中读取的字典数据转化为Task对象，并存储在tasks列表中，经todomanager再次封装给self
        #.tasks是一个列表，数据例子[对象1，对象2，……]，每个对象都是Task类的实例化对象

    def get_next_id(self):
        """生成下一个任务 ID"""
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add_task(self, title):
        """添加任务"""
        if not title.strip():#strip()方法用于去掉字符串的首尾空格，如果去掉空格后字符串为空，则抛出异常。括号内可以自己定义要去掉首尾的字符，默认是空格和换行符。
            raise ValueError("任务标题不能为空！")
        new_task = Task(self.get_next_id(), title)
        self.tasks.append(new_task)
        return new_task

    def list_tasks(self):
        """查看所有任务"""
        return self.tasks

    def complete_task(self, task_id):
        """完成任务"""
        for task in self.tasks:#这里的task是对象，对象内容是封装在Task里的
            if task.id == task_id:
                task.completed = True
                return True
        raise ValueError(f"未找到 ID 为 {task_id} 的任务")

    def delete_task(self, task_id):
        """删除任务"""
        for i, task in enumerate(self.tasks):#enmerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中。
            if task.id == task_id:
                del self.tasks[i]#删掉整个对象，del是python的删除语句，删除列表中指定索引的元素
                return True
        raise ValueError(f"未找到 ID 为 {task_id} 的任务")

    def to_dict_list(self):
        """将任务列表转换为字典列表，方便保存"""
        return [task.to_dict() for task in self.tasks] #这个函数封装在类里面了，所以直接用对象调用就好了