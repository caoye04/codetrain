import json
import os

def read_tmp_file(filename='tmp.txt'):
    """读取tmp.txt文件内容"""
    if not os.path.exists(filename):
        print(f"错误：{filename} 文件不存在")
        return None, None
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if len(lines) < 2:
        print("错误：tmp.txt 至少需要两行（编号 + 题目描述）")
        return None, None
    
    # 第一行是编号
    problem_id = lines[0].strip()
    # 剩余行是题目描述
    description = ''.join(lines[1:]).strip()
    
    return problem_id, description

def load_qlist(filename='Qlist.json'):
    """加载Qlist.json文件"""
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_qlist(qlist, filename='Qlist.json'):
    """保存到Qlist.json文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(qlist, f, ensure_ascii=False, indent=4)

def update_qlist(problem_id, description):
    """更新或添加题目到Qlist.json"""
    qlist = load_qlist()
    
    # 查找是否已存在该编号
    found = False
    for item in qlist:
        if problem_id in item:
            # 更新现有条目
            item[problem_id] = description
            found = True
            print(f"已更新题目：{problem_id}")
            break
    
    if not found:
        # 添加新条目
        qlist.append({problem_id: description})
        print(f"已添加新题目：{problem_id}")
    
    save_qlist(qlist)

def main():
    problem_id, description = read_tmp_file()
    
    if problem_id and description:
        update_qlist(problem_id, description)
        print("操作完成！")
    else:
        print("操作失败，请检查tmp.txt文件")

if __name__ == '__main__':
    main()