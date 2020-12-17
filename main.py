from threading import Thread
import itertools
import time


start = time.time()

def generator(num):
    res = itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&/()=?{[]}#", repeat=num)
    i = 0
    for pwd in res: 
        print (''.join(pwd),"Number:",i)
        i += 1

if __name__ == "__main__":
    howoften = (input("Type a number: "))

    for i in range(int(howoften)):
        threading_counter = len(howoften)
        t = Thread(target=generator(int(i+1)))

    t.start()
    end = time.time()
    print("finished in",end - start)
