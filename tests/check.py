"""Exercise the highlighting commands through pdfLaTeX and inspect the PDFs."""

import os
from pathlib import Path
import re
import subprocess
import tempfile

import fitz


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = Path(__file__).with_name("regression.tex")
PACKAGE_LINE = r"\usepackage{hlite}"


def compile_fixture(directory, source):
    directory.mkdir()
    (directory / "regression.tex").write_text(source)
    texinputs = os.environ.get("TEXINPUTS", "")
    env = dict(os.environ, TEXINPUTS=f"{ROOT}{os.pathsep}{texinputs}")
    for _ in range(3):
        run = subprocess.run(
            ["pdflatex", "-halt-on-error", "-interaction=nonstopmode", "regression.tex"],
            cwd=directory,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=60,
        )
        if run.returncode:
            raise RuntimeError(run.stdout)

    log = (directory / "regression.log").read_text()
    if re.search(r"Overfull \\hbox|undefined citations|undefined references", log):
        raise AssertionError("\n".join(re.findall(r"(?im)^.*(?:Overfull|undefined).*", log)))
    return directory / "regression.pdf"


def document_text(document):
    text = "\n".join(page.get_text() for page in document)
    return "".join(re.sub(r"(?<=\w)-\n(?=\w)", "", text).split())


def links(document):
    return sorted(
        (link["kind"], link.get("page", -1), link.get("nameddest", ""), link.get("uri", ""))
        for page in document for link in page.get_links()
    )


def main():
    source = FIXTURE.read_text()
    off_source = source.replace(PACKAGE_LINE, r"\usepackage[off]{hlite}")
    plain_source = source.replace(
        PACKAGE_LINE, r"\NewDocumentCommand{\hlight}{O{} m}{#2}\let\hlite\hlight"
    )
    with tempfile.TemporaryDirectory(prefix="hlite-regression-") as temp:
        work = Path(temp)
        on = compile_fixture(work / "on", source)
        off = compile_fixture(work / "off", off_source)
        plain = compile_fixture(work / "plain", plain_source)
        with fitz.open(on) as highlighted, fitz.open(off) as clean, fitz.open(plain) as unmarked:
            assert document_text(highlighted) == document_text(clean)
            assert links(highlighted) == links(clean)
            assert any(uri == "https://example.org/orbit" for _, _, _, uri in links(highlighted))

            blue_lines = {
                round(drawing["rect"].y0, 2)
                for page in highlighted for drawing in page.get_drawings()
                if drawing["fill"] and tuple(round(c, 2) for c in drawing["fill"]) == (0.88, 0.88, 1.0)
            }
            assert len(blue_lines) >= 2, "The blue highlight should wrap across printed lines"
            assert len(clean) == len(unmarked)
            for page, baseline in zip(clean, unmarked):
                assert page.get_pixmap().samples == baseline.get_pixmap().samples
            assert "highlightx.sty" not in (work / "off" / "regression.log").read_text()

    print("Wrapped math, references, citations, hyperlinks, and off mode passed.")


if __name__ == "__main__":
    main()
