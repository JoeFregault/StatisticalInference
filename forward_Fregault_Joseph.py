


def expect(xDistribution, function):
    xvals = list(xDistribution.keys())
    prob = list(xDistribution.values())

    outputlist = [function(xvals[j]) * prob[j] for j in range(len(prob))]

    expectation = sum(outputlist)
    return expectation


def forward(xT_1Distribution, eT, transitionTable, sensorTable):

    state0 = expect(transitionTable.get(0), lambda x: xT_1Distribution.get(x)) * sensorTable.get(0).get(eT)
    state1 = expect(transitionTable.get(1), lambda x: xT_1Distribution.get(x)) * sensorTable.get(1).get(eT)

    alpha = state0 + state1

    output = {0:state0/alpha, 1:state1/alpha}    
    return output

def main():
    
    pX0={0:0.3, 1:0.7}
    e=1
    transitionTable={0:{0:0.6, 1:0.4}, 1:{0:0.3, 1:0.7}}
    sensorTable={0:{0:0.6, 1:0.3, 2:0.1}, 1:{0:0, 1:0.5, 2:0.5}}
    
    xTDistribution=forward(pX0, e, transitionTable, sensorTable)
    print(xTDistribution)

if __name__=="__main__":
    main()
