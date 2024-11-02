def tmp(my,w):
    if len(my)==w:
        return
    f=my[w]
    tmp(my,w+1)
    if w==len(my)-1:
        print("конец списка")#это же конец списка я верно отобразил?
    print(f)



my_list = list(map(int,input().split()))
w1=0
tmp(my_list,w1)