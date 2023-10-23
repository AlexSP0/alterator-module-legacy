#!/bin/bash
writedirectory="/usr/share/alterator/backends/"
examplefilename="ljkafgldfg.dfsfsd"

mkdir -p $writedirectory
touch $writedirectory$examplefilename > /dev/null 2>&1

if [ $? -ne 0 ] 
then
	echo "Can't access $writedirectory"
	exit 1
fi

rm -f $writedirectory$examplefilename

for dir in "${@}" 
do
	for file in $dir*.desktop
	do
		if grep -q "[Desktop Entry]" $file
		then
			filename=`basename $file`
			cleanfilename=`echo $filename | sed 's/\..*//'`
			writefilename=$writedirectory$filename

			echo "[Manager]" > $writefilename
			echo "module_name = executor" > $writefilename
			echo "node_name = $cleanfilename" > $writefilename
			echo  > $writefilename
			echo "interface_name = object" > $writefilename
			echo > $writefilename
			echo "[info]" > $writefilename
			echo "execute = cat /usr/share/alterator/applications/$cleanfilename.desktop" > $writefilename
			echo "stdout_bytes = enabled" > $writefilename
		fi
	done
done

