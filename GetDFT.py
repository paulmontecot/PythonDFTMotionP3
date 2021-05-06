def DFT(dataFrame, m):
    lFrame_ = len(dataFrame)  # frame length lFram = 2.Ls in publication
    t = 0
    for n_ in range(lFrame_):
        t += dataFrame[n_] * cmath.exp(-2 * math.pi * 1j * m * n_ / (lFrame_ - 1))
    return t
def entropyDFT(dftData, m):
    p_ = float(dftData[m]) / np.sum(dftData[1:])
    return p_

def getDFT(data):

    absDFTData_ = np.empty((lengFrame, :))  # matrix containing DFT data from input data
            absDFTData_[:] = np.NaN
            for i in range(lengFrame):
                for j in range(9):
                    absDFTData_[i, j] = np.absolute(DFT(rowData[rg, j], i))

            # Add DC component as features (for each axis x,y,z)
            x_ += absDFTData_[0, :].tolist()

            # Add energy features (exclude DC component)
            x_ += (np.sum(np.power(absDFTData_[1:, :], 2), axis=0) / (lengFrame - 1)).tolist()

            # Add entropy features (exclude DC component)
            entropyDFTData_ = np.empty((lengFrame, 9))  # matrix containing DFT entropy data
            entropyDFTData_[:] = np.NaN
            for i in range(lengFrame):
                for j in range(9):
                    entropyDFTData_[i, j] = entropyDFT(absDFTData_[:, j], i)
            x_ += np.sum(entropyDFTData_[1:, :] * np.log(1 / entropyDFTData_[1:, :]), axis=0).tolist()  # normalize entropy

            # Add deviation features (time domain)
            datMean = np.mean(rowData[rg, :-1], axis=0)
            x_ += np.sum(np.power(rowData[rg, :-1] - datMean, 2), axis=0).tolist()