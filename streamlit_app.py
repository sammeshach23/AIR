import streamlit as st

# Experiment names and their corresponding code files
experiments = {
    "Experiment 1: Sliding Crank": "Sliding Crank.linkage2",
    "Experiment 2: Subscriber & Publisher": "AIR_Publisher_and_Subscriber.ipynb",
    "Experiment 3: Forward 2D": "experiment3_code.py",
    "Experiment 4: Inverse 2D": "experiment4_code.py",
    "Experiment 5: Forward 3D": "experiment5_code.py",
    "Experiment 6: Inverse 3D": "experiment6_code.py",
    "Experiment 7: Four Bar Linkage": "FOUR BAR LINKAGE.linkage2",
    "Experiment 8: Pick and Place": "Pick nd place.linkage2",
    "Experiment 9: SLAM": "SLAM_EXP.txt""SLAM.ipynb",
    "Experiment 10: Analyze torque and force": "experiment11_code.py",
}

# Function to generate a placeholder code file for download
def generate_code_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Generate placeholder files (optional, for demonstration)
for exp_name, filename in experiments.items():
    generate_code_file(filename, f"# Code for {exp_name}\n\nprint('{exp_name} executed!')")

# Streamlit App
st.title("Experiments List")

st.write("Below is the list of experiments. Click on the download button to get the code.")

for exp_name, filename in experiments.items():
    st.subheader(exp_name)
    with open(filename, "r") as file:
        file_content = file.read()
    st.download_button(
        label=f"Download {exp_name} Code",
        data=file_content,
        file_name=filename,
        mime="text/plain",
    )
