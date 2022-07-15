def randomnumber(low: int, high: int):
    from subprocess import run
    open('main.c', 'w').write('''#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    srand(time(NULL));
    int r = (rand() % ( ''' + str(high) + ' - ' + str(low) + ''')) + ''' + str(low) + ''';
    printf("%d", r);
    return 0;
}''')
    run(['gcc main.c -o out'], shell=True)
    return run(['./out'], capture_output=True, text=True).stdout


def random_array(low: int, high: int, length: int):
    from random import uniform
    return [uniform(low, high) for i in range(length)]


def random_normal_array(low: int, high: int, length: int):
    array = random_array(low, high, length)
    return sorted(array[len(array)//2:]) + sorted(array[len(array)//2:], reverse=True)
