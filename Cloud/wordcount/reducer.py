

import sys
 
current_word = None
current_count = 0
word = None
 
#获取标准输入，即mapper.py的输出
#obtain stdin, which is the output of mapper.py
for line in sys.stdin:
    line = line.strip()
    #解析mapper.py输出作为程序的输入，以tab作为分隔符
    #Delimiter: \t
    word,count = line.split('\t',1)
    
    try:
        count = int(count)
    except ValueError:
        #非字符时忽略此行
        #Ignore
        continue
    #要求mapper.py的输出做排序（sort）操作，以便对连续的word做判断
    if current_word == word:
        current_count += count
    else:
        if current_word:
            #输出当前word统计结果到标准输出
            #Output the current result to stdin
            print ('%s\t%s' %(current_word,current_count))
        current_count = count
        current_word = word
 
#输出最后一个word统计
if current_word ==word:
    print ('%s\t%s' % (current_word,current_count))

# $ echo "foo foo quux labs foo bar quux" | ./mapper.py | sort -k1,1 | ./reducer.py