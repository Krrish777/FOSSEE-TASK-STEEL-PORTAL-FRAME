# Steel Portal Frame Design Project

## Description
This project is a Python-based application for designing a steel portal frame. It utilizes the **PySide6** framework for creating the graphical user interface (GUI) and **OCC (OpenCASCADE)** for 3D modeling. Users can input the dimensions of the frame components, and the program generates a 3D model that can be visualized and saved to a STEP file for further analysis.

## Features
- Create customizable 3D models of a steel portal frame.
- Interactive GUI for user input (dimensions of columns, rafters, purlins, etc.).
- Export the generated model to a STEP file format.
- Easily extendable for future features like frame comparison and optimization.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/steel-portal-frame.git
    ```

2. **Create and activate a Conda environment**:
    ```bash
    conda create --name portalframe python=3.x
    conda activate portalframe
    ```

3. **Install dependencies**:
    Use the `environment.yml` file to install all the necessary dependencies:
    ```bash
    conda env update --file environment.yml --prune
    ```

## Usage

Once the environment is set up and dependencies are installed, you can run the application:

1. Navigate to the project directory:
    ```bash
    cd steel-portal-frame
    ```

2. Run the main Python application:
    ```bash
    python main.py
    ```

3. The GUI will open, where you can input the dimensions of the steel frame, and the 3D model will be generated. You can also save the model as a STEP file.

## Prerequisites
- **Python 3.6 to 3.10**
- **Conda** (for managing the environment)
- **PySide6** (for the GUI)
- **OCC (OpenCASCADE)** (for 3D modeling)
- **STEP file export** for saving models.

## Code Structure

- `main.py`: Initializes the application and connects the GUI with the 3D model generation.
- `geometry.py`: Contains the logic to create the steel portal frame (I-sections, purlins, etc.).
- `gui.py`: Defines the user interface with input fields for the frame dimensions.
- `file_operations.py`: Saves the 3D model to a STEP file.
- `environment.yml`: Lists all the dependencies needed to run the project.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions can include:
- Bug fixes
- New features
- Performance improvements

## Future Work

- **Comparison**: Ability to compare different steel portal frame designs based on cost and material usage.
- **Optimization**: Enhance the design for better material efficiency or manufacturing processes.
