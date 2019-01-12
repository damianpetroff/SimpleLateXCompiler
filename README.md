# SimpleLateXCompiler

## Installation

## Documentation
there's no " between text on command
<p><s>p("hi")</s></p>
<p>p(hi)<p>

### Guard page
#### Author : author(...);
Function that initialise an author to the document
##### Argument
* Anything you want, but normaly text

#### Date : date([...,today]);
Function that initialise a date to the document.
##### Argument
* Anything you want, but normaly a date
* today : return the date of today (exemple: date(today) = 11.01.2019)

#### Title : title(...);
Function that initialise the title of the document
##### Argument
* Anything you want, but normaly text

### Document Element
#### Paragraph : p(...);
Function that create a paragraph who's equal to a text zone
##### Argument
* Anything you want, but normaly text

#### Image : img(link);
Function that add an image on the document
##### Argument
* link of the image (absolute or relative to the path of the source file)

#### Chapter : c(...);
Function that create a chapter on the document
Chapter are automaticaly numbered.
##### Argument
* Anything you want, but normaly text

#### Section : s(...);
Function that create a section relative to his parent (**chapter**)
Section are automaticaly numbered.
##### Argument
* Anything you want, but normaly text

#### SubSection : ss(...);
Function that create a subsection relative to his parent (**section**)
SubSection are automaticaly numbered.
##### Argument
* Anything you want, but normaly text

#### SubSubSection : sss(...);
Function that creat a subsubsection relative to his parent (**subsection**)
SubSubSection are automaticaly numbered.
##### Argument
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

##### Argument
* number will do a bulletlist enumerated automaticaly (1,2,3,...)
* letter will do a bulletlist itemized automaticaly (point)

#### Table : table(x/y){p(...);,...};
Function that create a table of a x,y size who contains the element p in the block
Note that you have to fill **every case** with a p() so if you want an empty cell, just put p(#)
##### Syntaxe
table(2/3)
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


##### Argument
* x for the number of column
* y for the number of row

## Errors
