#Deobfuscated By xNot_Found
#Github : https://github.com/hatakecnk
clear
echo "You have downloaded the download file ? [y/n]"
read gil
if [ $gil = y ] || [ $gil = Y ]
then
python2 index.py
exit
fi
if [ $gil = n ] || [ $gil = N ]
then
sh install.sh
python2 index.py
exit
fi
sh cob.sh
