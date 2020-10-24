#!/bin/bash

until sudo systemctl restart pcscd &>/dev/null
do
    sleep 0.6
done

exit 0
