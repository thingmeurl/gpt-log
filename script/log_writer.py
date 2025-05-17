import os
from datetime import datetime
import subprocess

def git_commit_and_push(file_path: str, message: str):
    # Gitルート（gptフォルダ）を基準にする
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    subprocess.run(["git", "add", file_path], cwd=repo_dir)
    subprocess.run(["git", "commit", "-m", message], cwd=repo_dir)
    subprocess.run(["git", "push"], cwd=repo_dir)

def save_markdown_log(summary_text: str):
    today = datetime.now().strftime("%Y-%m-%d")
    script_dir = os.path.dirname(__file__)
    log_dir = os.path.abspath(os.path.join(script_dir, "../log"))
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, f"{today}.md")

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(summary_text)

    git_commit_and_push(log_path, f"{today} ログ追加")

def main():
    script_dir = os.path.dirname(__file__)
    summary_path = os.path.join(script_dir, "summary.txt")
    if not os.path.exists(summary_path):
        print("⚠️ summary.txt が見つかりません")
        return

    with open(summary_path, "r", encoding="utf-8") as f:
        summary = f.read()

    save_markdown_log(summary)

if __name__ == "__main__":
    main()
