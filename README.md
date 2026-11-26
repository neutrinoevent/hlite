# hlite

Alexander Nichols · Old Dominion University · [MIT License](LICENSE)

Put a colored background behind a selection in LaTeX. Choose the color
for each highlight and use one package option to prepare a clean copy.

## Install

Download the style file and put it next to your main `.tex` file. Replace
the project’s existing copy when you update. [Download `hlite.sty`](hlite.sty)

To share one copy across TeX Live projects, place it at
`tex/latex/hlite/hlite.sty` inside your personal TeX tree. Run
`kpsewhich -var-value=TEXMFHOME` to find that tree. If you have multiple
copies, run `kpsewhich hlite.sty` from the project directory to see which
file TeX finds.

Highlighting uses [highlightx](https://ctan.org/pkg/highlightx), which
`hlite` loads automatically. If it is missing, install it through your TeX
distribution. On TeX Live the package command is `tlmgr install highlightx`.
On a minimal TeX Live installation, an error that mentions `simplekv.sty`
means the rendering dependency is missing. Install it with
`tlmgr install simplekv` in the TeX Live installation your editor uses.

## Quick start

```latex
\documentclass{article}
\usepackage{hlite}

\begin{document}
\hlight{This uses the default pale yellow.}

\hlight[blue!12]{The closure error \(D=4.45\times10^{-8}\) was small
enough for the run. This selection can wrap across printed lines.}
\end{document}
```

Compile with pdfLaTeX. Compile twice when you add or move highlights so
the backgrounds line up with the text. TeXstudio's pdfLaTeX build uses the
same package. `latexmk -pdf` can handle the extra passes automatically.

Both `\hlight[blue!12]{text}` and `\hlite[blue!12]{text}` work. The optional
argument takes an `xcolor` color name or mix. For instance, `blue!12` mixes
12% blue with white. A named color works too.

```latex
% In the preamble, after \usepackage{hlite}
\definecolor{reportgold}{HTML}{F8F0E0}

% In the document body
\hlight[reportgold]{The finer integration kept the orbit bound.}
```

## Math, references, and citations

Both `$...$` and `\(...\)` work for inline math. References and citations
can go inside the selection, including optional citation notes.

```latex
\hlight[blue!12]{See Fig.~\ref{fig:orbit} and Eq.~\eqref{eq:period}.}
\hlight{The result agrees with the earlier study \cite[p.~15]{smith2020}.}
```

| Inside a highlight | Supported forms |
| --- | --- |
| Cross-references | `\ref`, `\pageref`, and `\eqref` |
| Named and linked references | `\autoref`, `\nameref`, `\cref`, and `\Cref` |
| Citations | `\cite`, natbib's `\citep` and `\citet`, and biblatex's `\parencite`, `\textcite`, and `\autocite` |
| Links and formatting | `\href{url}{text}` and common commands such as `\emph` and `\textbf` |

These commands use the reference and bibliography packages you load in
your document. For example, `\eqref` comes from `amsmath`. Citations still
need the usual BibTeX or Biber pass when your document uses one.

Wrap one paragraph at a time and keep display equations outside the selection.
A reference, citation, or link stays together inside a highlight. If a long
citation or link causes an overfull line, place it between two highlights so
LaTeX can break it normally.

If a custom inline command causes a build error, try boxing that command
and all its arguments.

```latex
\hlight{See \mbox{\myreference{orbit}} for the complete result.}
```

## Clean copy

Load the package with the `off` option for the submission copy.

```latex
\usepackage[off]{hlite}
```

The marked content is typeset directly, with the same text, math, and links.
This mode can run without `highlightx` installed.

## TeXstudio shortcut

In **Macros → Edit Macros**, add a **Normal** macro with the following content.

```latex
\hlight[blue!12]{%<text%>}
```

Assign a shortcut, select source text, and invoke the macro to wrap the
selection. [TeXstudio macro documentation](https://texstudio-org.github.io/advanced.html#personal-macros)

## Regression check

Run `python3 tests/check.py` with pdfLaTeX and [PyMuPDF](https://pymupdf.readthedocs.io/)
available. The check compiles [the fixture](tests/regression.tex) and verifies
wrapped highlights, intact links and citation text, and an `off` build that
renders like the unmarked fixture.
