![hlite set in TeX braces over blue and yellow highlights](assets/hlite-banner.jpg)

# hlite

Alexander Nichols · Old Dominion University · [MIT License](LICENSE)

Line-wrapping highlights for LaTeX drafts and reports.

## Highlight findings in context

Mark a result together with the inline equation, figure reference, or
citation that supports it. The background follows the text as it wraps.
Use `\hlight[color]{text}` to give results one color and flag passages
for a coauthor in another.

For submission, one preamble edit removes the backgrounds while keeping
the text in the PDF and the highlight commands in your source.
[Build a PDF without highlights](#build-a-pdf-without-highlights)

## Quick start

1. Open the style file on GitHub and choose **Download raw file**.
   [Open `hlite.sty`](hlite.sty)
2. Save it next to your main `.tex` file. On Overleaf, upload it to the
   project’s top-level folder alongside the main file. [Overleaf package files](https://docs.overleaf.com/managing-projects-and-files/adding-latex-dependencies)
3. In an existing document, add `\usepackage{hlite}` before
   `\begin{document}` and wrap a passage in `\hlight{...}` in the body.

Compile twice to position the backgrounds. To try the example on its
own, save it as `demo.tex` and use pdfLaTeX. A local
`latexmk -pdf demo.tex` build handles the extra pass. When highlights
are enabled, `hlite` loads `highlightx` automatically.
[Help with missing packages](#troubleshooting)

```latex
\documentclass{article}
\usepackage{hlite}

\begin{document}
\hlight{The orbit remained bound for the full run.}

\hlight[blue!12]{At \(t=2\pi\), the orbit returned to within
\(4.45\times10^{-8}\) of its starting point. The closure error stayed
below our tolerance without changing the step size.}
\end{document}
```

`\hlight` and `\hlite` are interchangeable. Omit the color argument for
pale yellow (`yellow!18`). A highlight can wrap across lines within a
single paragraph, page, and column.

To use one copy across your local TeX Live projects, put `hlite.sty` in
`tex/latex/hlite/hlite.sty` under the tree reported by
`kpsewhich -var-value=TEXMFHOME`.

## Build a PDF without highlights

Replace `\usepackage{hlite}` with `\usepackage[off]{hlite}` and recompile.
The PDF still prints everything inside each highlight, including any
review-only prose. Remove that prose before sharing and check line and
page breaks in the rebuilt PDF.

If you share the `.tex` source, include the project’s copy of `hlite.sty`.
The `off` option skips `highlightx`. Switch back to `\usepackage{hlite}`
to restore the backgrounds.

## Highlight math, references, and citations

```latex
\hlight[blue!12]{For \(\ell=1\), Fig.~\ref{fig:orbit}
agrees with the earlier result \cite{smith2020}.}
```

Use your own figure and bibliography keys. Citation notes such as
`\cite[p.~15]{smith2020}` also work. For a complete document with labels
and bibliography entries, see [the compilable example](tests/regression.tex).

**Where to split a highlight.** Use shorter selections on either side of
a page or column break. Leave display equations between highlights, and
leave headings plain when they are used as PDF bookmarks. Each inline
formula, reference, citation, or link stays together inside a highlight.
If a long citation or link runs past the margin, put it between highlights
so LaTeX can break it normally.

| Inside a highlight | Supported forms |
| --- | --- |
| Inline math | `$...$` and `\(...\)` |
| Cross-references | `\ref` and `\pageref`, amsmath’s `\eqref`, hyperref’s `\autoref` and `\nameref`, and cleveref’s `\cref` and `\Cref` |
| Citations | `\cite`, natbib’s `\citep` and `\citet`, and biblatex’s `\parencite`, `\textcite`, and `\autocite` |
| Links and emphasis | hyperref’s `\href{url}{text}`, `\emph`, and `\textbf` |

Load the packages that provide the commands you use, and run the usual
BibTeX or Biber pass if your document calls for one. Existing PDF links
remain clickable.

**Tested setups.** On TeX Live 2026, the engine checks covered pdfLaTeX,
LuaLaTeX, and XeLaTeX. The two-column APS REVTeX 4.2 check used pdfLaTeX.
The citation checks covered natbib and, separately, biblatex with Biber.
For shared builds, record the TeX Live version used for the manuscript.

## Choose a color

The brackets accept an `xcolor` name or mix. The examples below use
built-in names and work with the quick start above.

| For a background like this | Put this in brackets |
| --- | --- |
| Pale yellow, the default | `[yellow!18]` |
| Soft blue | `[blue!12]` |
| Soft teal | `[teal!15]` |
| Soft violet | `[violet!12]` |
| Warm peach | `[orange!18]` |

`blue!12` means 12% blue and 88% white. Lower the number for a paler
background or raise it for a stronger one. A plain name such as `[blue]`
uses the full color. The third term lets you replace white with another
color, as in `blue!12!yellow`. [xcolor manual](https://tug.ctan.org/macros/latex2e/contrib/xcolor/xcolor.pdf)

### Define colors you’ll reuse

Define a color once in the preamble, then use its name in any highlight.
Use `\definecolor` for an exact shade and `\colorlet` to name a mix.
Load `xcolor` explicitly so the definitions also work with `[off]`.

```latex
% In the preamble, before \begin{document}
\usepackage{xcolor}
\usepackage{hlite}
\definecolor{resultblue}{HTML}{E4EFF8} % Six hex digits, without #
\colorlet{reviewpeach}{orange!18}

% In the document body
\hlight[resultblue]{The two estimates agreed within uncertainty.}
\hlite[reviewpeach]{All periods are reported in hours.}
```

To use extra named colors such as `ForestGreen`, load
`\usepackage[dvipsnames]{xcolor}` before `hlite` or any other package that
loads `xcolor`. Use the spelling and capitalization from the color list.
[xcolor named colors](https://tug.ctan.org/macros/latex2e/contrib/xcolor/xcolor.pdf#page=38)

## Work faster in TeXstudio

In **Macros → Edit Macros**, add a **Normal** macro with this content.

```latex
\hlight[blue!12]{%<text%>}
```

Assign a shortcut, select source text, and invoke the macro to wrap the
selection. [TeXstudio macro documentation](https://texstudio-org.github.io/advanced.html#personal-macros)

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Text appears without a background | Check for `[off]` and run pdfLaTeX again after editing or moving a highlight. |
| TeX finds an old copy | Run `kpsewhich hlite.sty` from the project directory. If the project has a local copy, update that file. |
| `highlightx.sty` is missing | `hlite` loads it automatically when highlights are enabled. On local TeX Live, run `tlmgr install highlightx`. |
| `simplekv.sty` is missing | Run `tlmgr install simplekv` in the TeX Live installation your editor uses. |
| `Undefined color` | Check the name’s case, load the relevant `xcolor` palette, or define the color before using it. For HTML colors, define a name first and pass that name in brackets. |
| A custom inline command fails | Try wrapping the entire command and its arguments in `\mbox{...}`, as in `\hlight{See \mbox{\myreference{orbit}} for details.}`. |

If a selection still causes an error, include a small `.tex` example,
your compiler and TeX distribution, and the first error in the log.
[Open an issue](https://github.com/neutrinoevent/hlite/issues/new)

## How hlite uses highlightx

`hlite` draws its backgrounds with `highlightx`’s `\HighlightText*`, which
already wraps text and accepts a background color through `bg=...`.
`hlite` adds per-selection color shorthand, support for common inline
commands, and a document-wide off switch. The underlying `highlightx`
interface exposes TikZ styling and a separate formula highlighting
command. For a short label that fits on one line, `xcolor` provides `\colorbox`.
[highlightx documentation](https://ctan.org/pkg/highlightx) ·
[xcolor documentation](https://ctan.org/pkg/xcolor)

## Regression check

Run `python3 tests/check.py` with pdfLaTeX and PyMuPDF installed. The check
compiles [the test document](tests/regression.tex) and verifies wrapped
highlights, citation text, working links, and an `off` build that renders
like the unmarked document. [PyMuPDF installation](https://pymupdf.readthedocs.io/en/latest/installation.html)
