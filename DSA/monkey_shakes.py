import random

def generate(str_len):
    rand_sent = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    for i in range(str_len):
        rand_sent = rand_sent + random.choice(alphabet)
    
    return rand_sent
    
def score(goalstr, teststr):
    numSame = 0
    for i in range(len(goalstr)):
        if goalstr[i] == teststr[i]:
            numSame += 1
    return numSame/len(goalstr)

def main():
    
    goal_str = 'eastside to the westside'
    best_score = 0
    no_loops = 0
    
    gen_string = generate(len(goal_str))
    the_score =  score(goal_str, gen_string)
    best_str = ''
    
    while best_score < 1:
        
        if the_score > best_score:           
            best_score = the_score
            best_str = gen_string
            
        if no_loops%100000 == 0:       #prints every the best for every 0.1 mil loops
            print(best_score, best_str) 
            no_loops = 0
            best_score = 0 
            best_str = ''
            
        gen_string = generate(len(goal_str))
        the_score =  score(goal_str, gen_string)
        no_loops += 1

    
main()