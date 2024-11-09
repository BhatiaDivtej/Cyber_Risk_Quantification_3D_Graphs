import streamlit as st
import streamlit as st
import numpy as np
import plotly.graph_objects as go


def home():
    st.title("Cyber Risk Quantification")
    st.write(
    "Exploring Likelihood of Breach for Companies through interactive graphing. "
    )
    st.success("Welcome! Please Select the Company Size from the left menu")


def page_one():
    st.title("Micro Company")

    # Micro Company Functions
    def V(T, E, M):
        V1 = -0.2937 * E + 0.2467 * T - 0.0010 * (T**2) + 0.6192 * M
        V2 = -0.2937 * E + 0.12335 * T + 0.6192 * M
        return np.where(T <= 123.35, V1, V2)

    def P(V):
        sig = 1.017 / (1 + np.exp(-0.415 * (V - 10.703)))
        return 0.2 + 0.77 * sig

    # Generate grid data
    grid_size = 100
    T = np.linspace(20, 125, grid_size)  # T range for micro companies
    E = np.linspace(0, 18, grid_size)     # E range for all companies
    M = np.linspace(0, 10, grid_size)     # M range for all companies
    T, E, M = np.meshgrid(T, E, M, indexing='ij')

    # Streamlit app layout
    st.title("Interactive 3D Graph of V, T, E, and M for Micro Company")

    # Dropdown and Slider for variable selection
    variable = st.selectbox("Select Variable:", ['T', 'E', 'M'])
    
    if variable == 'T':
        value = st.slider("Select Temperature (T):", min_value=20.0, max_value=125.0, value=50.0, step=0.1)
    elif variable == 'E':
        value = st.slider("Select Energy (E):", min_value=0.0, max_value=18.0, value=9.0, step=0.1)
    else:  # M
        value = st.slider("Select M:", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

    # Update based on selected variable
    def update_plot(var, val):
        if var == 'T':
            index = np.abs(T[:, 0, 0] - val).argmin()
            v = V(T[index, :, :], E[index, :, :], M[index, :, :])
            x, y = E[index, :, :], M[index, :, :]
            title = f'V(T={val:.2f}, E, M)'
 
        elif var == 'E':
            index = np.abs(E[0, :, 0] - val).argmin()
            v = V(T[:, index, :], E[:, index, :], M[:, index, :])
            x, y = T[:, index, :], M[:, index, :]
            title = f'V(T, E={val:.2f}, M)'

        elif var == 'M':
            index = np.abs(M[0, 0, :] - val).argmin()
            v = V(T[:, :, index], E[:, :, index], M[:, :, index])
            x, y = T[:, :, index], E[:, :, index]
            title = f'V(T, E, M={val:.2f})'

        # Create hover text for each point
        p = P(v) * 100
        hover_text = np.array([f'E: {E_val:.2f}<br>M: {M_val:.2f}<br>V: {v_val:.2f}<br>Likelihood of Breach: {p_val:.2f}%'
                            for E_val, M_val, v_val, p_val in zip(E.flatten(), M.flatten(), v.flatten(), p.flatten())]).reshape(v.shape)

        # Create Plotly figure
        fig = go.Figure()
        colorscale = [
            [0.0, 'darkblue'],
            [0.2, 'blue'],
            [0.5, 'lime'],
            [0.7, 'orange'],
            [1.0, 'red']
        ]

        fig.add_trace(go.Surface(z=v, x=x, y=y, colorscale=colorscale,
                                name='V', showscale=True,
                                hoverinfo='text',
                                text=hover_text))

        fig.update_layout(title='Plot of V, T, E and M and Probability/Likelihood of Breach of a MICRO COMPANY <br>' + title,
                        scene=dict(
            xaxis_title='E' if var == 'T' else 'T',
            yaxis_title='M',
            zaxis_title='V',
        ))

        return fig

    # Update and display the plot
    fig = update_plot(variable, value)
    st.plotly_chart(fig)

import numpy as np
import streamlit as st
import plotly.graph_objects as go

def page_two():
    st.title("Small Company")

    # Small Company Functions
    def V(T, E, M):
        V1 = -1.2994 * E + 0.3368 * T - 0.0004 * (T**2) + 2.8878 * M
        V2 = -1.2994 * E + 0.0193 * T + 2.8878 * M + 62.7695
        return np.where(T <= 421, V1, V2)

    def P(V):
        sig = 1.017 / (1 + np.exp(-0.415 * (V/3.5 - 10.703)))
        return 0.2 + 0.77 * sig

    # Generate grid data
    grid_size = 100
    T = np.linspace(125, 500, grid_size)  # Updated T range for small companies
    E = np.linspace(0, 18, grid_size)      # E range for all companies
    M = np.linspace(0, 10, grid_size)      # M range for all companies
    T, E, M = np.meshgrid(T, E, M, indexing='ij')

    # Streamlit app layout
    st.title("Interactive 3D Graph of V, T, E, and M for Small Company")

    # Dropdown and Slider for variable selection
    variable = st.selectbox("Select Variable:", ['T', 'E', 'M'])
    
    if variable == 'T':
        value = st.slider("Select Temperature (T):", min_value=125.0, max_value=500.0, value=250.0, step=0.1)
    elif variable == 'E':
        value = st.slider("Select Energy (E):", min_value=0.0, max_value=18.0, value=9.0, step=0.1)
    else:  # M
        value = st.slider("Select M:", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

    # Update based on selected variable
    def update_plot(var, val):
        if var == 'T':
            index = np.abs(T[:, 0, 0] - val).argmin()
            v = V(T[index, :, :], E[index, :, :], M[index, :, :])
            x, y = E[index, :, :], M[index, :, :]
            title = f'V(T={val:.2f}, E, M)'
 
        elif var == 'E':
            index = np.abs(E[0, :, 0] - val).argmin()
            v = V(T[:, index, :], E[:, index, :], M[:, index, :])
            x, y = T[:, index, :], M[:, index, :]
            title = f'V(T, E={val:.2f}, M)'

        elif var == 'M':
            index = np.abs(M[0, 0, :] - val).argmin()
            v = V(T[:, :, index], E[:, :, index], M[:, :, index])
            x, y = T[:, :, index], E[:, :, index]
            title = f'V(T, E, M={val:.2f})'

        # Create hover text for each point
        p = P(v) * 100
        hover_text = np.array([f'E: {E_val:.2f}<br>M: {M_val:.2f}<br>V: {v_val:.2f}<br>Likelihood of Breach: {p_val:.2f}%'
                            for E_val, M_val, v_val, p_val in zip(E.flatten(), M.flatten(), v.flatten(), p.flatten())]).reshape(v.shape)

        # Create Plotly figure
        fig = go.Figure()
        colorscale = [
            [0.0, 'darkblue'],
            [0.2, 'blue'],
            [0.5, 'lime'],
            [0.7, 'orange'],
            [1.0, 'red']
        ]

        fig.add_trace(go.Surface(z=v, x=x, y=y, colorscale=colorscale,
                                name='V', showscale=True,
                                hoverinfo='text',
                                text=hover_text))

        fig.update_layout(title='Plot of V, T, E and M and Probability/Likelihood of Breach of a SMALL COMPANY <br>' + title,
                        scene=dict(
            xaxis_title='E' if var == 'T' else 'T',
            yaxis_title='M',
            zaxis_title='V',
        ))

        return fig

    # Update and display the plot
    fig = update_plot(variable, value)
    st.plotly_chart(fig)


import numpy as np
import streamlit as st
import plotly.graph_objects as go

def page_three():
    st.title("Medium Company")

    # Medium Company Functions
    def V(T, E, M):
        V1 = -16.7507 * E + 0.701 * T - 0.0002 * (T**2) + 32.5225 * M
        V2 = -16.7507 * E + 0.31222 * T + 32.5225 * M + 67.08712
        return np.where(T <= 1752.5, V1, V2)

    def P(V):
        sig = 1.017 / (1 + np.exp(-0.415 * (V / 20 - 10.703)))
        return 0.2 + 0.77 * sig

    # Generate grid data
    grid_size = 100
    T = np.linspace(500, 2000, grid_size)  # Updated T range for medium companies
    E = np.linspace(0, 18, grid_size)      # E range for all companies
    M = np.linspace(0, 10, grid_size)      # M range for all companies
    T, E, M = np.meshgrid(T, E, M, indexing='ij')

    # Streamlit app layout
    st.title("Interactive 3D Graph of V, T, E, and M for Medium Company")

    # Dropdown and Slider for variable selection
    variable = st.selectbox("Select Variable:", ['T', 'E', 'M'])
    
    if variable == 'T':
        value = st.slider("Select Temperature (T):", min_value=500.0, max_value=2000.0, value=1000.0, step=0.1)
    elif variable == 'E':
        value = st.slider("Select Energy (E):", min_value=0.0, max_value=18.0, value=9.0, step=0.1)
    else:  # M
        value = st.slider("Select M:", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

    # Update based on selected variable
    def update_plot(var, val):
        if var == 'T':
            index = np.abs(T[:, 0, 0] - val).argmin()
            v = V(T[index, :, :], E[index, :, :], M[index, :, :])
            x, y = E[index, :, :], M[index, :, :]
            title = f'V(T={val:.2f}, E, M)'
 
        elif var == 'E':
            index = np.abs(E[0, :, 0] - val).argmin()
            v = V(T[:, index, :], E[:, index, :], M[:, index, :])
            x, y = T[:, index, :], M[:, index, :]
            title = f'V(T, E={val:.2f}, M)'

        elif var == 'M':
            index = np.abs(M[0, 0, :] - val).argmin()
            v = V(T[:, :, index], E[:, :, index], M[:, :, index])
            x, y = T[:, :, index], E[:, :, index]
            title = f'V(T, E, M={val:.2f})'

        # Create hover text for each point
        p = P(v) * 100
        hover_text = np.array([f'E: {E_val:.2f}<br>M: {M_val:.2f}<br>V: {v_val:.2f}<br>Likelihood of Breach: {p_val:.2f}%'
                            for E_val, M_val, v_val, p_val in zip(E.flatten(), M.flatten(), v.flatten(), p.flatten())]).reshape(v.shape)

        # Create Plotly figure
        fig = go.Figure()
        colorscale = [
            [0.0, 'darkblue'],
            [0.2, 'blue'],
            [0.5, 'lime'],
            [0.7, 'orange'],
            [1.0, 'red']
        ]

        fig.add_trace(go.Surface(z=v, x=x, y=y, colorscale=colorscale,
                                name='V', showscale=True,
                                hoverinfo='text',
                                text=hover_text))

        fig.update_layout(title='Plot of V, T, E and M and Probability/Likelihood of Breach of a MEDIUM COMPANY <br>' + title,
                        scene=dict(
            xaxis_title='E' if var == 'T' else 'T',
            yaxis_title='M',
            zaxis_title='V',
        ))

        return fig

    # Update and display the plot
    fig = update_plot(variable, value)
    st.plotly_chart(fig)



# Create a dictionary to map page names to functions
pages = {
    "Welcome": home,
    "Micro Company": page_one,
    "Small Company": page_two,
    "Medium Company": page_three
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the selected page function
pages[selection]()
