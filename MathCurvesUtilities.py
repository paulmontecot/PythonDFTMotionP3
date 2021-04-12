def DFT(dataFrame,m):
    lFrame_ = len(dataFrame) #frame length lFram = 2.Ls in publication
    # print 'lFrame', lFrame
    t = 0
    for n_ in range(lFrame_):
        t += dataFrame[n_]*cmath.exp(-2*math.pi*1j*m*n_/(lFrame_-1))
    return (t)
def entropyDFT(dftData,m):
    p_ = float(dftData[m])/np.sum(dftData[1:])
    return (p_)
def timeIntegral(n,time):
    timeIntegral = [time[0]]
        for k in range(1,n):
            g = timeIntegral.append(time[k]-time[k-1])
        return (g)
def integralData(n,rowData):
    integralData = np.empty((n,6))
        integralData[:] = np.NAN
        for k in range(0,n):
            integralData[k,:] = rowData[k,:6]*timeIntegral[k]
            if k>0 :
                integralData[k,:] += integralData[k-1,:]
            h = integralData[k,:]
        return(integralData[k,:])
def doubleIntegraldata(n,integralData,timeIntegral):
    doubleIntegralData = np.empty((n,6))
        doubleIntegralData[:] = np.NAN
        for k in range(0,n):
            doubleIntegralData[k,:] = integralData[k,:6]*timeIntegral[k]
            if k>0 :
                doubleIntegralData[k,:] += doubleIntegralData[k-1,:]
            j = doubleIntegralData[k,:]
        return(doubleIntegraldata[k,:])
def derivData(n,rowData):
    derivData = np.empty((n,6))
    derivData[:] = np.NAN
        for k in range(0,n):
            if k==0 :
                derivData[k,:] = (rowData[k+1,:6]-rowData[k,:6])/(time[k+1]-time[k])
            elif k==n-1 :
                derivData[k,:] = (rowData[k,:6]-rowData[k-1,:6])/(time[k]-time[k-1])
            else :
                derivData[k,:] = (rowData[k+1,:6]-rowData[k-1,:6])/(time[k+1]-time[k-1])
        return(derivData[k,:])
def doubleDerivData(n,deriveData):
    doubleDerivData = np.empty((n, 6))
    doubleDerivData[:] = np.NAN
    for k in range(0, n):
        if k == 0:
            doubleDerivData[k, :] = (derivData[k + 1, :6] - derivData[k, :6]) / (time[k + 1] - time[k])
        elif k == n - 1:
            doubleDerivData[k, :] = (derivData[k, :6] - derivData[k - 1, :6]) / (time[k] - time[k - 1])
        else:
            doubleDerivData[k, :] = (derivData[k + 1, :6] - derivData[k - 1, :6]) / (time[k + 1] - time[k - 1])
    return (doubleDerivData[k, :])

#CHECK VARIABLES NAMES