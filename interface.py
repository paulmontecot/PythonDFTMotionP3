import streamlit as st
import pandas as pd
import base64
import MathUtilities
import getFeaturesWindows
import emoji

#app

st.title("Features Extraction Interface")
st.write("Fill the differents items then click on generate")

user_id = st.text_input("User ID")
datatype = st.sidebar.selectbox("datatype",('accX','accY','accZ'))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    dataframe.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
    st.write(dataframe)
    Data = dataframe[datatype]
    dataframe['norme'] = MathUtilities.norme(dataframe)
    norme = dataframe['norme']
    Xfinaldata, Yfinaldata = getFeaturesWindows.getFeaturesWindows(Data, 1)
    dffinaldata = pd.DataFrame(Xfinaldata)
    #dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation','contact','pressure']
    dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation']

BHK_score = st.text_input("BHK Score")

handed = st.selectbox(
'Left handed or Right handed',
('Left Handed', 'Right Handed'))

constraint = st.selectbox("level of constraint",('1','2','3','4','5','6','7','8','9','10'))

finger = st.checkbox("finger")
wrist = st.checkbox("wrist")
elbow = st.checkbox("elbow")
shoulder = st.checkbox("shoulder")

int_val = st.number_input('Frame Resolution', min_value=1, max_value=10, value=5, step=1)

def get_dataBHK():
    return[]
def get_dataglobal():
    return[]
mean = dffinaldata.mean(axis=1)
median = dffinaldata.median(axis=1)
standard_deviation = dffinaldata.std(axis=1)
variance = dffinaldata.var(axis=1)
df_BHK = pd.DataFrame()
df_Global = pd.DataFrame()

if finger == False:
    finger = "\U0001F534"
elif finger == True:
    finger = "\U0001F7E2"

if wrist == False:
    wrist = "\U0001F534"
elif wrist == True:
    wirst = "\U0001F7E2"

if elbow == False:
    elbow = "\U0001F534"
elif elbow == True:
    elbow = "\U0001F7E2"

if shoulder == False:
    shoulder = "\U0001F534"
elif shoulder == True:
    shoulder = "\U0001F7E2"

if st.button('GENERATE'):
    dataBHK = {"BHK score": BHK_score, "handedness": handed, "Constraint": constraint,"finger": finger, "wrist":wrist,"elbow":elbow,"shoulder":shoulder}
    dataglobal = {"Mean": mean, "Median": median, "standard deviation": standard_deviation, "variance": variance}
    df_BHK = pd.DataFrame.from_records([dataBHK])
    df_Global = pd.DataFrame.from_records(dataglobal)
    df_Frames = dffinaldata

    st.dataframe(df_BHK)
    st.dataframe(df_Global)
    st.dataframe(df_Frames)



    df_final = pd.concat([df_BHK, df_Global, df_Frames], axis=0)

if st.button('Download'):
    csv = dffinaldata.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown('### **⬇️ Download output CSV File **')
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as ".csv")'
    st.markdown(href, unsafe_allow_html=True)
