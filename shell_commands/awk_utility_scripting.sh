## AWK command ##

# text patterns
# the action that is to be taken when a match is found 
# 

# awk options 'selection _criteria {action }' input-file > output-file
# awk '{print}' ./input_data/employees.txt ## By default prints all the lines
# awk '/manager/ {print}' ./input_data/employees.txt ## prints only those lines in which manager is found
#awk '{print $1 "," $2}' ./input_data/employees.txt
#awk '{print $1,$NF}' ./input_data/employees.txt # - NF prints last field
# awk 'NR==2,NR==4 {print $0}' ./input_data/employees.txt  # Prints line from 2 to 4
# awk '{print length($0) }' ./input_data/employees.txt # print each line length
#awk ' END {print length($0)}' ./input_data/employees.txt #print last line length
# awk '{ if($3=="sales") print $0 }' ./input_data/employees.txt #print all those lines in which third argument is sales
# awk '{ if (length($0) > max) max = length($0) } END { print max }' ./input_data/employees.txt ##prints largest line length
awk 'BEGIN {for(i=1;i<=6;i++) print "Square of",i,"is",i*i;}' # with comma space is automatically added

###
# awk '
#  	BEGIN { actions } 
#  	/pattern/ { actions }
#  	/pattern/ { actions }
#             ……….
# 	 END { actions } 
# ' filenames  

###


# BEGIN pattern: means that Awk will execute the action(s) specified in BEGIN once before any input lines are read.
# END pattern: means that Awk will execute the action(s) specified in END before it actually exits.


## To check if the given input is file

# if [ -f $file ] ; then

# else;

# fi