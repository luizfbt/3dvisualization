# 3dvisualization
Tests for Python packages used for 3D visualization

## Development Environment Installation

1. Install **Python 3.11** (must be 3.11, for *open3d* package) from the [official website](https://www.python.org/)
2. From VS Code, inside the project, enter the terminal prompt.
3. Create the `venv` virtual environment:
    ```
    python -m venv venv
    ```
4. Activate the created environment:
    ```
    venv\Scripts\activate.bat
    ```
5. Run the script to install the packages:
    ```
    install_packages.bat
    ```

6. Installing the Flutter SDK: [flutter.dev website](https://docs.flutter.dev/get-started/install)

## PyVista
* [PyVista — PyVista documentation](https://docs.pyvista.org/)
* [pyvista/pyvista: 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK)](https://github.com/pyvista/pyvista)
* [pyvista/pyvista-tutorial: PyVista SciPy 2022-2024 Tutorial](https://github.com/pyvista/pyvista-tutorial)

## pyntcloud
* [daavoo/pyntcloud: pyntcloud is a Python library for working with 3D point clouds.](https://github.com/daavoo/pyntcloud)

## Folder `demos`: Code samples from the GitHub repositories
* &#x1F5C1; **pyvista_examples**: [pyvista/examples at main · pyvista/pyvista](https://github.com/pyvista/pyvista/tree/main/examples)
* &#x1F5C1; **pyvista_trame**: [pyvista/examples_trame at main · pyvista/pyvista](https://github.com/pyvista/pyvista/tree/main/examples_trame)
* &#x1F5C1; **pyvista_tutorial**: [pyvista-tutorial/tutorial at main · pyvista/pyvista-tutorial](https://github.com/pyvista/pyvista-tutorial/tree/main/tutorial)

## To run the main script
```
In the terminal:

flet run main.py
or
python main.py

Some scripts take time to launch.
Perhaps errors occur or some dependencies are missing.
```
