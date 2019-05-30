import time
def fibo_recursivo (n):
    if n <= 1:
        return n
    else:
        x = fibo_recursivo(n-1) + fibo_recursivo(n-2)
        ini = time.time()
        return x


def fibo_pd(n, tab):
    if n <= 1:
        return n
    if n in tab.keys():
        return tab[n]
    else:
        f = fibo_pd(n-1, tab) + fibo_pd(n-2, tab)
        tab[n] = f
        return f


def main():
    ini1 = time.time()
    print "fibo rec: ", fibo_recursivo(40)
    fim1 = time.time()
    ini2 = time.time()
    print "fibo pdf: ", fibo_pd(40, {})
    fim2 = time.time()
    print "tempo rec: ", (fim1-ini1)
    print "tempo pd: ", (fim2 - ini2)

if __name__ == '__main__':
    main()