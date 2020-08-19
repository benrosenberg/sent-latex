import os
# get filename
filename = input("Please enter the .txt filename: ")

# open file to read it
file = open(filename + ".txt", "r")

# read file lines into a list
file_line_list = file.readlines()
print("This is the file_line_list:")
print(file_line_list)
file.close()

# set prefix for latex within sent text file
latex_prefix = '!'

# get the lines with the latex demarcator in them (line begins with $)
latex_lines = []
for i in file_line_list:
    if i[0] == latex_prefix:
        latex_lines.append(i)

## skeleton for latex .tex file
before_eq_string = r"\documentclass{article} \usepackage{amsmath} \usepackage{amssymb} \begin{document} \thispagestyle{empty} \setlength{\parindent}{0pt}"
after_eq_string = r"\end{document}"

# run the lines with the latex demarcator through the latex2png script or something
for i in range(len(latex_lines)):
    ## get the names for the pdf and png files (`filename-latex-1`, `filename-latex-2`, etc.)
    latex_filename = filename + '-latex-' + str(i)

    ## create the .tex file from skeleton and latex_line in question
    latex_equation = latex_lines[i][1:]
    tex_file_contents = before_eq_string + latex_equation + after_eq_string
    tex_file = open(latex_filename + ".tex", "w")
    tex_file.write(tex_file_contents)
    tex_file.close()

    ## create the pdf (`pdflatex -jobname='filename to write' file.tex`)
    # to specify output name: -jobname=STRING flag before the FILE flag at the end
    os.system('pdflatex ' + latex_filename + '.tex')

    ## crop the pdf to remove excess whitespace
    os.system('pdfcrop -margin 3 ' + latex_filename + '.pdf ' + latex_filename + '.pdf')

    ## create the png from the pdf (`convert -density 3000 file.pdf -quality 90 file.png`)
    os.system('convert -density 3000 ' + latex_filename + '.pdf -quality 90 ' + latex_filename + '.png')

    ## remove all the useless (.aux, .log, .pdf, .tex) latex files
    os.system('rm *.log *.aux *.pdf *.tex')

# write a new file with the png references in it and overwrite the original filename
latex_line_count = 0
for i in range(len(file_line_list)):
    if file_line_list[i] != '\n' and file_line_list[i][0] == latex_prefix:
        file_line_list[i] = '#' + file_line_list[i] + '\n@' + filename + '-latex-' + str(latex_line_count) + '.png\n'
        latex_line_count += 1

file = open(filename + ".txt", "w")
file.write(''.join(file_line_list))
print("This is the new file_line_list:")
print(file_line_list)
file.close()
