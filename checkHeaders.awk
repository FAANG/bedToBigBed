BEGIN{FS="\t"}
headersPattern = NR == 1 && /^#chr\tstart\tend\twidth\tstrand\tscore$/ {p = 1}
{
    print headersPattern
    exit 0
}
