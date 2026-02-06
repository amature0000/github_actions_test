import subprocess
from pathlib import Path
from urllib.parse import quote

BASE = Path("resource")


def last_modified(path):
    cmd = ["git", "log", "-1", "--format=%ad", "--date=short", "--", str(path)]
    try:
        return subprocess.check_output(cmd).decode().strip()
    except:
        return "-"

def file_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


sections = []

for topic in sorted(BASE.iterdir()):
    if not topic.is_dir():
        continue

    rows = []

    for data_dir in sorted(topic.iterdir()):
        if not data_dir.is_dir():
            continue

        name = data_dir.name

        # #d 태그 확인
        enabled = True
        if name.endswith("#d"):
            enabled = False
            name = name[:-2]

        # 내부 zip 찾기
        zips = list(data_dir.glob("*.zip"))
        if not zips:
            continue

        file = zips[0]

        date = last_modified(file)
        size = file_size(file.stat().st_size)

        display = name
        if not enabled:
            display = f"<del>{name}</del>"

        rows.append(f"""
        <tr>
            <td><a href="{quote(str(file))}">{display}</a></td>
            <td>{date}</td>
            <td>{size}</td>
        </tr>
        """)

    if not rows:
        continue

    sections.append(f"""
    <h2>{topic.name}</h2>
    <table>
        <tr>
            <th>설명</th>
            <th>수정일</th>
            <th>크기</th>
        </tr>
        {''.join(rows)}
    </table>
    """)


html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Downloads</title>
<style>
body {{
    font-family: sans-serif;
    max-width: 900px;
    margin: auto;
}}

table {{
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 30px;
}}

td, th {{
    padding: 6px 10px;
    border-bottom: 1px solid #ddd;
    text-align: left;
}}

th {{
    background: #f3f3f3;
}}

del {{
    color: #888;
}}
</style>
</head>
<body>
<div style="margin-bottom:20px;">
<input id="searchBox" placeholder="검색..." />
</div>
<h1>Download Center</h1>

{''.join(sections)}
<script src="script.js"></script>
</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")
