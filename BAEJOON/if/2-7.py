T,M=map(int,input("").split())
time = int(input(""))
if (time+M)<60:
    print("{0} {1}".format(T,time+M))
elif T+(((time+M))/60)<24 and time+M>=60:
    print("{0} {1}".format(int(T+(((time+M))/60)),int((time+M))%60))
else:
    print("{0} {1}".format((int((T+(((time+M))/60)))%24),int((time+M))%60))
