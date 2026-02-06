import subprocess
from pathlib import Path

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

    for file in sorted(topic.glob("*.zip")):
        date = last_modified(file)
        size = file_size(file.stat().st_size)

        rows.append(f"""
        <tr>
            <td><a href="{file}">{file.name}</a></td>
            <td>{size}</td>
            <td>{date}</td>
        </tr>
        """)

    if not rows:
        continue

    sections.append(f"""
    <h2>{topic.name}</h2>
    <table>
        <tr>
            <th>파일</th>
            <th>크기</th>
            <th>수정일</th>
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
    background: #f5f5f5;
}}
</style>
</head>
<body>

<h1>Download Center</h1>

{''.join(sections)}

</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")
