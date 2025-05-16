from datetime import datetime
import os

# 保存先ディレクトリの指定（環境に合わせて絶対パス）
save_dir = r"D:\Users\admin\Documents\gpt\log"

# フォルダがなければ作成
os.makedirs(save_dir, exist_ok=True)

# ファイル名（日付ベース）
today = datetime.today().strftime("%Y-%m-%d")
filename = f"{today}.md"

# ファイルパス（絶対パスに変更）
file_path = os.path.join(save_dir, filename)

# 仮の中身
content = f"# 🗓️ {today} ログ\n\n## 🌧️ 天気・気分\n- 雨模様のスタート\n\n## 💬 雑感\n- 最小単位から始める"

# ファイル保存
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"{file_path} を作成しました。")
