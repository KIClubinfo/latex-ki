\ProvidesClass{ki019}[05/07/2017 KI Clubinfo des Ponts]
\LoadClass[11pt]{article}

\RequirePackage[a4paper,margin=1.75cm]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage[frenchb]{babel}
\RequirePackage[md]{titlesec}
\RequirePackage{tikzpagenodes}
\usetikzlibrary{calc}
\RequirePackage{atbegshi}
\RequirePackage{mdframed}

\RequirePackage{fontspec}
\newfontfamily\titlefont[Path = fonts/]{Telex-Regular.ttf}
\setmainfont[
    Extension=.ttf,
    UprightFont= *-Light,
    BoldFont=*-Bold,
    Path = fonts/
]{Nunito}


\setlength{\parindent}{0em}
\setlength{\parskip}{1em}
% vert : 13, 161, 75
% rouge : 192, 30, 51
\definecolor{ki019}{RGB}{5, 5, 5}
\definecolor{bg}{RGB}{231,241,253}

\newenvironment{kiframe}%
  {\begin{mdframed}[linewidth=0,backgroundcolor=bg]\vspace{-1em}}%
  {\end{mdframed}}

\newcommand{\Header}[1]{%
\begin{tikzpicture}[remember picture,overlay,baseline=0pt]
\fill[ki019]
  (current page.north west) -- (current page.north east) --
  ([yshift=-3.0cm]current page.north east) --
  ([yshift=-2.5cm]current page.north west) -- cycle;
  \node[anchor=base west, white,font=\Huge\titlefont,xshift=3.3cm,yshift=-1.5cm] at (current page.north west){#1};
  \node[anchor=north east,xshift=-0.5cm] at (current page.north east)%
    {\includegraphics[height=2.5cm]{logo-ki019.png}};
\end{tikzpicture}%
}
\newcommand\Footer{%
}

%\pagestyle{empty}
%\AtBeginShipout{\Header\Footer}
%\AtBeginShipoutFirst{\Header\Footer}

\let\emph\relax % there's no \RedeclareTextFontCommand
\DeclareTextFontCommand{\emph}{\bfseries}

\let\oldsection\section
\renewcommand{\section}[1]{\newpage\Header{#1}\vspace{1cm}}

\let\oldsubsection\subsection
\renewcommand{\subsection}[1]{{\color{ki019}\titlefont\oldsubsection*{#1}}\vspace{-1em}}

\let\oldsubsubsection\subsubsection
\renewcommand{\subsubsection}[1]{{\oldsubsubsection*{#1}}\vspace{-1em}}
