# hlite

Add a soft background to selected text in LaTeX. Choose the color for each
selection and use one package option to produce a clean copy.

## Install

Put [hlite.sty](hlite.sty) beside the main LaTeX file. To use it across projects
with TeX Live, put it under the personal TeX tree at
`tex/latex/hlite/hlite.sty`. Run `kpsewhich -var-value=TEXMFHOME` to find
that tree.

Enabled highlights use [highlightx](https://ctan.org/pkg/highlightx). If your
TeX Live installation lacks it, install it with `tlmgr install highlightx`.

## Use

    \documentclass{article}
    \usepackage{hlite}

    \begin{document}
    \hlight{This uses the default pale yellow.}

    \hlight[blue!12]{This selection can wrap across lines and include
    inline math such as $D=4.45\times10^{-8}$.}
    \end{document}

The optional argument accepts an xcolor name or mix. A selection can span several printed lines within a paragraph. With pdfLaTeX, compile twice to place the highlights. TeXstudio's
usual pdfLaTeX build works.

For a clean copy, load the package as follows.

    \usepackage[off]{hlite}

The off option typesets the contents of each selection directly. A clean
build can run without highlightx installed.
