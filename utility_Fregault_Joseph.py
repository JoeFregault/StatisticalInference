

def expect(xDistribution, function):
    xvals = list(xDistribution.keys())
    prob = list(xDistribution.values())

    outputlist = [function(xvals[j]) * prob[j] for j in range(len(prob))]

    expectation = sum(outputlist)
    return expectation

def getSPrimeProbability(sPrime, action, s0Distribution, transitionTable):
    sPrimeProbability = expect(s0Distribution, lambda s0: transitionTable.get(s0).get(action).get(sPrime))
    return sPrimeProbability # probability of you ending up in the state of s prime given action

def getEU(action, sPrimeDistributionGivenAction, utilityTable):
    getUtility = lambda sPrime: utilityTable.get(sPrime)
    EU = expect(sPrimeDistributionGivenAction[action], getUtility)
    return EU


def main():
    s0Distribution={0:0.125, 1:0.25, 2:0.0625, 3:0.0625, 4:0.25, 5:0.25}
    utilityTable={0:2000, 1:-500, 2:100, 3:1000, 4:0, 5:-5000}
    #{s0:{a:{s':p}}}, p is the probability of the event (Start from s0, take action a, end up at s')
    transitionTable={0:{0:{0:1,1:0,2:0,3:0,4:0,5:0},\
                        1:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        2:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        3:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        4:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        5:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9}},\
                     1:{0:{0:0,1:1,2:0,3:0,4:0,5:0},\
                        1:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        2:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        3:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        4:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        5:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05}},\
                     2:{0:{0:0,1:0,2:1,3:0,4:0,5:0},\
                        1:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        2:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        3:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        4:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        5:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0}},\
                     3:{0:{0:0,1:0,2:0,3:1,4:0,5:0},\
                        1:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        2:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        3:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        4:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        5:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0}},\
                     4:{0:{0:0,1:0,2:0,3:0,4:1,5:0},\
                        1:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        2:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        3:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        4:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        5:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0}},\
                     5:{0:{0:0,1:0,2:0,3:0,4:0,5:1},\
                        1:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        2:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        3:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        4:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        5:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05}}}
    
    
    possibleAction = [0,1,2,3,4,5]
    possibleSPrime = [0,1,2,3,4,5]
     
    sPrimeDistribution={action:{sPrime:getSPrimeProbability(sPrime, action, s0Distribution, transitionTable) for sPrime in possibleSPrime} for action in possibleAction}
    EU = {action: getEU(action, sPrimeDistribution, utilityTable) for action in possibleAction }
    print(EU)




if __name__ == '__main__':
    main()
