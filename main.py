# Import necessary packages
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Terminal Velocity Calculator', page_icon=':helicopter:', layout='centered')

st.title(':helicopter: Terminal Velocity Calculator')
st.subheader(':sparkles: Powered by DL Droni')
st.markdown(
'''
Simple calculator that computes the terminal velocity 
of an object falling in a fluid.

Useful when dealing with UAS risk assessment.
'''
)

st.divider()

# Column division
col_input, col_output = st.columns(2, gap='large')

# Input part
with col_input:
    # st.markdown('Insert the values here.')

    uav_mass = st.number_input(
        label='UAV MTOW (kg)',
        min_value=0.250,
        max_value=150.0,
        value=9.0,
        format='%f',
        help='Insert the maximum take-off mass of the employed UAV, expressed in kg.'
    )
    g = st.number_input(
        label='Gravity acceleration (m/s^2)',
        min_value=0.1,
        max_value=100.0,
        value=9.81,
        format='%f',
        help=r'The g acceleration on Earth is 9.81 m/s^2'
    )
    drag_coeff = st.number_input(
        label='Drag coefficient',
        min_value=0.01,
        max_value=1.0,
        value=0.7,
        format='%f',
        help=r'Typical value: 0.7'
    )
    fluid_density = st.number_input(
        label='Fluid density (kg/m^3)',
        min_value=0.1,
        max_value=100.0,
        value=1.212,
        format='%f',
        help=r'Air typical value is 1.212 kg/m^3'
    )
    uav_side = st.number_input(
        label='Dimension of a main side of the UAV (m)',
        min_value=0.1,
        max_value=20.0,
        value=0.5,
        format='%f',
        help=r'Insert the measure of the side of an hypothetical box that encloses tha whole UAV.'
    )

# Make computations
if st.button('Compute'):
    # Compute UAV area (cross section)
    uav_area = np.power(uav_side, 2)

    # Compute newton
    newton = uav_mass * g

    # Compute terminal velocity
    v_term = np.sqrt((2. * uav_mass * g) / (drag_coeff * fluid_density * uav_area))

    with col_output:
        
        # st.header('Figures of Merit')
        st.metric(
            label='Terminal velocity (m/s)',
            value=round(v_term,5)
        )
        st.divider()
        st.metric(
            label='UAV cross-section area (m^2)',
            value=round(uav_area,5)
        )

st.write(
    """<style>
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Display explanation
if st.toggle(label='Tell me more'):
    # Show math
    st.markdown('---')
    st.header('Mathematical explanation')
    st.markdown(
    '''
    Terminal velocity is the maximum velocity attainable 
    by an object as it falls through a fluid. 
    It occurs when the sum of the drag force and the buoyancy 
    is equal to the downward force of gravity acting on the object. 
    Since the net force on the object is zero, 
    the object has zero acceleration.
    '''
    )
    st.markdown(
    '''
    It can be obtained using the following formula:
    '''
    )
    st.latex(r'''
    V_{t} = \sqrt{\frac{m g}{ \rho D_c A_{cs}}}
    ''')
    st.markdown(
    '''
    where:
     - $V_{t}$ is the terminal velocity,
     - $m$ is the mass of the object,
     - $g$ is the acceleration due to gravity,
     - $\rho$ is the density of the fluid,
     - $D_c$ is the drag coefficient, and
     - $A_{cs}$ is the cross-section area of the object.
    '''
    )