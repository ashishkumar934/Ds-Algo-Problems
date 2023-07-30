#!/bin/bash
# sed means stream editor
# Used for operations on file- like- insertion, deletion, find and replace(substitution)

# sed [options] [script] input_file


#sed 's/unix/linux/' $1 # It will replace first occurence of pattern i.e. unix with linux in given file for {each line}
# sed 's/unix/linux/2' $1 # It replaces the second occurence in each line.
# sed 's/unix/linux/g' $1 ## It will replace all the occurances.
# sed 's/unix/linux/3g' $1  ## It will replace from third to all the occurances

sed '4s/unix/linux/' $1 ## REplaces only in the specified line. For multiple lines 3,7 like this can be given

sed 's/unix/linux/p' $1 ## /p duplicates the replaced line. 
sed -n 's/unix/linux/p' $1  ## Prints only the replaced lines

## sed 'x,yd' filename.txt ## For deleting the lines /d to delete the lines matching the pattern.




