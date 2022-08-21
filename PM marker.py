

def sacar_peso(miprot, mig):
    import sklearn
    import numpy as np
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt
    import math
    PM=[94, 66,45,29,21,14]
    #mig=[72,119,221,381,554,773]
    #miprot=182
    plt.scatter(mig, PM)
    logPM=np.log(PM)
    x=np.array(mig)
    x=x.reshape(-1,1)
    y=np.array(logPM)
    model=LinearRegression().fit(x, y)
    b=model.intercept_
    m=model.coef_
    lnY=m*miprot+b
    Y = math.exp(lnY)
    return Y
