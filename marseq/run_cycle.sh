for g in ../*.gz
do
    bf=`basename $g`
    cf=`echo $bf | sed -r 's/.fq.gz//g'`
    if ! [ -f $cf.log ]
    then
        echo $cf
        qsub -N $cf -v inp=$g,out=$cf zdo_python.sh
        sleep 1
    fi
done


