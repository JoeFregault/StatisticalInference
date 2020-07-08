
def expect(xDistribution, function):
    xvals = list(xDistribution.keys())
    prob = list(xDistribution.values())

    outputlist = [function(xvals[j]) * prob[j] for j in range(len(prob))]

    expectation = sum(outputlist)
    return expectation



##################################################
#		Your code below each comment
##################################################  
def getVariance(xDistribution):
    
    #Step 1 - Calculate the expected value E(X) 
    function = lambda x: x
    mu = expect(xDistribution, function)

    def getSquaredDistanceToMu(x):
    #Step 2 - Calculate (X-E(X))^2
        sd = (x - mu) ** 2
        return sd
    #Step 3 - Calculate Variance: Var(X)=E((X-E(X))^2)
    variance = expect(xDistribution, getSquaredDistanceToMu)
    return variance

def main():
    xDistributionExample1={1: 1/5, 2: 2/5, 3: 2/5}
    functionExample1=lambda x: x ** 2 # squares an input
    print(expect(xDistributionExample1, functionExample1))
    print(getVariance(xDistributionExample1))
    
    xDistributionExample2={1: 1/6, -1/2: 1/3, 1/3: 1/4, -1/4: 1/12, 1/5: 1/6}
    functionExample2=lambda x: 1/x
    print(expect(xDistributionExample2, functionExample2))  
    print(getVariance(xDistributionExample2))

if __name__ == '__main__':
    main()