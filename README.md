# SimpleLateXCompiler

## Installation
#### Requirements
- Having an up-to-date implementation TeX/LateX  such as [MiKTeX](https://miktex.org/)
- Install the following package :
  - **geometry**, for magins
  - **babel**, for language
  - **graphicx**, for images
  - and **tabularx** for tables

## How To Run


## Documentation
there's no " between text on command
<p><s>p("hi")</s></p>
<p>p(hi)<p>

### Document settings commands
|Attribute|Function|Description|
|:----:|:--:|:--:|
|Filename   | filename(`string`); | This is the only mendatory command. Defines the name of the generated files (`.tex` and `.pdf`). |
|Marge      | margin(`int`);      | Defines the margins of the document in centimeters. |
|Language   | language(`string`); | Defines the language of the document (generated text such as "Contents", "Chapter", etc.), can be any language that is supported by the `babel` package. If the given language is not present in your babel package, it should normally download itself during compilation. |
|Numbering  | numbering();        | Toggles the numbering of chapters and sections. Can be toggled multiple times within the document. |

#### Front page commands
|Attribute|Function|Description|
|:----:|:--:|:--:|
|Image | frontpageimg(`filepath`);| Defines the front page image, `filepath` can be relative or absolute, with no ". |
|Title | title(`string`);         | Defines the title of the document.  |
|Author| author(`string`);        | Defines the author(s) of the document.  |
|Date  | date([today,`string`]);  | Defines the date at the bottom of the front page.|


### Document elements
|Attribute|Function|Description|
|:----:|:--:|:--:|
|Table of Content   | toc();  | Generates a table of content.  |
|Abstract   | abstract(`string`)`;`  | Generates an Abstract page with the text provided. |
|Chapter   | c(`string`);  | Generates a chapter with the text provided.  |
|Section   | s(`string`);  | Generates a section with the text provided.  |
|SubSection   | ss(`string`);  | Generates a subsection with the text provided.  |
|SubSubSection   | sss(`string`);  | Generates a subsubsection with the text provided.  |
|Paragraph   | p(`string`);  | Generates a paragraph with the text provided. |
|Image | img(`filepath`); | Generates an image with its caption (filename). |
|Bullet list| bl( [enum, item] ) { p(`string`) [ , p(`string`) , ... ] }; | Generates a bulletlist (enumerate or itemized depending on the parameter) containing all paragraphs given in the block. See example later.
|Table | table(`int` n);  | Creates a simple dynamic table of n columns. Data are read in a row-major way.|

### Examples for bullet lists and tables
#### BulletList
```
bl(enum)
{
p(first);
p(second);
p(etc);
};
```
#### Table
```
table(2)
{
p(hi);
p(#);
p(#);
p(how are);
p(you ?);
};
```

This will be equivalent to :

| hi  |        |
|---|:--------:|
|   | **how are**  |
| **you ?**   |    |


### Try this !

To test is everything works on your end follow this quick steps:

1. In the folder of the python program create a new folder named `output`.
2. In this folder that you've juste made. Create a subfolder named `img`.
3. Inside this folder, put 3 `.jpg` images of your choice, doesn't matter what it is but you have to name them `img1.jpg`, `img2.jpg` and `img3.jpg`.
4. Back into the "root" folder, create a file named `input.txt`.
5. Copy-paste this code into the file :
```
filename(ExampleDocument);
language(english);
margin(2);
frontpageimg(img/img1.jpg);
title(Les fleurs);
author(Quentin Michel, Damian Petroff);
date(today);
abstract(In this document we show all our commands);
toc();
numbering();
c(Basics);
  s(Section);
    ss(Subsection);
      sss(Subsubsection);
        p(Paragraph);
        p(Another paragraph);
  s(Margins);
    p(Margin can be set manually using the margin function and giving a number. This number will be the margin in centimeters.);
    p(Putting the word auto is also possible which will set default margins, 3cm);
  s(Language);
    p(The language of the document is settable using the language function, and giving it a language, english is used here obviously.);
    p(The point of changing the language of the document is that all generated text such as Contents, Chapter, Abstract, etc will be translated into the given language.);
  s(Filename);
    p(The filename of the document is settable using the filename function, and giving it a name.);
    p(This name, say XYZ, will be the names of the generated files, XYZ.tex and XYZ.pdf);
  s(Table of content);
    p(The table of content is generated automatically using the toc command without argument, as simple as that.);
c(Bulletlists);
  s(Enumerate);
    bl(enum)
    {
    p(First a element of an enumerate list);
    p(Second one);
    p(Third one);
    p(etc);
    };
    s(Itemized);
    bl(item)
    {
    p(First a element of an itemized list);
    p(Second one);
    p(Third one);
    p(etc);
    };
c(Table);
  p(Tables are created using the table command, only the number of columns is given in parameter since the number of row is defined by the number of elements in the array and the number of columns);
  p(This is a table of 3 columns with 12 elements);
  table(3)
  {
  p(1);
  p(2);
  p(3);
  p(4);
  p(5);
  p(6);
  p(7);
  p(8);
  p(9);
  p(10);
  p(11);
  p(12);
  };

  p(This is a table of 3 columns with only 7 elements.);
  table(3)
  {
  p(1);
  p(2);
  p(3);
  p(4);
  p(5);
  p(6);
  p(7);
  };

  p(This is a table of 5 columns with some blank cells.);
  table(5)
  {
  p(1);
  p(2);
  p(3);
  p(#);
  p(5);
  p(#);
  p(7);
  p(8);
  p(9);
  p(#);
  p(11);
  p(12);
  p(13);
  p(14);
  p(#);
  };

  p(This is a blank table of 4 columns.);
  table(4)
  {
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  p(#);
  };

  p(This is an easy sudoku.);
  table(9)
  {
  p(#);
  p(6);
  p(7);
  p(#);
  p(#);
  p(#);
  p(5);
  p(2);
  p(#);
  p(4);
  p(#);
  p(#);
  p(3);
  p(5);
  p(#);
  p(#);
  p(7);
  p(#);
  p(1);
  p(#);
  p(9);
  p(#);
  p(6);
  p(#);
  p(#);
  p(#);
  p(8);
  p(2);
  p(8);
  p(#);
  p(5);
  p(#);
  p(#);
  p(#);
  p(6);
  p(#);
  p(5);
  p(#);
  p(#);
  p(1);
  p(#);
  p(#);
  p(#);
  p(8);
  p(2);
  p(#);
  p(1);
  p(#);
  p(8);
  p(2);
  p(#);
  p(#);
  p(3);
  p(#);
  p(6);
  p(#);
  p(5);
  p(2);
  p(#);
  p(7);
  p(#);
  p(#);
  p(#);
  p(#);
  p(7);
  p(1);
  p(#);
  p(3);
  p(#);
  p(#);
  p(#);
  p(6);
  p(#);
  p(4);
  p(#);
  p(6);
  p(#);
  p(#);
  p(#);
  p(5);
  p(3);
  };

c(Images);
  p(Calling the img function with a filepath to an image in parameter will generate it directly.);
  p(These are some random images);
  img(img/img1.jpg);
  p(They come with a caption, editable in the tex file);
  img(img/img2.jpg);
  img(img/img3.jpg);
numbering();
c(Numbering);
  p(As you can see, the chapters are not numbered anymore);
  s(Same for the sections);
    p(That is because the numbering function was called, which toggles numbering);
    p(call it again);
    numbering();
  s(And everything is numbered again);
  p(Please notice that everything that is not numbered will not be taken into account in the table of content. That is normal LateX behaviour. Activating numbering inside a chapter, as done here, will cause the table of content to potentially put content in wrong chapter.);
  p(For example, this section appears the in Table of content chapter.);
c(Front page);
  s(Image);
    p(The image on the front page is displayed using the frontpageimg function giving it the filepath of the desired img file.);
  s(Title of the document);
    p(The title of the document is displayed right under the image and is settable by using the title function.);
  s(Authors);
    p(Authors are defined using author function and the given string is displayed under the title of the document.);
  s(Date);
    p(date is basically a function where you can put a date, but it will display the current date if you put today in it. The date will show itself at the bottom of the front page.);
c(Needed packages);
  bl(item)
  {
  p(geometry, for magins);
  p(babel, for language);
  p(graphicx, for images);
  p(tabularx, for tables);
  };
```
6. Run the program using the command : `python SimpleLateXCompiler.py input.txt`
7. See that your `.tex` and `.pdf` files are correctly generated !
