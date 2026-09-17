"""Convierte un reporte .md (con LaTeX) al .html que pide la entrega.

Uso:
    python toHTML.py P1E4_Gael_Jose_Remi.md
    python toHTML.py archivo1.md archivo2.md ...
"""

import re
import sys
from pathlib import Path

import markdown

MATH_PLACEHOLDER = "\x00MATH{}\x00"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']] }}
  }};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  body {{
    font-family: Georgia, "Times New Roman", serif;
    max-width: 850px;
    margin: 2rem auto;
    padding: 0 1.5rem;
    line-height: 1.6;
    color: #1a1a1a;
  }}
  h1, h2, h3 {{ font-family: Arial, Helvetica, sans-serif; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 2rem 0; }}
  code {{ background: #f2f2f2; padding: 0.1rem 0.3rem; }}
</style>
</head>
<body>
{content}
</body>
</html>
"""


def protect_math(text):
    """Saca los bloques $$...$$ y $...$ antes de correr el parser de markdown,
    para que no interprete _ o * dentro de LaTeX como negritas/cursivas."""
    stored = []

    def stash(match):
        stored.append(match.group(0))
        return MATH_PLACEHOLDER.format(len(stored) - 1)

    text = re.sub(r"\$\$.*?\$\$", stash, text, flags=re.DOTALL)
    text = re.sub(r"\$.*?\$", stash, text, flags=re.DOTALL)
    return text, stored


def restore_math(html, stored):
    for i, original in enumerate(stored):
        html = html.replace(MATH_PLACEHOLDER.format(i), original)
    return html


def convert_file(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    protected_text, stored = protect_math(text)

    body_html = markdown.markdown(
        protected_text, extensions=["extra", "sane_lists"]
    )
    body_html = restore_math(body_html, stored)

    title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else md_path.stem

    html = HTML_TEMPLATE.format(title=title, content=body_html)

    out_path = md_path.with_suffix(".html")
    out_path.write_text(html, encoding="utf-8")
    print(f"OK: {md_path.name} -> {out_path.name}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python toHTML.py archivo1.md [archivo2.md ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        md_path = Path(arg)
        if not md_path.exists():
            print(f"ERROR: no existe {arg}")
            continue
        convert_file(md_path)


if __name__ == "__main__":
    main()
