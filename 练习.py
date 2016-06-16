'''#!/usr/bin/env python'''
#coding=utf-8
def func(*string):
    length = []
    #print string
    for line in string:
        if isinstance(line, str):
            
            length.append(len(line))
            #print len(line)
        else:
            length.append(len(str(line)))
            #print len(str(line))
    #print length
    len_max = max(length)
    #print len_max
    mark = []
    start = 0
    end = len(length)
    #print length.count(len_max)
    for num in range(length.count(len_max)):    
         temp = length.index(len_max,start, end)
         print temp
         mark.append(temp)
         start = temp + 1
         end  = len(length)

    
    for times in mark:
        print "Max string is %s" % string[times]

if __name__ == "__main__":
    s = ["abc", "bbc", "ooxx", "a", "b", "linyu", "fish"]
    print '列表只有字符串的：', s
    func(*s)

    s = ['abc', 'a', 'b', 'c', 'cba', 'qwe', 'q', 'tre']
    print '列表中的字符串有一样长的：', s
    func(*s)

    s = ['abc', 123, 'linux', 'python', 1234567]
    print "列表中带有整数的：", s
    func(*s)
    
