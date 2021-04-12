def PCA(dataSetMatrix):
# Principal Component Analysis
# features association: project features on specific vectors to reduce their number
# PCA function compute Ureduce (used by LogisticRegression.m and PLAY.m)
# cf. Coursera - Week 13 - PCA Algorithm
    m = len(dataSetMatrix[:1])  # number of training example
    X_ = dataSetMatrix
    X_ = np.array(X_)

# Compute eigen vectors and matrix
# formula p.28
    Sigma = (1 / float(m)) * np.dot(X_.T, X_)
    U, S, V = np.linalg.svd(Sigma, full_matrices=True)

# Get main componants
# formula p.29
    k = 1
    while (np.sum((S[:k]) / (np.sum(S))) < 0.99):  # precision up to 99#
        k = k + 1

    Ureduce = U[:, :k]

# Plot weight graph (optional)
    sU = np.dot(U.T, np.array([S]).T)
    wMeanFeatures = np.mean(np.abs(sU), axis=1)
    print ("wMeanFeatures = ", wMeanFeatures.shape)
    fig, ax = plt.subplots()
    ax.bar(range(len(wMeanFeatures)), wMeanFeatures, bottom=np.min(wMeanFeatures))
    plt.show()

    return Ureduce