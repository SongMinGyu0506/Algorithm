import sys


s = sys.stdin.readline().rstrip('\n')
s_list = list(s)
s_list.reverse()
ok_counter = False
reverse_s = ''.join(s_list)
if s == reverse_s:
    print(len(s))
else:
    for i in range(1,len(s)):
        q = list(s[0:i])
        q.reverse()
        a = ''.join(q)

        tmp_s = s + a
        tmp_s_list = list(tmp_s)
        tmp_s_list.reverse()
        reverse_tmp = ''.join(tmp_s_list)
        if tmp_s == reverse_tmp:
            ok_counter = True
            print(len(tmp_s))
            break
    if ok_counter == False:
        print(len(tmp_s))