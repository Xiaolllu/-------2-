import json
from pathlib import Path

DATA_FILE = Path("todos.json")


def load_todos():
    if not DATA_FILE.exists():
        return []

    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("任务数据文件格式错误，已从空列表开始。")
        return []


def save_todos(todos):
    DATA_FILE.write_text(
        json.dumps(todos, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def show_todos(todos):
    if not todos:
        print("\n暂无任务。")
        return

    print("\nTodo 列表：")
    for index, todo in enumerate(todos, start=1):
        status = "✓" if todo["done"] else " "
        print(f"{index}. [{status}] {todo['title']}")


def read_number(prompt, maximum):
    try:
        number = int(input(prompt))
        if 1 <= number <= maximum:
            return number
    except ValueError:
        pass

    print("请输入有效的任务编号。")
    return None


def main():
    todos = load_todos()

    while True:
        print("\n1. 查看任务")
        print("2. 添加任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("0. 退出")

        choice = input("请选择操作：").strip()

        if choice == "1":
            show_todos(todos)

        elif choice == "2":
            title = input("请输入任务内容：").strip()
            if title:
                todos.append({"title": title, "done": False})
                save_todos(todos)
                print("已添加任务。")
            else:
                print("任务内容不能为空。")

        elif choice == "3":
            show_todos(todos)
            number = read_number("请输入要完成的任务编号：", len(todos))
            if number:
                todos[number - 1]["done"] = True
                save_todos(todos)
                print("任务已标记为完成。")

        elif choice == "4":
            show_todos(todos)
            number = read_number("请输入要删除的任务编号：", len(todos))
            if number:
                removed = todos.pop(number - 1)
                save_todos(todos)
                print(f"已删除：{removed['title']}")

        elif choice == "0":
            print("Todo 已保存，再见！")
            break

        else:
            print("无效选择，请重新输入。")


if __name__ == "__main__":
    main()