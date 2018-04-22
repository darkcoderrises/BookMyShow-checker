while true : 
do
    sh ./call_website.sh > website.html 
    var_a=`cat theaters.txt | wc -l`
    python ./read_website.py > theaters.txt
    var_b=`cat theaters.txt | wc -l`
    echo $var_a $var_b
    if [ $var_a -ne $var_b ]
    then 
        node send_msg.js
    fi
    sleep 60
done
