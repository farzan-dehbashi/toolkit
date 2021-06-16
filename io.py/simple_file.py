sample_file = open('./tobe_read.txt', mode='r', encoding='utf8') #r w a
for line in sample_file:
    print(line, end='') #ends with '' not a new line

sample_file.close()