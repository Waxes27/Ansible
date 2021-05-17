#!/usr/bin/expect -f

spawn /bin/scp [lindex $argv 1] root@[lindex $argv 0]:/home/root
expect " \r"
send -- "beresponsible\n"

expect eof
