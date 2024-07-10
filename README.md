# Data Generation
#### QGIS Spatial Data Processing Project
This project demonstrates spatial data processing and visualization using QGIS and PyQt5. The project involves:
1. **Environment Setup:**
   - Setting up the QGIS environment and initializing necessary components.

2. **Canvas and Layers Setup:**
   - Creating a map canvas and loading vector layers from shapefiles.

3. **Temporary Line Layer Creation:**
   - Creating a temporary line layer for visualizing generated lines.

4. **Adding Layers:**
   - Adding loaded vector layers (e.g., administrative boundaries, buffer zones, generated lines) to the QGIS project.

5. **Layer Opacity Settings:**
   - Adjusting the opacity of layers for better visualization.

6. **Main Window Configuration:**
   - Configuring the main application window to display the map canvas.

7. **Map Canvas Configuration:**
   - Setting the extent and layers to be displayed on the map canvas.

8. **Random Point Generation on Lines:**
   - Generating random points along predefined lines starting from specified points and at various angles.

9. **Editing and Committing Changes:**
   - Editing the line layer to add generated features and committing changes.

10. **Saving Points to npy File:**
    - Saving generated points as a numpy array file (`generated_points.npy`).

11. **Terminal Output:**
    - Printing the generated points to the terminal for verification.

12. **Canvas Refresh:**
    - Refreshing the map canvas to reflect all changes made.

13. **Application Event Loop:**
    - Running the PyQt application event loop to handle user interactions.

#### Usage Instructions:
To run the project:
- Ensure QGIS is properly installed and configured.
- Install PyQt5 and numpy dependencies.
- Adjust paths to shapefiles (`pak_map`, `buffer_map`) and starting points (`starting_points`) as per your data requirements.
- Execute the script to visualize and process spatial data.
