\ProvidesClass{ki020}[8/08/2018 KI Clubinfo des Ponts]
\LoadClass[14pt]{extarticle}

\RequirePackage[a4paper,margin=1.75cm]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage[french]{babel}
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
\definecolor{primary}{RGB}{66,134,244}
\definecolor{secondary}{RGB}{191,27,44}
\definecolor{exemplebg}{RGB}{211, 229, 255}

\newenvironment{kiframe}
  {\vspace{1em}
  \begin{mdframed}
    [linewidth=0,backgroundcolor=exemplebg]}
  {\vspace{0.8cm}\end{mdframed}\vspace{-0.5em}}

\newcommand{\Header}[1]{
\begin{tikzpicture}[remember picture,overlay,baseline=0pt]
\fill[primary]
  ([yshift=-4.4cm]current page.north west) --
  ([xshift=-4.62cm,yshift=-2.85cm]current page.north east) --
  ([yshift=-5.27cm]current page.north west) -- cycle;
\fill[header]
  (current page.north west) -- (current page.north east) --
  ([yshift=-2.45cm]current page.north east) --
  ([xshift=-4.62cm,yshift=-2.89cm]current page.north east) --
  ([yshift=-4.44cm]current page.north west) -- cycle;
  \node[anchor=base west, white,font=\Huge\titlefont,xshift=4.0cm,yshift=-2cm] at (current page.north west){#1 \vphantom{A}};
  \node[anchor=north west,xshift=0.5cm,yshift=-0.2cm] at (current page.north west)
    {\includegraphics[height=3cm]{../../logos/Logo_fond_gris_blanchi.png}};
\end{tikzpicture}
%\vspace{4cm}

\vspace{2.3cm}
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

%\pagestyle{empty}
%\AtBeginShipout{\Header\Footer}
%\AtBeginShipoutFirst{\Header\Footer}
%\AddEverypageHook{\Header\Footer}

\let\emph\relax % there's no \RedeclareTextFontCommand
\DeclareTextFontCommand{\emph}{\bfseries}

\newcommand{\primary}[1]{{\color{primary}#1}}
\newcommand{\secondary}[1]{{\color{secondary}#1}}

\makeatletter
%\let\oldsection\section
%\newcommand\section{\@startsection {section}{1}{\z@}%
%                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
%                                   {2.3ex \@plus.2ex}%
%                                   {\Header}}
\newcommand{\Section}[1]{\newpage\Header{#1}\addcontentsline{toc}{section}{#1}}

\let\oldsubsection\subsection
%\renewcommand{\subsection}[1]{{\color{primary}\titlefont\oldsubsection*{#1}}\vspace{-1em} \addcontentsline{toc}{subsection}{#1}}
\newcommand\Subsection{\@startsection{subsection}{2}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\large\bfseries\color{primary}}}
\renewcommand\subsection[1]{\Subsection*{#1}\vspace{-1em}\addcontentsline{toc}{subsection}{#1}}

\let\oldsubsubsection\subsubsection
%\renewcommand{\subsubsection}[1]{{\oldsubsubsection*{\secondary{#1}}}\vspace{-1em}}
\newcommand\Subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\normalsize\bfseries\color{secondary}}}
\renewcommand\subsubsection[1]{\Subsubsection*{#1}\vspace{-1em}\addcontentsline{toc}{subsubsection}{#1}}

\makeatother
