func round(n){
    n = n + 0.5
    n = int(n)
    if (n > 1000){
        print "Score over 1000 in file: "basename(FILENAME) "with value " n > "logs/err.txt"
        n = substr(n,1,3)
    }
    return int(n)
}

function basename(file, a, n) {
    n = split(file, a, "/")
    return a[n]
}

function editChromEnd(n){
    if (n == 16617 && NR !=1){
         n = 16616
        return n
    }
    return n
}
func modify_file(outputFile){
    $(NF+1) = "\".\""; if (NR!=1) print $1"\t"$2"\t"editChromEnd($3)"\t"$7"\t"round($6)"\t"$5"\t"$4 > outputFile
}

BEGIN{FS=OFS="\t"}
{
    modify_file(updatedpath)
}


