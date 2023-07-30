echo "ashish"
echo \<Hello\>]KrishnaBalaram\  ## Backslash is the special character which represents at endline line to skip the endline cahracter
## Also backslash ignores the special meaning of characters
echo '\<Hello>]Krishna\' 
echo "\<Hello>]Krishna\""
echo "ashish"
var1="Krishna"
echo "$var1" #-> value is printed
echo "`date`" #date is executed
echo '$var1'
echo "hostname"
echo "`hostname`" # Within `` backquote command is given and it is executed
#   ‘$’, ‘`’, ‘”’, ‘\’, have special meaning in the double quote

## Echo vs printf. printf provides more granular output option through which we can control the output.
# printf [-v var] [format specifiers] [arguments]


# printf "formating options" arg1 arg2 arg3
# echo [option] arg1 arg2