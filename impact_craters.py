import matplotlib.pyplot as plt
import random
import math
import timeit

def impact_craters():
    x = [] # initialize x list
    y = [] # initialize y list
    time = [] # keep track of time the crater was made
    hold = 0.90 # baseline impact ratio so while will run
    last = 1 # number of impacts on last run
    area = 25 * 25 # area of data points on graph
    plt.title('Impact Craters')
    plt.ylabel('Kilometers')
    plt.xlabel('Kilometers')
    plt.axis([0, 500, 0, 500]) # sets graph to be 500km x 500km
    dub = timeit.default_timer() # baseline time to check for double runtime
    while(hold < 0.95): # while the ratio of impacts from the last ratio check is less than 95%
        clear = [] # empty list to use for crater removal due to obliteration
        inX = random.randint(0,500) # random X coordinate between 0 and 500
        inY = random.randint(0,500) # random Y coordinate between 0 and 500
        x.append(inX) # adds new value to end of x list
        y.append(inY) # adds new value to end of y list
        time.append(timeit.default_timer()) # adds time crater was made to time list
        for i in range(len(x) - 1): # iterated through x, excludes last x which is the new crater
            if x[i] > (inX-30) and x[i] < (inX+30): # if the x value is within range to be obliterated
                check = math.sqrt((inX - x[i])**2 + (inY - y[i])**2) # use pythag to determine distance from center of craters
                if check <= 30: # if crater is closer than 30km or half the diameter of obliteration
                    clear.append(i) # add location to clear list
        for i in range(len(clear),0,-1): # clear list runs backwards to not change locations as they are deleted from each list
            x.pop(i) # deletes i crater from x list
            y.pop(i) # deletes i crater from y list
            time.pop(i) # deletes i crater from time list
        if (timeit.default_timer() / dub) >= 2: # if current time is double start time
            hold = last / len(x) # calc ratio for amount of craters
            last = len(x) # update last for next calc
            dub = timeit.default_timer() # update for next time comparison
    final = timeit.default_timer() # will execute after while loop breaks, this is actual end of simulation
    print ("Number of Craters is:") 
    print (len(x))
    for i in range(len(x)):
        print('Crater', i + 1 , ': x -' , x[i] , ' y -', y[i], '@ -', time[i])
    plt.scatter(x , y , s = area, c = 'b', alpha = 1)
    plt.show()
    return (final)
    
    
def main():
    print(impact_craters())
    return (0)

if __name__ == "__main__":
    main()
