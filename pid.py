import streamlit as st
import numpy as np
import math

def solar_energy_control(Kp, Ki, Kd, setpoint, solar_energy_production, solar_irradiance, dt):
    # Initialize errors
    error = setpoint - solar_energy_production
    integral = 0
    derivative = 0
    
    # Initialize previous errors
    prev_error = error
    prev_time = time.time()
    
    while True:
        # Calculate current error
        error = setpoint - solar_energy_production
        
        # Update integral error
        integral += error * dt
        
        # Calculate derivative error
        derivative = (error - prev_error) / (time.time() - prev_time)
        
        # Calculate control output
        control_output = Kp * error + Ki * integral + Kd * derivative
        
        # Update previous errors
        prev_error = error
        prev_time = time.time()
        
        # Modify control output based on solar irradiance
        control_output *= solar_irradiance / 100
        
        # Adjust solar energy production based on control output
        solar_energy_production += control_output
        
        yield solar_energy_production

# Set default control parameters
Kp = 0.5
Ki = 0.1
Kd = 0.1
setpoint = 100
solar_energy_production = 50
solar_irradiance = 70
dt = 0.01

# Create sliders for control parameters
Kp_slider = st.slider("Proportional gain (Kp)", 0.0, 1.0, Kp)
Ki_slider = st.slider("Integral gain (Ki)", 0.0, 1.0, Ki)
Kd_slider = st.slider("Derivative gain (Kd)", 0.0, 1.0, Kd)
setpoint_slider = st.slider("Setpoint", 0, 200, setpoint)
solar_irradiance_slider = st.slider("Solar irradiance", 0, 100, solar_irradiance)

# Update control parameters based on slider values
Kp = Kp_slider
Ki = Ki_slider
Kd = Kd_slider
setpoint = setpoint_slider
solar_irradiance = solar_irradiance_slider

# Run control algorithm and update solar energy production
for energy in solar_energy_control(Kp, Ki, Kd, setpoint, solar_energy_production, solar_irradiance, dt):
    solar_energy_production = energy
    
    # Display current solar energy production
    st.write(f"Current solar energy production: {solar_energy_production:.2f}")
