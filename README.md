# Sales Prediction with Linear Regression and 3D Visualization

This Python script uses linear regression to predict sales based on advertising data and provides 3D visualizations to understand the relationships between advertising channels (TV and radio) and sales.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Features

- Predicts sales based on advertising data.
- Uses linear regression for prediction.
- Visualizes the relationships between TV, radio, and sales in 3D.
- Provides data exploration and summary statistics.

## Getting Started

### Prerequisites

To run this code, you will need:

- Python 3.x installed on your computer.
- The following Python libraries: `pandas`, `seaborn`, `matplotlib`, `numpy`, `scikit-learn`, `statsmodels`.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/sales-prediction-3d-visualization.git
   ```

2. Change into the project directory:

   ```bash
   cd sales-prediction-3d-visualization
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required libraries:

   ```bash
   pip install pandas seaborn matplotlib numpy scikit-learn statsmodels
   ```

## Usage

1. Make sure you've followed the installation steps above.

2. Ensure that you have the data file (`Advertising.csv`) in the same directory as the script.

3. Run the script:

   ```bash
   python sales_prediction_3d_visualization.py
   ```

4. The script will perform linear regression to predict sales based on TV and radio advertising data and provide 3D visualizations to explore the relationships between these variables.

## Code Explanation

The code is organized into sections for data exploration, linear regression modeling, and 3D visualization. Detailed comments are provided within the code to help you understand each step.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
