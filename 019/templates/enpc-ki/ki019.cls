\ProvidesClass{ki019}[05/07/2017 KI Clubinfo des Ponts]
\LoadClass[11pt]{article}

\RequirePackage[a4paper,margin=1.75cm]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage[frenchb]{babel}
\RequirePackage[md]{titlesec}
\RequirePackage{tikzpagenodes}
\usetikzlibrary{calc}
%\RequirePackage{atbegshi}
%\RequirePackage{everypage}
\RequirePackage{mdframed}

\RequirePackage{fontspec}
\newfontfamily\titlefont[Path = fonts/]{Telex-Regular.ttf}
\setmainfont[
    Extension=.ttf,
    UprightFont= *-Light,
    BoldFont=*-Bold,
    Path = fonts/
]{Nunito}


\setlength{\parindent}{1em}
\setlength{\parskip}{1em}
\definecolor{header}{RGB}{45, 45, 45}
\definecolor{footer}{RGB}{191, 30, 45}
\definecolor{primary}{RGB}{0, 161, 75}
\definecolor{secondary}{RGB}{191,27,44}
\definecolor{exemplebg}{RGB}{224,252,218}

\newenvironment{kiframe}
  {\vspace{1em}\begin{mdframed}[linewidth=0,backgroundcolor=exemplebg]}
  {\end{mdframed}\vspace{-0.5em}}

\newcommand{\Header}[1]{
\begin{tikzpicture}[remember picture,overlay,baseline=0pt]
\fill[primary]
  ([yshift=-4.1cm]current page.north west) --
  ([xshift=-4.62cm,yshift=-2.55cm]current page.north east) --
  ([yshift=-4.97cm]current page.north west) -- cycle;
\fill[header]
  (current page.north west) -- (current page.north east) --
  ([yshift=-2.15cm]current page.north east) --
  ([xshift=-4.62cm,yshift=-2.59cm]current page.north east) --
  ([yshift=-4.14cm]current page.north west) -- cycle;
  \node[anchor=base west, white,font=\Huge\titlefont,xshift=5cm,yshift=-1.7cm] at (current page.north west){#1};
  \node[anchor=north west,xshift=0.5cm,yshift=-0.2cm] at (current page.north west)
    {\includegraphics[height=3cm]{../../logos/Logo_fond_gris_blanchi.png}};
\end{tikzpicture}
}
\newcommand{\Footer}{
\begin{tikzpicture}[remember picture,overlay,baseline=0pt]
\fill[footer]
  ([yshift=0.5cm]current page.south west) --
  ([yshift=1.08cm]current page.south west) --
  ([xshift=12.01cm,yshift=0.74cm]current page.south west) -- cycle;
\fill[header]
  (current page.south west) -- (current page.south east) --
  ([yshift=0.96cm]current page.south east) --
  ([xshift=12.01cm,yshift=0.78cm]current page.south west) --
  ([yshift=0.54cm]current page.south west) -- cycle;
\end{tikzpicture}
}

\pagestyle{empty}
%\AtBeginShipout{\Header\Footer}
%\AtBeginShipoutFirst{\Header\Footer}
%\AddEverypageHook{\Header\Footer}

\let\emph\relax % there's no \RedeclareTextFontCommand
\DeclareTextFontCommand{\emph}{\bfseries}

\newcommand{\primary}[1]{{\color{primary}#1}}
\newcommand{\secondary}[1]{{\color{secondary}#1}}

\let\oldsection\section
\renewcommand{\section}[1]{\newpage\Header{#1}\vspace{2cm}}

\let\oldsubsection\subsection
\renewcommand{\subsection}[1]{{\color{primary}\titlefont\oldsubsection*{#1}}\vspace{-1em}}

\let\oldsubsubsection\subsubsection
\renewcommand{\subsubsection}[1]{{\oldsubsubsection*{#1}}\vspace{-1em}}
