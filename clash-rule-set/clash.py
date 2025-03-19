import os

def add_prefix_suffix_to_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 修改每一行
        modified_lines = ["  - '" + line.rstrip() + "'\n" for line in lines]

        with open(filepath, 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)

        print(f"文件 {filepath} 已成功修改。")

    except FileNotFoundError:
        print(f"错误：文件 {filepath} 未找到。")
    except Exception as e:
        print(f"发生错误：{e}")

file_path = input("请输入文件路径：")

add_prefix_suffix_to_file(file_path)