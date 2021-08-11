from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

for path in sorted(Path("src").glob("**/*.py")):
    doc_path = path.relative_to("src", "syndio_backend_test").with_suffix(".md")

    nav[doc_path.with_suffix("").parts] = doc_path

    with mkdocs_gen_files.open(Path("reference", doc_path), "w") as f:
        print(f"::: {'.'.join(path.relative_to('src').with_suffix('').parts)}", file=f)

with mkdocs_gen_files.open("reference/index.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
