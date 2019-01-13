# SimpleLateXCompiler

## Installation

## Documentation
there's no " between text on command
<p><s>p("hi")</s></p>
<p>p(hi)<p>

### Guard page
#### Author : author(...);
Function that initialise an author to the document
##### Arguments
* Anything you want, but normaly text

#### Date : date([...,today]);
Function that initialise a date to the document.
##### Arguments
* Anything you want, but normaly a date
* today : return the date of today (exemple: date(today) = 11.01.2019)

#### Title : title(...);
Function that initialise the title of the document
##### Arguments
* Anything you want, but normaly text

#### FrontPageImage : frontpageimg(path);
Function that add an image only in the frontpage
##### Arguements
* link of the image (absolute or relative to the path of the source file)

### Document settings (details)
#### Marge : marge(auto);
##### Arguments

#### Margin : margin(...);
##### Arguments

#### Numbering : numbering();
##### Arguments
NO ARGUMENTS

#### Filename : filename(...);
Function that set the name of the .tex file it will generate + .pdf
##### Arguments
Anything you want but normaly text, and something like "rapport_..."

#### Language : language(...);
Function that aload you to change the language of the document (to change the language of some title like the table of content or the chapter)
##### Arguments
Languages like : (if you don't have the language downloaded, it will normaly download automaticaly)
* french
* english
* spanish
* ...

### Document Element
#### Abstract : abstract(...);
Function that create a an abstract of you document
##### Arguments
* Anything you want but normaly text

#### Paragraph : p(...);
Function that create a paragraph who's equal to a text zone
##### Arguments
* Anything you want, but normaly text

#### Table of Content : toc();
Function that create a table of content dynamic
##### Arguements
NO ARGUMENTS

#### Image : img(path);
Function that add an image on the document
##### Arguments
* link of the image (absolute or relative to the path of the source file)

#### Chapter : c(...);
Function that create a chapter on the document
Chapter are automaticaly numbered.
##### Arguments
* Anything you want, but normaly text

#### Section : s(...);
Function that create a section relative to his parent (**chapter**)
Section are automaticaly numbered.
##### Arguments
* Anything you want, but normaly text

#### SubSection : ss(...);
Function that create a subsection relative to his parent (**section**)
SubSection are automaticaly numbered.
##### Arguments
* Anything you want, but normaly text

#### SubSubSection : sss(...);
Function that creat a subsubsection relative to his parent (**subsection**)
SubSubSection are automaticaly numbered.
##### Arguments
* Anything you want, but normaly text

### Multiple Element
#### BulletList : bl([number, point]){p(...);,...};
Function that create a bulletlist of the element p put in the block
The syntax must be respected to work
##### Syntaxe
bl(number)
{
p(...);
p(...);
};

##### Arguments
* number will do a bulletlist enumerated automaticaly (1,2,3,...)
* letter will do a bulletlist itemized automaticaly (point)

#### Table : table(x){p(...);,...};
Function that create a table of a x column and y row who's dynamic. It contains the element p in the block
Note that you have to fill **every case** with a p() so if you want an empty cell, just put p(#)
##### Syntaxe
table(2)
{
p(#);
p(hi);
p(#);
p(how are);
p(#);
p(you ?);
};

this will equal to something like :

|   | hi       |
|---|----------|
|   | **how are**  |
|   | **you ?**    |


##### Arguments
* x for the number of column

## Errors
