import streamlit as st

# main heading
st.title("unit converter")


#define weight units 
weight_units = {
    "gram": 1,  #base unit
    "kilogram": 0.001,  # 1 gram = 0.001 kilogram
    "pounds": 0.00220462  # 1 gram =  0.00220462 gram
}

#define lenght units
lenght_units ={
    "meter": 1, # base unit
    "kilometer":0.001,  # 1 meter = 0.001 kilometer
    "miles": 0.000621371,  # 1 meter =  0.000621371 miles
    "feet": 3.28084  # 1 meter =  3.28084 feett
}

# dropdown for category weight and lenght units
categories = ["weight units", "lenght units"] 
category = st.selectbox("select a category", categories)

#input field for enter a value for convertion
value = st.number_input("enter a value to convert", min_value=0.0, format="%.2f", step=1.0 )  #value add with 1, use format specifier here to control decimal numbers 

#if slect weight unit all weight units wills show
if category == "weight units":  
    from_units = st.selectbox("convert from", list(weight_units.keys()))
    to_units = st.selectbox("convert into", list(weight_units.keys()))
    units = weight_units

#if select lenght unit al lenght units will show
elif category == "lenght units":
    from_units = st.selectbox("convert from", list(lenght_units.keys()))
    to_units = st.selectbox("convert into", list(lenght_units.keys()))
    units = lenght_units

# by pressing the button the result will display 
if st.button("convert"):
    if from_units and to_units and value:
        result = (value / units[from_units]) * units[to_units]
        st.success(f"{value} {from_units} = {result:.4f} {to_units}")
    else:
     st.error("please enter a value and select units.")
