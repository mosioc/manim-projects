# Manim Community Personal Projects

A collection of mathematical animations and visualizations created using Manim Community Edition.  


[![demo](https://raw.githubusercontent.com/mosioc/manim-projects/main/EnhancedIrisAnimation.png)](https://raw.githubusercontent.com/mosioc/manim-projects/main/EnhancedIrisAnimation.mp4)

## Overview

This repository contains various animations and mathematical visualizations created using Manim Community Edition. The projects range from basic animations to complex mathematical concepts, including:

- Eye and Iris Animations
- 3D Camera Effects
- Mathematical Transformations
- Abstract Wallpapers
- Various Mathematical Concepts

## Project Structure

```
.
├── animations/
│   ├── eye/           # Eye and iris-related animations
│   │   ├── human-eye.py      # Basic human eye animation
│   │   ├── human-eye2.py     # Advanced eye animation with blinking
│   │   ├── human-eye3.py     # Eye animation with iris movement
│   │   ├── Iris.py           # Iris animation with color changes
│   │   ├── iris2.py          # Advanced iris patterns
│   │   ├── eyeExp.py         # Eye expressions and emotions
│   │   └── Heterochromia.py  # Different colored irises
│   ├── 3d/            # 3D and camera effect animations
│   │   ├── threeDCamera.py           # Basic 3D camera setup
│   │   ├── ThreeDCameraIllusionRotation.py  # Camera rotation effects
│   │   └── MovingZoomedSceneAround.py       # Dynamic camera movements
│   ├── math/          # Mathematical concept animations
│   │   ├── Fourier.py        # Fourier transform visualization
│   │   ├── ft.py             # Basic Fourier transform
│   │   ├── ft3d.py           # 3D Fourier transform
│   │   ├── PiTransfer.py     # Pi-related animations
│   │   ├── Morse.py          # Morse code visualization
│   │   └── MultMod100.py     # Modular arithmetic
│   └── abstract/      # Abstract and artistic animations
│       ├── abstract-wallpaper.py  # Abstract pattern generation
│       ├── mcescher.py           # Escher-style patterns
│       └── ttt.py                # Tic-tac-toe animation
├── utils/             # Utility functions and common components
│   ├── scenes.py      # Common scene implementations
│   ├── mobjects.py    # Custom Manim objects
│   ├── functions.py   # Mathematical functions
│   └── graph.py       # Graph utilities
└── svg/               # SVG assets for animations
```

## Code Guides

### Eye Animations (`animations/eye/`)

The eye animations demonstrate various aspects of human eye visualization:

1. Basic Eye Animation (`human-eye.py`):
```python
class HumanEyeScene(Scene):
    def construct(self):
        # Create basic eye shape
        eye = Circle(radius=2, color=WHITE)
        iris = Circle(radius=1, color=BLUE)
        pupil = Circle(radius=0.5, color=BLACK)
        
        # Add to scene
        self.play(Create(eye))
        self.play(Create(iris))
        self.play(Create(pupil))
```

2. Advanced Eye Animation (`human-eye2.py`):
- Includes blinking mechanism
- Realistic iris patterns
- Dynamic pupil dilation

3. Iris Animations (`Iris.py`, `iris2.py`):
- Color gradient effects
- Pattern generation
- Dynamic color transitions

### 3D Camera Effects (`animations/3d/`)

These animations showcase various 3D camera techniques:

1. Basic 3D Setup (`threeDCamera.py`):
```python
class ThreeDScene(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create 3D object
        cube = Cube()
        self.play(Create(cube))
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
```

2. Camera Illusions (`ThreeDCameraIllusionRotation.py`):
- Perspective tricks
- Optical illusions
- Dynamic camera movements

### Mathematical Concepts (`animations/math/`)

Mathematical visualizations and animations:

1. Fourier Transform (`Fourier.py`):
```python
class FourierTransform(Scene):
    def construct(self):
        # Create function to transform
        func = FunctionGraph(
            lambda x: np.sin(x),
            x_range=[-4, 4],
            color=YELLOW
        )
        
        # Show transformation
        self.play(Create(func))
        self.play(
            func.animate.apply_complex_function(
                lambda x: np.exp(2j * PI * x)
            )
        )
```

2. Modular Arithmetic (`MultMod100.py`):
- Number theory visualizations
- Pattern recognition
- Mathematical sequences

### Abstract Animations (`animations/abstract/`)

Creative and artistic animations:

1. Abstract Wallpaper (`abstract-wallpaper.py`):
```python
class AbstractPattern(Scene):
    def construct(self):
        # Create repeating pattern
        pattern = VGroup()
        for i in range(5):
            for j in range(5):
                square = Square(side_length=1)
                square.move_to([i*2, j*2, 0])
                pattern.add(square)
        
        # Animate pattern
        self.play(Create(pattern))
        self.play(
            pattern.animate.arrange_in_grid(5, 5),
            run_time=2
        )
```

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Manim Community Edition
- Required Python packages (see `requirements.txt`)

### Python Interpreter Setup

Manim requires a specific Python environment setup to work correctly. Here's how to set it up:

#### Using Virtual Environment (Recommended)

1. Create a virtual environment:
```bash
# Windows
python -m venv manim-env
.\manim-env\Scripts\activate

# macOS/Linux
python3 -m venv manim-env
source manim-env/bin/activate
```

2. Install Manim and dependencies:
```bash
pip install manim
pip install -r requirements.txt
```

3. Verify installation:
```bash
manim --version
```

#### Using Conda Environment

1. Create a conda environment:
```bash
conda create -n manim-env python=3.9
conda activate manim-env
```

2. Install Manim and dependencies:
```bash
pip install manim
pip install -r requirements.txt
```

#### IDE Configuration

If you're using an IDE like VS Code or PyCharm:

1. **VS Code**:
   - Open Command Palette (Ctrl+Shift+P)
   - Select "Python: Select Interpreter"
   - Choose the interpreter from your manim-env

2. **PyCharm**:
   - Go to File → Settings → Project → Python Interpreter
   - Click the gear icon → Add
   - Select "Existing Environment" and point to your virtual environment

#### Troubleshooting Common Issues

- **ImportError: No module named 'manim'**: Make sure you've activated the correct virtual environment
- **FFmpeg not found**: Install FFmpeg separately:
  ```bash
  # Windows (using Chocolatey)
  choco install ffmpeg

  # macOS
  brew install ffmpeg

  # Linux
  sudo apt-get install ffmpeg
  ```
- **LaTeX errors**: Install a LaTeX distribution:
  ```bash
  # Windows: Install MiKTeX
  # macOS: Install MacTeX
  # Linux
  sudo apt-get install texlive-full
  ```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/mosioc/manim-projects.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Animations

To run any animation, use the following command:
```bash
manim -pql animations/[category]/[filename].py [SceneName]
```

For example:
```bash
# Run basic eye animation
manim -pql animations/eye/human-eye.py HumanEyeScene

# Run 3D camera effect
manim -pql animations/3d/threeDCamera.py ThreeDScene

# Run Fourier transform
manim -pql animations/math/Fourier.py FourierTransform
```

### Common Parameters

- `-p`: Preview the animation
- `-q`: Quality (l=low, m=medium, h=high)
- `-l`: Use a lower quality (faster rendering)
- `-o`: Output file name
- `--write_to_movie`: Save as video file

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch for your feature
3. Submitting a pull request

## Acknowledgments

- Manim Community Edition team
- 3Blue1Brown for inspiration
- The Manim community for support and resources

## Contact

For questions or suggestions, please open an issue in the repository.
