import numpy as np
import pandas as pd
import streamlit as st
 

a=np.array([1,2])
b=pd.DataFrame(a)
st.write(b)

re=st.checkbox("RED")
if re:
    st.info('red')
else:
    st.info('not')
