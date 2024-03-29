# sent-latex
attempt to make sent work with latex

will:
* allow you to have latex in your sent presentations
* capitalize on sent's ability to display images by having it display a latex png
* turn your sent txt file from one with latex into one with image references instead
* allow you to have basically whatever latex you want in a sent presentation, provided you know what the commands are
* put comments in the line preceding the latex so that you don't lose the original latex when you run the script

will not:
* allow you to have latex in the same slide as regular text
* bake you a cake

## dependencies:
* [sent](https://tools.suckless.org/sent/) (obviously)
* [farbfeld](https://tools.suckless.org/farbfeld/)
* [python](https://www.python.org/)
* [latex](https://www.latex-project.org/get/) and pdflatex
* [imagemagick](https://imagemagick.org/index.php)
* the [bilinear scaling patch for sent](https://tools.suckless.org/sent/patches/bilinear_scaling/) is *highly* recommended
* willingness to open up `/etc/ImageMagick-X/policy.xml` and edit a line 

## installation
after installing all dependencies and stuff, you need to edit the line in `/etc/ImageMagick-6/policy.xml` or whatever file corresponds to the version of ImageMagick you're using. see this stackoverflow post for details: [post](https://askubuntu.com/questions/1127260/imagemagick-convert-not-allowed)

## testing
after cloning the repository:
1. run `python convert-latex.py` in the main directory
    * when prompted for a ".txt filename", enter `example`
2. run `sent example.txt` in the same directory
if the sent presentation displays what it says it should display, you should be good.

## how it works
the comments in `convert-latex.py` should be self-explanatory

## how to use
to use this, first copy the `convert-latex.py` file into the same directory as the txt file you want to read with sent.

now, edit your txt file so that each equation is on its own page (empty line both before and after it). An example follows:

```
a command to display the latex equation "L=3" follows:

!$$L=3$$
```

there's a more complex example at the end of the readme.

make sure that you format it with the `latex_prefix` in front (in the above example and by default it's `!`; however, it can be easily changed in the `convert-latex.py` file). otherwise pdflatex will get have an aneurysm and your computer will explode.

finally, run `python convert-latex.py` and when prompted, enter the name of your txt file (without the .txt). a lot of scary text will pop up (!) but then you will have some nice png files which will be referenced with proper syntax

now you can do `sent (filename).txt` and you will have epic gamer moment

### a more complex example sent file

```
the next slide should be a list:

!\begin{enumerate} \item item \item $1+1=2$ \item item \end{enumerate}

the next slide should be a captioned equation:

!caption: $equation$

the next slide should be another captioned equation:

!caption: \\ $equation$

the next slide should be yet another captioned equation:

!caption: \\ $$equation$$
```
