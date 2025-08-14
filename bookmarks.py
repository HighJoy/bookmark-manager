import json
import os

BOOKMARKS_FILE = "bookmarks.json"

def load_bookmarks():
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, 'r') as f:
            return json.load(f)
    return {"categories": []}

def save_bookmarks(data):
    with open(BOOKMARKS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_bookmark():
    name = input("网站名称: ")
    url = input("网址URL: ")
    category = input("分类: ")

    bookmarks = load_bookmarks()
    
    # 查找或创建分类
    found = False
    for cat in bookmarks["categories"]:
        if cat["name"] == category:
            cat["links"].append({"name": name, "url": url})
            found = True
            break
    
    if not found:
        bookmarks["categories"].append({
            "name": category,
            "links": [{"name": name, "url": url}]
        })
    
    save_bookmarks(bookmarks)
    print(f"✅ 已添加: {name}")

def generate_html():
    bookmarks = load_bookmarks()
    with open('index.html', 'w') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>我的书签导航</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .category { margin-bottom: 30px; }
        h2 { border-bottom: 2px solid #3498db; padding-bottom: 5px; }
        ul { list-style: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #2c3e50; }
        a:hover { color: #3498db; }
    </style>
</head>
<body>
    <h1>我的常用网站</h1>
""")
        for category in bookmarks["categories"]:
            f.write(f'    <div class="category">\n')
            f.write(f'        <h2>{category["name"]}</h2>\n        <ul>\n')
            for link in category["links"]:
                f.write(f'            <li><a href="{link["url"]}" target="_blank">{link["name"]}</a></li>\n')
            f.write('        </ul>\n    </div>\n')
        f.write("</body>\n</html>")
    print("🚀 已生成 index.html")

if __name__ == "__main__":
    while True:
        print("\n==== 书签管理器 ====")
        print("1. 添加新书签")
        print("2. 生成网页")
        print("3. 退出")
        
        choice = input("请选择: ")
        
        if choice == "1":
            add_bookmark()
        elif choice == "2":
            generate_html()
        elif choice == "3":
            break
