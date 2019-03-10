# time_ranges is list of lists
timez = [[3, 10], [1, 6], [4, 8], [6, 13], [9, 12]]
print(timez)
print()

def offset(pair):
    return pair[0]

def type_p(pair):
    return pair[1]

def create_pairs(time_ranges):
    tuples_list = [] # list of start and end tuples
    
    for t_range in time_ranges:
        start = (t_range[0], -1)
        end   = (t_range[1], +1)
        
        #print(start)
        #print(end)
        #print()

        tuples_list.append(start)
        tuples_list.append(end)
        
    return tuples_list



def Marzullo(time_ranges):
    best_start = 0
    best_end = 0
    
    tuples_list = create_pairs(time_ranges)
    
    print(tuples_list)
    
    # sort dem bitches
    tuples_list = sorted(tuples_list, key=lambda x: (x[0], -x[1]))
    
    print(tuples_list)
    
    best = 0
    current = 0
    
    for i in range(len(tuples_list)):
        print("Step: ", i)
        
        current = current - type_p(tuples_list[i])
    
        if (current > best):
            best = current
            best_start = offset(tuples_list[i])
            best_end = offset(tuples_list[i + 1])

        print(tuples_list[i], "\tCurrent:", current, "\tBest:", best)    
    return [best_start, best_end]


print(Marzullo(timez))
