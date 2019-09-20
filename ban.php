<?php

if (strtolower(substr(PHP_OS, 0, 3)) == "win") {
    $bersih = "cls";
} else {
    $bersih = "clear";
}

date_default_timezone_set('Asia/Jakarta');
$date = date('d~M~Y H:i:s');
$green = "\e[92m";
$red = "\e[91m";
$yellow = "\e[93m";
$blue = "\e[36m";
$cyan = "\e[0;36m";
$purple = "\e[0;35m";
$brown = "\e[0;33m";
$lightgray = "\e[0;37m";
$nick = "XerXez7 Gans";
$darkgray = "\e[1;30m";
$lightblue = "\e[1;34m";
$lightgreen = "\e[1;32m";
$lightcyan = "\e[1;36m";
$lightred = "\e[1;31m";
$lightpurple = "\e[1;35m";
$bg = "\033[48;9;32m";
$gb = "\033[0;0m";
$rd = "\033[41;2;32m";
pilih:
    system($bersih);

echo "
$green        W
       WWW
       WWW
      WWWWW       $lightred   [$darkgray SMS FRE :$lightpurple Install whit Termux$lightred  ]$green
W     WWWWW     W $lightred   [$darkgray Version :$lightpurple 1.3.1$lightred                ]$green
WWW   WWWWW   WWW  $lightred  [$darkgray Author  :$lightpurple IyXerXez777$lightred          ]$green
 WWW  WWWWW  WWW $lightred    [$darkgray Since   :$lightpurple 2k19-2k20$lightred            ]$green
  WWW  WWW  WWW   $lightred   [$darkgray Log     :$lightpurple $date$lightred ]$green
   WWW WWW WWW   $lightred    [$darkgray Team    :$lightpurple 2e4h-Buft-GblK CreW $lightred ] $green
     WWWWWWW
  WWWW$darkgray  |$green  WWWW
$darkgray        |$bg$lightred
YA)$lightgreen LANJUT $lightred |$darkgray NO)$lightgreen KEMBALI KE HALAMAN UTAMA$darkgray
[X] UNTUK ExIt
";
