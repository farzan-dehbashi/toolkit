#! /bin/bash

# clear 

store_in_file (){
    echo 'hi' > store_in_file.txt
}

conditional_statements(){
var=11
echo $var
if(($var == 10))  
then
    echo "Var is equal to 10"
elif (($var > 10))
then
    echo "Var is not equal to 10 and greater"
else
    echo "Var is not equal to 10 and smaller"
fi
}


loop (){
    n=1
    while((n <= 10))
    do
        echo $n
        n=$(($n+1))
    done
}

for_loop(){
    for i in 1 2 3 4 5 6
        do
            echo $i
        done
}

for_loop2(){
    for i in {0..10..5}
        do
            echo $i
        done
}

for_loop3(){
    for ((i = 0; i < 10; i=$(($i+3))))
    do
        echo $i
    done
}

inputs(){
    while read line
    do
        echo "$line"
    done < "$1"
}

strings(){
    echo "enter str1:"
    read str1
    echo "enter str2:"
    read str2

    if [ "$str1" == "$str2" ]
    then
        echo "strings are equal"
    else
        echo "strings are not equal"
    fi
    echo 
}

pipe(){
    ls ./ | while read line
    do
        echo  "$line exists in this directory"
    done
}

math(){
    var1=1
    var2=2
    echo $(( $var1 + $var2 ))
}

arrays(){
    var1=1
    var2=2
    var3=3
    arr=()
}
############
math


