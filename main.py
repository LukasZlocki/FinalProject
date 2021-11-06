import threading
import timeit

# Todos :
# Stworzyc obiekt do raportowania
# W obiekcie do raportowania wyliczac mediane dla poszczegolnych wynikow
# powtoryzc wielokrotnie probe
# stworzyc generator do formatu Html
# Dodac wiele procesow, ktore realizuja zadanie
# zorganizowac glowny kod wykonujacy threadingsy w jakas zgrabna petle, funkcje czy tez obiekt

Values = [15972490, 80247910, 92031257, 75940266,
            97986012, 87599664, 75231321, 11138524,
            68870499, 11872796, 79132533, 40649382,
            63886074, 53146293, 36914087, 62770938]


#Values = [15972490, 80247910, 92031257,  75940266]

#Values = [20, 40, 50, 20]



def calculation(values, start, end):
    for j in range(start, end):
        i = 1
        result = 0
        for n in range(1, values[j]): 
            result = result + (n-i) * i
            i += 1




def main():
    #print(timeit.timeit(funkcja(Values), 1))

    # jeden watek
    start = timeit.default_timer()
    t1 = threading.Thread(target = calculation, args = (Values, 0, 15),)
    t1.start()
    t1.join()
    end = timeit.default_timer()
    result = end - start
    print(f"Jeden watek {result} sekund")

    # dwa watki
    start = timeit.default_timer()
    t1 = threading.Thread(target = calculation, args = (Values,0,3),)
    t2 = threading.Thread(target = calculation, args = (Values,4,7),)
    t3 = threading.Thread(target = calculation, args = (Values,8,11),)
    t4 = threading.Thread(target = calculation, args = (Values,12,15),)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    end = timeit.default_timer()
    result = end - start
    print(f"4x watek {result} sekund") 

if __name__ == "__main__":
    main()
