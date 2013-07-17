for f in "$@";
    do fmt -w 79 $f > tmp; mv tmp $f
done
