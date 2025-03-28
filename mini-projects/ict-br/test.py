from pathlib import Path

dir_script = Path(__file__).resolve().parent
dir_logs = dir_script / "logs"

with open(dir_logs / "test.log", "w", encoding="utf-8") as f:
    f.write("✅ Success!\n")
    f.write("📦 Loaded: 1000 rows\n")
    f.write("✂️ Truncated: 5 rows\n")