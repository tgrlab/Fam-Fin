from pathlib import Path
import subprocess, shutil
root = Path(__file__).resolve().parents[1]
out = root / "dist"
if out.exists(): shutil.rmtree(out)
(out / "test").mkdir(parents=True)
shutil.copyfile(root / "production/index.html", out / "index.html")
try:
    source = subprocess.check_output(["git", "show", "origin/develop:app/index.html"], cwd=root, stderr=subprocess.DEVNULL, text=True)
except subprocess.CalledProcessError:
    source = (root / "app/index.html").read_text(encoding="utf-8")
source = source.replace("family-v4-before-restore", "family-finance-preview-before-restore").replace("family-v4", "family-finance-preview")
source = source.replace("<main>", '<main><div role="status" style="background:#fff0d7;color:#704600;padding:12px;border-radius:12px;margin-bottom:14px;font-weight:600">테스트 환경 · 실제 가계 데이터, 개인정보, 실제 카드명세서를 입력하지 마세요.</div>', 1)
(out / "test/index.html").write_text(source, encoding="utf-8")
(out / ".nojekyll").touch()
print("Pages build complete: / (production hold), /test/ (preview)")
