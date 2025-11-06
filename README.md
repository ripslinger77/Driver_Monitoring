# Driver Monitoring System with YOLOv5

## Overview

This repository contains a YOLOv5-based driver monitoring system designed to detect and classify driver states in real-time. The system integrates computer vision with sensor data (GPS, compass, accelerometer) to provide comprehensive driver behavior analysis and distraction detection.

## System Architecture

The project consists of three main components:

1. **Detection Module**: YOLOv5 model for classifying driver states
2. **Sensor Integration**: Real-time data collection from smartphone sensors via ADB
3. **Visualization Pipeline**: Data processing and video generation for analysis

## Features

### Core Functionality

- **Real-time Driver State Classification**
  - Focused
  - Other Distractions
  - Sleepy/Drowsy

- **Sensor Data Integration**
  - GPS coordinates tracking
  - Compass bearing measurements
  - Accelerometer data for motion detection
  - Vehicle turning detection based on bearing changes

- **Data Logging**
  - CSV export of detection results
  - Temporal synchronization with video frames
  - Confidence scores and probability metrics

### Visualization Tools

- Geographic mapping with route visualization
- Bar graph generation for state distribution analysis
- Side-by-side video composition
- Compass bearing overlay on detection results

## Requirements

### Hardware
- CUDA-capable GPU (recommended for real-time inference)
- Android smartphone with ADB debugging enabled
- Camera system (webcam, RealSense, or GoPro)

### Software Dependencies

```
Python >= 3.7
PyTorch >= 1.7.0
torchvision >= 0.8.1
opencv-python >= 4.1.1
numpy >= 1.18.5
pandas >= 1.1.4
pyrealsense2 (for RealSense camera support)
folium (for map generation)
selenium (for map screenshot capture)
moviepy (for video processing)
```

See `requirements.txt` for complete dependency list.

## Usage

### Model Training

Train a custom YOLOv5 model on driver state dataset:

```bash
python train.py --data <dataset.yaml> --weights yolov5s.pt --img 640 --epochs 100
```

### Detection Inference

Run detection on video source:

```bash
python detect.py --weights <best.pt> --source <video_path> --conf-thres 0.25
```

For detection with sensor integration:

```bash
python detect_non.py --weights <best.pt> --source <video_path>
```

### Sensor Data Collection

**GPS Tracking:**
```bash
python modules/disp/phone_gps\ -\ 1+.py
```

**Compass/Bearing:**
```bash
python modules/disp/phone_compass\ -\ 1+.py
```

**Accelerometer:**
```bash
python modules/disp/phone_accelerometer\ -\ 1+.py
```

Note: Requires Android device connected via ADB with appropriate permissions.

### Benchmark Performance

Evaluate model across different export formats:

```bash
python benchmarks.py --weights <model.pt> --img 640
```

### Model Export

Export to various formats for deployment:

```bash
python export.py --weights <model.pt> --include onnx torchscript tflite
```

## Project Structure

```
├── detect.py                 # Standard detection script
├── detect_non.py            # Detection with sensor integration
├── train.py                 # Model training script
├── val.py                   # Validation script
├── export.py                # Model export utilities
├── benchmarks.py            # Performance benchmarking
├── hubconf.py               # PyTorch Hub configuration
├── modules/
│   ├── disp/                # Display and visualization modules
│   │   ├── bar_graph_gen.ipynb
│   │   ├── mapping.ipynb
│   │   ├── side_by_side.py
│   │   ├── image_quality.py
│   │   ├── video_quality.py
│   │   └── video_time.py
│   ├── phone_gps.py         # GPS data acquisition
│   ├── phone_compass.py     # Compass/bearing measurement
│   ├── video_frame.py       # Frame extraction utilities
│   ├── gopro_datetime.py    # GoPro timestamp extraction
│   ├── Gopro_MP4-mkv.py    # GoPro format conversion
│   ├── burn_bearing.py      # Bearing overlay on video
│   ├── gui.py               # GUI utilities
│   ├── something.py         # RealSense integration
│   ├── timestamp_and_compass.py  # Timestamp and compass overlay
│   ├── timestamp_and_gyro.py     # Gyroscope data overlay
│   └── real_time[1].ipynb   # Real-time processing notebook
├── requirements.txt         # Python dependencies
├── setup.cfg               # Configuration file
└── README.md               # This file
```

