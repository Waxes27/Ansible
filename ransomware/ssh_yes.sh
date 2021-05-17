#!/usr/bin/expect -f

spawn /bin/ssh wtc@[lindex $argv 0]
expect " \r"

send -- "yes\n"

expect eof
