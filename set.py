# set의 유용함
mylist = ['a','b','a','c']
mylist = list(set(mylist)) # set은 중복을 저장하지 않으므로, 결과적으로 중복삭제가 된다

biglist = [str(i) for i in range(1000000)] # 1부터 대응하는 문자열에 맞추어 저장. 즉, '72'가 아닌 'H'
print("abc" in biglist)
bigset = set(biglist)
print("abc" in bigset) # set이 훨씬 빠르다