## Data Format

### Detection Output CSV

The system generates CSV files with the following structure:

```csv
Focused,Other_Distractions,Sleepy,Class,Prob,Bearing,Turning
```

- `Focused`: Cumulative count of focused state detections
- `Other_Distractions`: Count of distraction events
- `Sleepy`: Count of drowsiness detections
- `Class`: Detected class ID (0=Focused, 1=Distracted, 2=Sleepy)
- `Prob`: Detection confidence score
- `Bearing`: Compass bearing in degrees
- `Turning`: Binary flag for turning detection (YES/NO)

### GPS Output CSV

```csv
timestamp,latitude,longitude
```

### Bearing/Compass CSV

```csv
Bearing,Turning
```

## Validation and Testing

Run validation on test dataset:

```bash
python val.py --data <dataset.yaml> --weights <model.pt> --img 640
```

## Model Formats Supported

- PyTorch (.pt)
- TorchScript (.torchscript)
- ONNX (.onnx)
- OpenVINO
- TensorRT (.engine)
- CoreML (.mlmodel)
- TensorFlow (SavedModel, GraphDef, Lite)
- TensorFlow Edge TPU
- TensorFlow.js
- PaddlePaddle

## Configuration

Key parameters can be adjusted in the detection scripts:

- `conf_thres`: Confidence threshold (default: 0.25)
- `iou_thres`: NMS IoU threshold (default: 0.45)
- `max_det`: Maximum detections per image (default: 1000)
- `imgsz`: Input image size (default: 640)
- `device`: Device for inference (cpu, 0, 0,1,2,3)
- `half`: Use FP16 half-precision inference

## Visualization Workflows

### 1. Route Mapping

Generate geographic visualization of driving route:

```bash
jupyter notebook modules/disp/mapping.ipynb
```

### 2. State Distribution Analysis

Create bar graphs showing driver state distribution:

```bash
jupyter notebook modules/disp/bar_graph_gen.ipynb
```

### 3. Multi-view Video Composition

Combine multiple video sources side-by-side:

```bash
python modules/disp/side_by_side.py
```

## ADB Setup for Sensor Integration

1. Enable Developer Options on Android device
2. Enable USB Debugging
3. Connect device via USB
4. Verify connection:
```bash
adb devices
```
5. Grant necessary permissions for location and sensor access

## Development

### Adding New Detection Classes

1. Update dataset YAML with new class names
2. Retrain model with updated dataset
3. Modify class ID mappings in `detect_non.py`

### Custom Sensor Integration

Extend sensor modules by:
1. Creating new module in `modules/` directory
2. Implementing data acquisition function
3. Integrating with main detection loop in `detect_non.py`

## License

GPL-3.0 License (inherited from YOLOv5)

This project is based on YOLOv5 by Ultralytics and inherits its licensing terms.

## Acknowledgments

Based on YOLOv5 by Ultralytics: https://github.com/ultralytics/yolov5

Special thanks to the contributors of the open-source libraries used in this project.

## Citation

If you use this work in your research, please cite:

```bibtex
@software{yolov5_driver_monitoring,
  title = {Driver Monitoring System with YOLOv5},
  year = {2023},
  note = {Based on YOLOv5 by Ultralytics},
  url = {https://github.com/ripslinger77/Driver_Monitoring}
}
```

## References

- Ultralytics YOLOv5: https://github.com/ultralytics/yolov5
- PyTorch: https://pytorch.org/
- OpenCV: https://opencv.org/
- RealSense SDK: https://github.com/IntelRealSense/librealsense

## Future Enhancements

- Real-time alerting system for drowsiness detection
- Multi-camera support for comprehensive cabin monitoring
- Integration with vehicle CAN bus for additional telemetry
- Cloud-based data aggregation and analysis
- Mobile application for standalone deployment
