Visual Studio Code LaTeX Workshop Extension
version downloads installs rating license

Average time to resolve an issue Percentage of issues still open

LaTeX Workshop is an extension for Visual Studio Code, aiming to provide all-in-one features and utilities for LaTeX typesetting with Visual Studio Code.

This project won't be successful without contributions from the community, especially the current and past key contributors:

Jerome Lelong @jlelong
Takashi Tamura @tamuratak
Tecosaur @tecosaur
James Booth @jabooth
Thank you so much!

Note that starting from version 7.0.0, LaTeX-Workshop requires at least VSCode 1.34.0.

Manual
The manual of the extension is maintained as a wiki

Installation and basic settings
Requirements
Installation
Usage
Using Docker
Compiling
Building the document
Terminating the current compilation
Auto build
Cleaning generated files
LaTeX recipes
Magic comments
Catching errors
Linting
Viewing & synctex
Formatting
Multi file projects
Intellisense
Citations
References
Commands
Environments
Files
Snippets and shortcuts
Environments
Inserting Greek letters
Handy mathematical snippets
Font commands
Mathematical font commands
Surrounding text
Miscellaneous actions
Hovering features
Documentation of a package
Previewing equations
Previewing citation details
Previewing references
Documentation of a command
Playing with environments
Inserting an environment
Itemize like environments
Navigating
Closing the current environment
Surrounding selection with an environment
FAQ and common issues
Features (Taster)
This is not a complete list but rather a preview of some of the coolest features.

Build LaTeX (including BibTeX) to PDF automatically on save.

build process gif
View PDF on-the-fly (in VS Code or browser).

demo of preview feature
Direct and reverse SyncTeX. Click to jump between location in .tex source and PDF and vice versa.

demo of SyncTeX
Intellisense, including completions for bibliography keys (\cite{}) and labels (\ref{}).

intellisense demo
LaTeX log parser, with errors and warnings in LaTeX build automatically reported in VS Code.

error reporting demo
Linting
auto \item demo
Snippets

A lot of LaTeX commands can be typed using snippets starting in \, then type part of the command to narrow the search.

auto \item demo
Surround some selected text with a LaTeX command using ctrl+l, ctrl+w (⌘+l, ⌘+w on Mac). A new menu pops up to select the command. This works with multi selections. The former approach using \ has been deprecated.

wrap demo
We also provide a few other snippets mechanisms

Greek letters are obtained as @ + letter. Some letters have variants, which are available as @v + letter. See here.

greek letters demo
Common environments can be obtained by BXY where XY are the first two letters of the environment name, eg. BEQ gives the equation environment. If you want the star version of the environment, use BSXX, eg. BSEQ gives the equation* environment. See here.

BSAL demo
Common font commands can be obtained by FXY where XY are the last two letters of the font command name, eg. FIT gives \textit{}. See here.

FBF demo
Many other maths symbols can be obtained with the @ prefix. See here.

\frac shortcut demo \int shortcut demo
Shortcuts

In addition to snippets, there are shortcuts provided by the extension that allow you to easily format text (and one or two other things).

\emph{} demo
When the current line starts with \item or \item[], hitting Enter automatically adds a newline starting in the same way. For a better handling of the last item, hitting Enter on a line only containing \item or \item[] actually deletes the content of the line. The alt+Enter is bind to the standard newline command. This automatic insertion of \item can be deactivated by setting latex-workshop.bind.enter.key to false.

auto \item demo
Preview on hover. Hovering over the start tag of a math environment causes a mathjax preview to pop up.

auto \item demo
GitHub
The code for this extension is available on github at: https://github.com/James-Yu/LaTeX-Workshop

Like this work?
😄 Star this project on GitHub and Visual Studio Marketplace
😊 Leave a comment
☺️ Spare me some coffee via Paypal
License
MIT
