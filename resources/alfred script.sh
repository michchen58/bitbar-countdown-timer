sed -i '' -e '$ d' ~/Applications/BitBar/plugins/countdown_timer/data/source.txt

# clear files
rm ~/Applications/BitBar/plugins/countdown_timer/data/data.txt
> ~/Applications/BitBar/plugins/countdown_timer/data/source.txt

# calculate time (convert date to seconds)
curTime=$(date +%s)
# calculate end time
let curTime+=60*10

# write file
echo {query} >> ~/Applications/BitBar/plugins/countdown_timer/data/source.txt

# if contains cancel then stop here
if [[ {query} == *"cancel"* ]]; then
	echo "contains 'cancel'"
	rm ~/Applications/BitBar/plugins/countdown_timer/data/data.txt
	rm ~/Applications/BitBar/plugins/countdown_timer/data/source.txt
elif [[ {query} == *"x"* ]]; then
	echo "contains 'x'"
	rm ~/Applications/BitBar/plugins/countdown_timer/data/data.txt
	rm ~/Applications/BitBar/plugins/countdown_timer/data/source.txt
fi
