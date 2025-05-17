import os
import subprocess
import re

def is_suspicious_commit_msg(msg: str) -> bool:
    """不正っぽい文字列（実行パスやコマンド）を検知する"""
    lowered = msg.lower()
    suspicious_patterns = [
        r'^\s*&\s',             # PowerShell実行パターン: & "path/to/python"
        r'python\.exe',
        r'\.py$',               # スクリプト名で終わってる場合
        r'^c:\\',               # Windowsの絶対パスっぽいやつ
        r'^d:\\',
        r'\.exe',
        r'\/.*\.py',            # Unix系パス+スクリプト名
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, msg):
            return True
    return False

def main():
    script_dir = os.path.dirname(__file__)
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))

    tracked_files = [
        "script/log_writer.py",
        "script/generate_and_log.py",
        "script/push_script_changes.py",
        "script/.gitignore"
    ]

    print("📦 ステージング予定ファイル：")
    for file in tracked_files:
        print(f"  - {file}")

    print("\n📝 コミットメッセージを入力してください")
    commit_msg = input("> ").strip()

    if not commit_msg:
        print("❌ エラー: 空のメッセージではコミットできません。")
        return

    if is_suspicious_commit_msg(commit_msg):
        print("🚨 エラー: 実行コマンドやパスっぽい文字列が含まれています。")
        print("💡 手動入力で、コメントのみのメッセージを入力してください。")
        return

    # Git操作
    for f in tracked_files:
        subprocess.run(["git", "add", f], cwd=repo_root)

    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_root)
    subprocess.run(["git", "push"], cwd=repo_root)

    print("✅ コミット＆Push完了！")

if __name__ == "__main__":
    main()
