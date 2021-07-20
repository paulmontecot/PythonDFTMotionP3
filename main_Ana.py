import getFeaturesFromFile
import getFeaturesWindows
import plot
import pandas as pd
import MathUtilities
import os
# Put the path of the directory where the data is located (keep the r before the string)
path = r'C:\Users\CRI User\Documents\GitHub\PythonDFTMotionP3\goodata\Openclose'

def runfeaturesextract():

    # Go thru the folder with all datas
    for filename in os.listdir(path):

        # DataFrame Creation with the Data
        df = pd.DataFrame()
        df = df.append(pd.Dataframe(getFeaturesFromFile.datafromfile(path+'\\'+filename)), ignore_index=True)
        df.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
        # Datatype is the axis of data you want, you just have to replace by the correpsonding column. (exemple 'accX')
        datatype = ['accX']

        # Operations for Different versions of Data
        data = df[datatype]
        df['norme'] = MathUtilities.norme(df)
        norme = df['norme']
        df['integral'] = MathUtilities.integral(df, data)
        integral = df['integral']
        df['derivate'] = MathUtilities.derivData(df, data)
        derivate = df['derivate']
        angle = MathUtilities.angle(df, df.accX, df.accZ)

        # Get Features by Window, here you have to specify the type of data you want (data, norme, integral, derivate or angle).
        # The model is trained for the norme Data so plz extract from norme :)
        Xfinaldata, Yfinaldata = getFeaturesWindows.getFeaturesWindows(data, 1)

        # Create final DataFrame
        dffinaldata= pd.DataFrame(Xfinaldata)
        dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation']

        # This show the final dataframe in the interpreter
        print(dffinaldata)

        # This plot the little dashboard with the distributions of values
        plot.plotfeatures(dffinaldata)

        # This command create the new file with extracted features.
        # You could replace the path with where you want the file to be stocked in.
        # after the last \ you just have to write the name you want for the file and finish by .csv.
        # Then, you can click on the Play Button :)
        dffinaldata.to_csv(r'C:\Users\CRI User\Desktop\DataSets\openclosepierro.csv')

runfeaturesextract()

