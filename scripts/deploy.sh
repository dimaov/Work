#!/bin/bash

DIR=`echo "$2" | cut -d . -f 1 `
if [ -d $HOME/$DIR ]; then
	echo "repo is already downloaded"
else
	git clone https://$LOGNAME@gitblit.dsp.ugo-wallet.com:8443/r/$1/$2
fi
function read_filename {
echo -e "\033[37;1;42m Enter filemane you want to deploy \033[0m"
read filename
}

function read_server_name {
echo -e "\033[37;1;42m Specify server nams \033[0m"
read dest
}

function read_path {
echo -e "\033[37;1;42m Enter path to the file \033[0m"
read paths
}
###############Working with files##############
cd $HOME/$DIR
git checkout $3 && git checkout $4
if [ "$?" -eq "0" ]; then 
	tag=`git describe --tag`
	echo "$tag" > $HOME/deploy.log 
	echo -e "\033[37;1;42m How many files do you need from this repo? \033[0m"
	read number
		for (( i=1; i<=$number; i++ )); do
			read_filename
        		match_num=`find  -type f -iname "$filename*" -path "./*" | tee -a $HOME/deploy.log | wc -l `
				if [ "$match_num" -eq "0" ]; then
					echo -e "\033[37;1;41m NO SUCH FILES \033[0m"
					exit
				fi
				if [ "$match_num" -gt "1" ]; then
					echo -e "\033[37;1;42m FILES THAT WERE FOUND ACCORDING YOUR FILENAME,PLEASE SPECIFY PATH OR SKIP IF YOU WANT TO MOVE ALL OF THEM \033[0m"
					find  -type f -iname "$filename*" -path "./*"
					read_path
					echo -e "\033[37;1;42m How many server you want to move that file on? \033[0m"
					read server_number
						for  (( j=1; j<=$server_number; j++ )); do
							read_server_name
							find -type f -iname "$filename*" -path "./$paths*" -exec scp {} $LOGNAME@$dest:$HOME/ \;
						done
				else
					echo -e "\033[37;1;42m File that was found \033[0m"
					find  -type f -iname "$filename*" -path "./*" 
					echo -e "\033[37;1;42m How many server you want to move that file on? \033[0m"
                			read server_number
						for  (( j=1; j<=$server_number; j++ )); do
                                			read_server_name
                                			find -type f -iname "$filename*" -path "./*" -exec scp {} $LOGNAME@$dest:$HOME/ \;
                        			done
				fi

		done
else 
	echo -e "\033[37;1;41m Exited with error wrong branch or tag \033[0m"	
fi














