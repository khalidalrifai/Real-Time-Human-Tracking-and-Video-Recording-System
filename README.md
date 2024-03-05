# Real-Time Human Tracking and Video Recording System

## Overview
The Real-Time Human Tracking and Video Recording System is designed to detect and track human faces or bodies in real-time, recording the video feed for further use. Leveraging computer vision technology, specifically OpenCV, this project allows for the automated monitoring and recording of individuals in various environments, making it ideal for security, research, and interactive installations.

## Features
- **Real-time Detection**: Utilizes OpenCV's pre-trained models for accurate face and body detection.
- **Tracking**: Implements tracking algorithms to follow detected humans across frames, reducing computational load.
- **Video Recording**: Records the tracked video feed in real-time, saving it for future playback or analysis.
- **Customization**: Offers parameters for detection sensitivity, tracking quality, and output video settings.

## Installation

Ensure you have Python installed on your system. This project requires Python 3.6 or newer.

### Dependencies

- OpenCV
- Numpy

Install the required Python packages using pip:

```bash
pip install opencv-python opencv-python-headless numpy
```

## Usage

To start the tracking and recording system, run the main script:

```bash
python track_and_record.py
```

Use `q` to quit the application at any time.

## Configuration

You can adjust various parameters within `track_and_record.py`, including detection sensitivity, tracking algorithm choice, and output video properties.

## Contributing

Contributions to the Real-Time Human Tracking and Video Recording System are welcome. Please ensure to follow the contribution guidelines outlined in `CONTRIBUTING.md`.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgements

- OpenCV contributors and community for providing extensive resources and tools for computer vision applications.
