
INSTRUCTIONS:
1. Place folder "chalmers_thesis" into C directory
2. Donwload and install mmWaveVisualizer from "https://dev.ti.com/gallery/info/mmwave/mmWave_Demo_Visualizer//" or from "https://github.com/ruslanmasinjila/mmWaveVisualizer"
3. Replace mmWave.js found in "guicomposer\runtime\gcruntime.v7\mmWave_Demo_Visualizer\app" with the one found in "C:\chalmers_thesis\mmWave_template"
4. Import and activate anaconda environment found in "C:\chalmers_thesis\anaconda_environment" 
5. Launch GUI found in "C:\chalmers_thesis\JAVA_GUI\dist"
6. Press "Launch Server" on Java GUI
7. Run mmWave Visualizer
8. Select Geture to record from the dropdown menu of the JAVA GUI
9. Click on "START CAPTURE" to start saving frames into C:\chalmers_thesis\data
10.Click on "STOP CAPTURE" to stop saving frames
---------------
Current Status
---------------
Version 1.1 [Complete]
- JAVA GUI Launches 2 python servers, 1 mmWaveVisualizer Client, and One Java client
- One of the python servers receives range-doppler heatmaps from mmWaveVisualizer Client and saves data.
- The other python server receives commands from Java Client
- Preprocessing of captured frames into 128x128 features standardized to [0,1]
- Training data can be found at https://drive.google.com/drive/folders/1Fl0gFXouDYUSRcVearLVbsP_qxscS_Y1?usp=sharing

----------------------------------------