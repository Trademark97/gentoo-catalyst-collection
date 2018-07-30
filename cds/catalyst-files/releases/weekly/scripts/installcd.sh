#!/bin/bash
# This is where we will put any release-specific fsscript code

# Tweak the inittab so that kmscon is used instead of mingetty
# I also leave one terminal (tty6) spare as a backup in case kmscon
# causes issues.

sed -e '/^c1/ s/mingetty/kmscon/' \
    -e '/^c2/ s/mingetty/kmscon/' \
    -e '/^c3/ s/mingetty/kmscon/' \
    -e '/^c4/ s/mingetty/kmscon/' \
    -e '/^c5/ s/mingetty/kmscon/' \
    -i /etc/inittab
