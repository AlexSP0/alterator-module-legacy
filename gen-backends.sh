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
			desktopfilename=$filename
			filename=`tr "-" "_" <<< $filename`
			cleanfilename=`echo $filename | sed 's/\..*//'`
			cleandesktopfilename=`echo $desktopfilename | sed 's/\..*//'`
			writefilename=$writedirectory$cleanfilename
			ext=".backend"

			echo "[Manager]" > $writefilename$ext
			echo "module_name = executor" >> $writefilename$ext
			echo "node_name = $cleanfilename" >> $writefilename$ext
			echo  >> $writefilename$ext
			echo "interface_name = displayable" >> $writefilename$ext
			echo >> $writefilename$ext
			echo "[Info]" >> $writefilename$ext
			echo "execute = bash /usr/libexec/backend_helper.sh $cleandesktopfilename" >> $writefilename$ext
			echo "stdout_bytes = enabled" >> $writefilename$ext
			echo "thread_limit = 3" >> $writefilename$ext
			echo "action_id = Info" >> $writefilename$ext
		fi
	done
done

