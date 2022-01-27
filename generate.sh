#!/bin/sh

# Generate HTML pages from the specifications a directory above.
# Copyright (C) 2022 bellrise

not_specs='generate.sh|readme'
specs=$(find . -maxdepth 1 -type f | grep -Ev $not_specs | sed 's/\.\///')

rm -rf webpage/spec
mkdir -p webpage/spec

for spec in $specs; do
    p=webpage/spec/$spec.html
    echo Generating $p
    num=$(echo $spec | awk -F '-' '{ print $2 }')
    cat webpage/gen_html_head.html | sed "s/((RSD_NUM))/$num/" > $p
    echo '<h2>' >> $p
    cat $spec | head -n 1 >> $p
    echo '</h2>\n<p>' >> $p

    cat $spec | tail -n +4  |\
        sed 's/\&/\&amp;/'  |\
        sed 's/</\&lt;/'    |\
        sed 's/>/\&gt;/' >> $p
    cat webpage/gen_html_foot.html >> $p
done
