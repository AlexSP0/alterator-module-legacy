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
			writefilename=$writedirectory$cleanfilename
			ext=".backend"

			echo "[Manager]" > $writefilename$ext
			echo "module_name = executor" >> $writefilename$ext
			echo "node_name = $cleanfilename" >> $writefilename$ext
			echo  >> $writefilename$ext
			echo "interface_name = object" >> $writefilename$ext
			echo >> $writefilename$ext
			echo "[Info]" >> $writefilename$ext
			echo "execute = cat /usr/share/alterator/applications/$cleanfilename.desktop" >> $writefilename$ext
			echo "stdout_bytes = enabled" >> $writefilename$ext
			echo "action_id = Info" >> $writefilename$ext 
		fi
	done
done

