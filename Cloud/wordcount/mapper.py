
import sys
#input is stdin
for line in sys.stdin:
    #delete space 
    line = line.strip( )
    #以默认空格分隔行单词到words列表
    #Split word using space
    words = line.split( )
    for word in words:
        #输出所有单词，格式为“单词，1”以便作为reduce的输入
        #Output all words, the format is (word,1), and will be the input for reducer
        print ('%s\t%s' %(word,1))

# $ echo "foo foo quux labs foo bar quux" | ./mapper.py
# $ cat /tmp/test.txt | ./mapper.py