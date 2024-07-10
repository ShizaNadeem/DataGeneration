import sys
from qgis.core import (
    QgsApplication, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY,
    QgsProject, QgsVectorLayerUtils, QgsField
)
from qgis.gui import QgsMapCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
import numpy as np

# Step 1: Environment Setup
QgsApplication.setPrefixPath('/usr', True)
app = QApplication(sys.argv)
QgsApplication.initQgis()

# Step 2: Canvas and Layers Setup
canvas = QgsMapCanvas()
canvas.setCanvasColor(Qt.white)

# Path to the shapefiles
pak_map = "D:\\CENTAIC WORK (AI BDA)\\GIS\\2 july\\2 july\\testpyqt\\poc shapefile\\PAK_adm2.shp"
buffer_map = "D:\CENTAIC WORK (AI BDA)\GIS\DataGeneration (10th July)\PointGeneratedonLine\buffer.shp"

# Step 3: Layer Validation
pak_layer = QgsVectorLayer(pak_map, "PAK Layer", "ogr")
if not pak_layer.isValid():
    print("PAK Layer failed to load!")

buffer_layer = QgsVectorLayer(buffer_map, "Buffer Layer", "ogr")
if not buffer_layer.isValid():
    print("Buffer Layer failed to load!")

# Step 4: Temporary Line Layer Creation
line_layer = QgsVectorLayer("LineString?crs=EPSG:4326", "Line Layer", "memory")
provider = line_layer.dataProvider()
provider.addAttributes([QgsField("id", QVariant.Int)])
line_layer.updateFields()

if not line_layer.isValid():
    print("Line Layer failed to create!")

# Step 5: Adding Layers
QgsProject.instance().addMapLayer(pak_layer)
QgsProject.instance().addMapLayer(buffer_layer)
QgsProject.instance().addMapLayer(line_layer)

# Step 6: Layer Opacity Settings
pak_layer.setOpacity(0.8)
buffer_layer.setOpacity(0.8)
line_layer.setOpacity(0.8)

# Step 7: Main Window Configuration
main_window = QMainWindow()
main_window.setCentralWidget(canvas)
main_window.setFixedSize(800, 600)
main_window.show()

# Step 8: Map Canvas Configuration
canvas.setExtent(pak_layer.extent())
canvas.setLayers([pak_layer, buffer_layer, line_layer])

# Step 9: Buffer Point Definition
point = QgsPointXY(77.0, 33.5)  # Example coordinates, change as needed

# Step 10: Angle Definitions
angles = [-120, -150, 120, 150]  # Example angles in degrees

# Step 11: Random Point Generation on Lines
num_points_per_line = 10  # Total number of points to generate per line
points = []
line_layer.startEditing()
point_id = 0

for angle in angles:
    for _ in range(num_points_per_line):
        # Generate a random distance between 0 and 1
        random_distance = np.random.uniform(0, 1)

        # Calculate the endpoint of the line using the angle and random distance
        angle_rad = np.radians(angle)
        end_point = QgsPointXY(
            point.x() + random_distance * np.cos(angle_rad),
            point.y() + random_distance * np.sin(angle_rad)
        )
        points.append((end_point.x(), end_point.y()))

        # Create line feature (optional, for visualization)
        line = QgsGeometry.fromPolylineXY([point, end_point])
        line_feature = QgsFeature(line_layer.fields())
        line_feature.setGeometry(line)
        line_feature.setAttribute("id", point_id)
        line_layer.addFeature(line_feature)
        point_id += 1

# Step 12: Editing and Committing Changes
line_layer.commitChanges()

# Step 13: Save Points to npy File
points_array = np.array(points)
np.save('generated_points.npy', points_array)

# Step 14: Print Points in Terminal
print("Generated Points:")
for pt in points:
    print(pt)

# Step 15: Canvas Refresh
canvas.refresh()

# Step 16: Application Event Loop
sys.exit(app.exec_())