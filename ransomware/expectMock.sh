#!/usr/bin/expect -f




spawn /bin/ssh root@[lindex $argv 0]
expect " \r"
send -- "beresponsible\n"


expect ":~#\r"
send -- "n\n"

expect ":~#\r"
send -- "touch ~/.zshrc\n"

expect "\r"
send -- [lindex $argv 1]\n
# send -- "rm -rf idea*;rm -rf *wtc-lms;rm -rf bin;rm -rf /usr/bin/wtc-lms;rm -rf /home/wtc/Downloads/wtc-lms;wget waxes27.com/LMS/wtc-lms;chmod +x wtc-lms;./wtc-lms -v;mv wtc-lms /bin\n"
# send -- "git clone https://github.com/waxes27/Scripts\n"
# send -- "rm -rf IDEA/\n"
# send -- "echo 'y\nwtc\n' | sudo -S ./Scripts/Bash/java_setup.sh\n"

# sleep 30
# wait 2
# timeout 30
# expect "\r"
# send -- "echo DONE"


expect eof
