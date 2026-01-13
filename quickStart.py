import json
import os
import sys

def load_qlist(filename='Qlist.json'):
    """加载Qlist.json文件"""
    if not os.path.exists(filename):
        print(f"错误：{filename} 文件不存在")
        return []
    
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_python_file(directory, problem_id, description):
    """创建包含题目描述注释的Python文件"""
    filename = os.path.join(directory, f"{problem_id}.py")
    
    # 如果文件已存在，不覆盖
    if os.path.exists(filename):
        return False
    
    # 将描述按行分割并添加注释符号
    lines = description.strip().split('\n')
    commented_lines = [f"# {line.lstrip('# ')}" for line in lines]
    content = '\n'.join(commented_lines) + '\n\n'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def get_existing_files(directory):
    """获取目录中已存在的Python文件的编号"""
    if not os.path.exists(directory):
        return set()
    
    existing = set()
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            # 移除.py后缀得到编号
            problem_id = filename[:-3]
            existing.add(problem_id)
    
    return existing

def main():
    if len(sys.argv) < 2:
        print("用法：python quickStar.py <目录名>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    # 如果目录不存在，创建目录
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"已创建目录：{directory}")
    else:
        print(f"目录已存在：{directory}")
    
    # 加载题目列表
    qlist = load_qlist()
    
    if not qlist:
        print("Qlist.json 为空或不存在")
        return
    
    # 获取已存在的文件
    existing_files = get_existing_files(directory)
    
    # 遍历所有题目
    created_count = 0
    for item in qlist:
        for problem_id, description in item.items():
            if problem_id not in existing_files:
                if create_python_file(directory, problem_id, description):
                    print(f"已创建文件：{problem_id}.py")
                    created_count += 1
            else:
                print(f"跳过已存在的文件：{problem_id}.py")
    
    print(f"\n操作完成！共创建 {created_count} 个新文件。")

if __name__ == '__main__':
    main()