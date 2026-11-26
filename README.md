![hlite set in TeX braces over blue and yellow highlights](assets/hlite-banner.jpg)

# hlite

Alexander Nichols · Old Dominion University · [MIT License](LICENSE)

Line-wrapping highlights for LaTeX drafts and reports.

## Why use hlite?

Mark an entire finding, including the inline equation, figure reference,
or citation that gives it context. Use `\hlight[color]{text}` to choose
a color for each selection. As you revise the sentence, the background
follows the text across line breaks.

When you need a submission copy, switch to `\usepackage[off]{hlite}`.
One preamble edit gives you a clean PDF and keeps your review marks
in the source so you can turn them back on for the next revision.

## Get a highlight on the page

1. Put `hlite.sty` next to the main `.tex` file. On GitHub, open the style
   file and choose **Download raw file**. [Open `hlite.sty`](hlite.sty)
2. Add `\usepackage{hlite}` to your preamble. It loads `highlightx`
   automatically. If TeX Live reports that `highlightx.sty` is missing,
   run `tlmgr install highlightx`.
3. Compile this example with pdfLaTeX. Run it twice so the background
   lands behind the text. `latexmk -pdf` can handle the extra pass.

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

`\hlight` and `\hlite` are interchangeable. Omit the optional argument
for pale yellow (`yellow!18`).

To share one copy across TeX Live projects, put the style file at
`tex/latex/hlite/hlite.sty` inside your personal TeX tree. Find that
tree with `kpsewhich -var-value=TEXMFHOME`.

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
\hlite[reviewpeach]{Check the reported units before submission.}
```

To use extra named colors such as `ForestGreen`, load
`\usepackage[dvipsnames]{xcolor}` before `hlite` or any other package that
loads `xcolor`. Use the spelling and capitalization from the color list.
[xcolor named colors](https://tug.ctan.org/macros/latex2e/contrib/xcolor/xcolor.pdf#page=38)

## Highlight math, references, and citations

Use the same command when a selection includes inline math or a reference.
For example, in a document with the labels and citation key defined, write

```latex
\hlight[blue!12]{See Fig.~\ref{fig:orbit} and Eq.~\eqref{eq:period}
for the case \(\ell=1\).}
\hlight{This agrees with the earlier study \cite[p.~15]{smith2020}.}
```

| Inside a highlight | Supported forms |
| --- | --- |
| Inline math | `$...$` and `\(...\)` |
| Cross-references | `\ref` and `\pageref`, amsmath’s `\eqref`, hyperref’s `\autoref` and `\nameref`, and cleveref’s `\cref` and `\Cref` |
| Citations | `\cite`, natbib’s `\citep` and `\citet`, and biblatex’s `\parencite`, `\textcite`, and `\autocite` |
| Links and emphasis | hyperref’s `\href{url}{text}`, `\emph`, and `\textbf` |

Load the packages that provide the commands you use, and run the usual
BibTeX or Biber pass if your document calls for one. Existing PDF links
remain clickable.

Wrap one paragraph per highlight and leave display equations between
highlights. Each inline formula, reference, citation, or link stays
together. If a long citation or link runs past the margin, place it between
two highlights so LaTeX can break it normally.

## Build a clean copy

Replace `\usepackage{hlite}` with `\usepackage[off]{hlite}`. All marked text,
math, and links are typeset as ordinary content, and this mode can run
without `highlightx`. Switch back to `\usepackage{hlite}` to show the
backgrounds again.

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
| `simplekv.sty` is missing | Run `tlmgr install simplekv` in the TeX Live installation your editor uses. |
| `Undefined color` | Check the name’s case, load the relevant `xcolor` palette, or define the color before using it. For HTML colors, define a name first and pass that name in brackets. |
| A custom inline command fails | Try wrapping the entire command and its arguments in `\mbox{...}`, as in `\hlight{See \mbox{\myreference{orbit}} for details.}`. |

If a selection still causes an error, a small `.tex` example and the first
error in the log make it easier to reproduce.

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
