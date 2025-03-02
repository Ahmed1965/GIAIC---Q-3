import streamlit as st
import os

def convert_length(value, from_unit, to_unit):
    # Conversion to meters first
    meters = {
        "Meters": value,
        "Kilometers": value * 1000,
        "Miles": value * 1609.34,
        "Feet": value * 0.3048,
        "Inches": value * 0.0254
    }[from_unit]
    
    # Convert from meters to target unit
    return {
        "Meters": meters,
        "Kilometers": meters / 1000,
        "Miles": meters / 1609.34,
        "Feet": meters / 0.3048,
        "Inches": meters / 0.0254
    }[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion to kilograms first
    kg = {
        "Kilograms": value,
        "Grams": value / 1000,
        "Pounds": value * 0.453592,
        "Ounces": value * 0.0283495
    }[from_unit]
    
    return {
        "Kilograms": kg,
        "Grams": kg * 1000,
        "Pounds": kg / 0.453592,
        "Ounces": kg / 0.0283495
    }[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    celsius = {
        "Celsius": value,
        "Fahrenheit": (value - 32) * 5/9,
        "Kelvin": value - 273.15
    }[from_unit]
    
    return {
        "Celsius": celsius,
        "Fahrenheit": (celsius * 9/5) + 32,
        "Kelvin": celsius + 273.15
    }[to_unit]

def convert_time(value, from_unit, to_unit):
    # Convert to seconds first
    seconds = {
        "Seconds": value,
        "Minutes": value * 60,
        "Hours": value * 3600,
        "Days": value * 86400
    }[from_unit]
    
    return {
        "Seconds": seconds,
        "Minutes": seconds / 60,
        "Hours": seconds / 3600,
        "Days": seconds / 86400
    }[to_unit]

def convert_area(value, from_unit, to_unit):
    # Convert to square meters first
    sq_meters = {
        "Square Meters": value,
        "Square Kilometers": value * 1000000,
        "Square Miles": value * 2589988.11,
        "Square Feet": value * 0.092903,
        "Acres": value * 4046.86
    }[from_unit]
    
    return {
        "Square Meters": sq_meters,
        "Square Kilometers": sq_meters / 1000000,
        "Square Miles": sq_meters / 2589988.11,
        "Square Feet": sq_meters / 0.092903,
        "Acres": sq_meters / 4046.86
    }[to_unit]

def convert_volume(value, from_unit, to_unit):
    # Convert to cubic meters first
    cubic_meters = {
        "Cubic Meters": value,
        "Liters": value / 1000,
        "Gallons": value / 264.172,
        "Cubic Feet": value / 35.3147,
        "Milliliters": value / 1000000
    }[from_unit]
    
    return {
        "Cubic Meters": cubic_meters,
        "Liters": cubic_meters * 1000,
        "Gallons": cubic_meters * 264.172,
        "Cubic Feet": cubic_meters * 35.3147,
        "Milliliters": cubic_meters * 1000000
    }[to_unit]

st.set_page_config(
    page_title="Unit Conversion",
    page_icon="🔄",
    layout="centered"
)

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(current_dir, 'styles.css')

# Read and apply CSS
with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write('<h1 class="heading">Unit Conversion</h1>', unsafe_allow_html=True)

# Create tabs for different conversion types
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Length Conversion", 
    "Weight Conversion",
    "Temperature Conversion",
    "Time Conversion",
    "Area Conversion",
    "Volume Conversion"
])

with tab1:
    st.header("Length Conversion")
    input_value = st.number_input("Enter Length:", min_value=0.0, step=0.01, key="length_input")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"], key="length_from")
    with col2:
        to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"], key="length_to")
    if st.button("Convert Length", key="convert_length"):
        result = convert_length(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")

with tab2:
    st.header("Weight Conversion")
    input_value = st.number_input("Enter Weight:", min_value=0.0, step=0.01, key="weight_input")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"], key="weight_from")
    with col2:
        to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"], key="weight_to")
    if st.button("Convert Weight", key="convert_weight"):
        result = convert_weight(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")

with tab3:
    st.header("Temperature Conversion")
    input_value = st.number_input("Enter Temperature:", step=0.1, key="temp_input")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    with col2:
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    if st.button("Convert Temperature", key="convert_temp"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")

with tab4:
    st.header("Time Conversion")
    input_value = st.number_input("Enter Time:", min_value=0.0, step=0.01, key="time_input")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Seconds", "Minutes", "Hours", "Days"], key="time_from")
    with col2:
        to_unit = st.selectbox("To:", ["Seconds", "Minutes", "Hours", "Days"], key="time_to")
    if st.button("Convert Time", key="convert_time"):
        result = convert_time(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")

with tab5:
    st.header("Area Conversion")
    input_value = st.number_input("Enter Area:", min_value=0.0, step=0.01, key="area_input")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Square Meters", "Square Kilometers", "Square Miles", "Square Feet", "Acres"], key="area_from")
    with col2:
        to_unit = st.selectbox("To:", ["Square Meters", "Square Kilometers", "Square Miles", "Square Feet", "Acres"], key="area_to")
    if st.button("Convert Area", key="convert_area"):
        result = convert_area(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")

with tab6:
    st.header("Volume Conversion")
    input_value = st.number_input("Enter Volume:", min_value=0.0, step=0.01, key="volume_input")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Cubic Meters", "Liters", "Gallons", "Cubic Feet", "Milliliters"], key="volume_from")
    with col2:
        to_unit = st.selectbox("To:", ["Cubic Meters", "Liters", "Gallons", "Cubic Feet", "Milliliters"], key="volume_to")
    if st.button("Convert Volume", key="convert_volume"):
        result = convert_volume(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
    