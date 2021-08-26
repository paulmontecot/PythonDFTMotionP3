import streamlit as st
import pandas as pd
import base64
import MathUtilities
import getFeaturesWindows
from zipfile import ZipFile
import SessionState

#Config of the app
st.set_page_config(
    # Can be "centered" or "wide". In the future also "dashboard", etc.
    layout="wide",
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    # String or None. Strings get appended with "• Streamlit".
    page_title="Features Extraction Interface \U0001F58A",
    page_icon="\U0001F58A Features Extraction Interface",  # String, anything supported by st.image, or None.
)

#app

st.title("Features Extraction Interface \U0001F58A")
st.markdown("**Fill the differents items then click on generate**")



#Data Infos
st.subheader('User ID')
user_id = st.text_input("")
st.sidebar.subheader("Data type")
datatype = st.sidebar.selectbox("",('accX','accY','accZ','Norme'))

st.subheader('BHK Score')
BHK_score = st.text_input(" ")
st.subheader('Handedness')
handed = st.selectbox('',('Right Handed', 'Left Handed'))
st.subheader('Level of constraint')
constraint = st.selectbox("",('1','2','3','4','5','6','7','8','9','10'))
st.subheader('Constraint type')
finger = st.checkbox("finger")
wrist = st.checkbox("wrist")
elbow = st.checkbox("elbow")
shoulder = st.checkbox("shoulder")
st.subheader('Frame Resolution')
int_val = st.number_input('', min_value=1, max_value=50, value=20, step=1)

#Data Upload
st.subheader('Please Upload Data \U00002B07')
uploaded_file = st.file_uploader("")

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    dataframe.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']

    #Data Type setting
    dataframe['Norme'] = MathUtilities.norme(dataframe)
    Norme = dataframe['Norme']
    st.write(dataframe)
    Data = dataframe[datatype]
    getFeaturesWindows.dataWindow = int_val

    #Features extraction
    Xfinaldata, Yfinaldata = getFeaturesWindows.getFeaturesWindows(Data, 1)
    dffinaldata = pd.DataFrame(Xfinaldata)
    # For Further analysis, adding pressure --> dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation','contact','pressure']
    dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation']

else:
     #To avoid display error
     dffinaldata = pd.DataFrame()

#Create Metrics
mean = dffinaldata.mean(axis=0)
median = dffinaldata.median(axis=0)
standard_deviation = dffinaldata.std(axis=0)
variance = dffinaldata.var(axis=0)

df_BHK = pd.DataFrame()
df_Global = pd.DataFrame()

#Optional: Convert True and False in Red or Green Dots
if finger == False:
    finger = "\U0001F534"
elif finger == True:
    finger = "\U0001F7E2"

if wrist == False:
    wrist = "\U0001F534"
elif wrist == True:
    wrist = "\U0001F7E2"

if elbow == False:
    elbow = "\U0001F534"
elif elbow == True:
    elbow = "\U0001F7E2"

if shoulder == False:
    shoulder = "\U0001F534"
elif shoulder == True:
    shoulder = "\U0001F7E2"

#Generate DataFrames
if st.button('GENERATE'):
    dataBHK = {"User ID" : user_id,"BHK score": BHK_score, "handedness": handed, "Constraint": constraint,"finger": finger, "wrist":wrist,"elbow":elbow,"shoulder":shoulder}
    dataglobal = {"Mean": mean, "Median": median, "standard deviation": standard_deviation, "variance": variance}
    df_BHK = pd.DataFrame.from_records([dataBHK])
    df_Global = pd.DataFrame.from_records(dataglobal)
    dffinaldata["contact"] = True
    dffinaldata["pressure"] = "NaN"
    df_Frames = dffinaldata

    #df_labeled = df_Frames
    for i,j in dataBHK.items():
            df_Frames[i]= j



    st.dataframe(df_BHK)
    st.dataframe(df_Global)
    st.dataframe(df_Frames)
    #st.dataframe(df_labeled)

    #Create the CSV files and set up the names
    #df_labeled.to_csv('4.Label_Features_'+ user_id + '_.csv')
    df_Frames.to_csv('3.labeled_Features_'+ user_id + '_.csv')
    df_Global.to_csv('2.Metrics_'+user_id+'_.csv')
    df_BHK.to_csv('1.Settings_' + user_id + '_.csv')

    #Optional: concatenate all
    #df_final = pd.concat([df_BHK, df_Global, df_Frames], axis=1)

    #Generate zip file
    zipObj = ZipFile('sample.zip', 'w')
    # Add the CSV files to the zip
    #zipObj.write('4.Label_Features_' + user_id + '_.csv')
    zipObj.write('3.labeled_Features_'+user_id+'_.csv')
    zipObj.write('2.Metrics_'+user_id+'_.csv')
    zipObj.write('1.Settings_'+user_id+'_.csv')
    # close the Zip File
    zipObj.close()

    #button to Dowload the zip file
    with open("sample.zip", "rb") as f:
        bytes = f.read()
    b64 = base64.b64encode(bytes).decode()
    st.markdown('### **⬇️ Download output CSV Files **')
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV Files</a> (right-click and save as ".zip")'
    st.markdown(href, unsafe_allow_html=True)
