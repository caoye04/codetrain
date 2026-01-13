怎么 0 基础快速开启代码拟真训练 「 MAC 」

==================================================
首次使用
==================================================

1. 环境准备
   - 确保已安装 Git
   - 确保已安装 Python 3.x

2. 初始化项目
   
   克隆或初始化仓库（二选一）
   
   方式一：如果已有远程仓库
   git clone <仓库地址>
   cd <仓库目录>

   方式二：如果是新项目
   git init
   git remote add origin <仓库地址>

3. 生成练习文件
   
   创建你的练习目录并生成题目文件
   python quickStar.py your_project_name

4. 开始训练
   
   进入练习目录
   cd your_project_name

   逐个完成 Python 题目
   可以去 LeetCode 官网查看对应编号的题解，对比复杂度

5. 提交训练成果
   
   返回项目根目录
   cd ..

   创建并切换到你的个人分支
   git checkout -b your_name_practice

   添加所有修改
   git add .

   提交（建议格式：姓名 + 完成题数/题目）
   git commit -m "张三 完成 10 题"

   推送到远程分支
   git push -u origin your_name_practice

==================================================
后续训练
==================================================

1. 同步最新题库
   
   切换到主分支
   git checkout main

   拉取最新题目
   git pull origin main

   切换回你的练习分支
   git checkout your_name_practice

   合并最新题目到你的分支
   git merge main

2. 继续训练
   
   如果需要更新题目文件
   python quickStar.py your_project_name

   进入目录继续练习
   cd your_project_name

3. 提交新的训练成果
   
   cd ..
   git add .
   git commit -m "张三 新完成 5 题"
   git push origin your_name_practice

==================================================
添加新题目（维护者使用）
==================================================

1. 编辑题目
   
   创建 tmp.txt 文件，格式如下：
   lc_2335
   # 2335.装满杯子需要的最短总时长
   # 题目描述...

2. 更新题库
   
   python tmp2json.py

3. 提交到主分支
   
   git add Qlist.json
   git commit -m "添加题目 lc_2335"
   git push origin main

==================================================
常见问题
==================================================

Q: 如何查看我完成了哪些题目？
   cd your_project_name
   ls -l *.py | wc -l

Q: 不小心覆盖了代码怎么办？
   git checkout HEAD -- your_project_name/lc_xxxx.py

Q: 如何对比我的解法和官方解法？
   访问 LeetCode: https://leetcode.cn/problems/
   搜索题目编号查看题解和复杂度分析