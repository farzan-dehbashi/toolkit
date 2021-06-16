with open ('./tobe_read.txt') as sample_file:
    line = sample_file.readline()
    while line:
        print(line, end='')
        line = sample_file.readline()