# Data Science using Python LAB 🐍📊

Welcome to the Data Science using Python Laboratory repository! This repository contains practical experiments and implementations covering various aspects of data science, data analysis, and visualization using Python.

## 📋 Table of Contents

- [About](#about)
- [Experiments](#experiments)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [Author](#author)

## 📖 About

This repository contains hands-on laboratory experiments for the Data Science using Python course. Each experiment focuses on different concepts and techniques in data science, including data manipulation, analysis, visualization, and machine learning fundamentals.

The experiments use the **Aadhar Enrollment Dataset** as a common dataset to demonstrate various data science operations and techniques.

## 🧪 Experiments

### Experiment 1: Data Analysis Fundamentals
**📁 Folder:** `EXP1/`

**Topics Covered:**
- Reading data from Excel files using Pandas
- Understanding DataFrame structure and shape
- Generating descriptive statistics
- Dataset information and data types
- Identifying and handling missing values
- Data imputation using mean values

**Key Files:**
- `EXP1.py` - Main implementation
- `demo.py` - Demo script
- `Sample_Aadhar_Enrollment_Dataset.xlsx` - Dataset

**Learning Outcomes:**
- Load and inspect datasets
- Understand basic data properties
- Handle missing data effectively

---

### Experiment 2: Data Visualization
**📁 Folder:** `EXP2/`

**Topics Covered:**
- Creating bar charts with Matplotlib
- Grouped bar charts for multiple categories
- Box plots for distribution analysis
- Statistical visualizations
- Saving plots as image files
- Data-driven storytelling through visualizations

**Key Files:**
- `EXP2.py` - Main implementation
- `DOC.ipynb` - Jupyter Notebook with visualizations
- `demo.py` - Demo script
- `Image/` - Generated visualization images
  - `bar_charts_by_state.png`
  - `box_plots_distribution.png`
  - `box_plot_overall_analysis.png`
  - `top_10_districts_bar_chart.png`

**Learning Outcomes:**
- Create various types of charts and plots
- Visualize data distributions
- Compare categorical data
- Export visualizations for reports

---

### Experiment 3: Exploring Pandas Library
**📁 Folder:** `EXP3/`

**Topics Covered:**
- Data I/O operations (CSV, Excel)
- DataFrame manipulation and operations
- Data selection and filtering
- Sorting and grouping data
- Statistical operations
- Data aggregation and transformation
- Advanced Pandas functions

**Key Files:**
- `EXP3.py` - Main implementation
- `Aadhar_Enrollment_Data.csv` - CSV output
- `Aadhar_Enrollment_Output.xlsx` - Processed Excel output
- `Sample_Aadhar_Enrollment_Dataset.xlsx` - Input dataset

**Learning Outcomes:**
- Master Pandas DataFrame operations
- Perform data transformations
- Apply statistical functions
- Export data in various formats

---

### 🔜 Future Experiments

This repository will be updated with more experiments covering:
- Machine Learning Algorithms
- Statistical Analysis
- Data Preprocessing Techniques
- Feature Engineering
- Model Evaluation
- And more...

## 🛠️ Technologies Used

- **Python 3.x** - Programming Language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Jupyter Notebook** - Interactive computing
- **openpyxl** - Excel file operations

## 🚀 Getting Started

### Prerequisites

Before running the experiments, ensure you have:

- Python 3.7 or higher installed
- pip (Python package manager)
- Basic understanding of Python programming
- Familiarity with data structures

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prem-Hanchate/Data-Science-using-Python-LAB-.git
   cd Data-Science-using-Python-LAB-
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install pandas numpy matplotlib openpyxl jupyter
   ```

   Or use requirements file if available:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running Python Scripts

Navigate to the experiment folder and run the Python file:

```bash
# For Experiment 1
cd EXP1
python EXP1.py

# For Experiment 2
cd EXP2
python EXP2.py

# For Experiment 3
cd EXP3
python EXP3.py
```

### Running Jupyter Notebooks

```bash
# Start Jupyter Notebook
jupyter notebook

# Navigate to the experiment folder and open the .ipynb file
```

### Running Demo Files

Each experiment folder contains a `demo.py` file for quick demonstrations:

```bash
cd EXP1
python demo.py
```

## 📂 Repository Structure

```
Data-Science-using-Python-LAB-/
│
├── EXP1/                          # Experiment 1: Data Analysis Fundamentals
│   ├── .vscode/
│   ├── EXP1.py
│   ├── demo.py
│   └── Sample_Aadhar_Enrollment_Dataset.xlsx
│
├── EXP2/                          # Experiment 2: Data Visualization
│   ├── .vscode/
│   ├── EXP2.py
│   ├── demo.py
│   ├── DOC.ipynb
│   ├── Sample_Aadhar_Enrollment_Dataset.xlsx
│   ├── EXP2 (Bar Chart Visualizations Created).docx
│   └── Image/
│       ├── bar_charts_by_state.png
│       ├── box_plots_distribution.png
│       ├── box_plot_overall_analysis.png
│       └── top_10_districts_bar_chart.png
│
├── EXP3/                          # Experiment 3: Exploring Pandas Library
│   ├── .vscode/
│   ├── EXP3.py
│   ├── Aadhar_Enrollment_Data.csv
│   ├── Aadhar_Enrollment_Output.xlsx
│   ├── Sample_Aadhar_Enrollment_Dataset.xlsx
│   └── EXP3 (Data Exploration).docx
│
└── README.md                      # This file
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Prem-Hanchate/Data-Science-using-Python-LAB-/issues).

### How to Contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**Prem Hanchate**

- GitHub: [@Prem-Hanchate](https://github.com/Prem-Hanchate)
- Repository: [Data-Science-using-Python-LAB-](https://github.com/Prem-Hanchate/Data-Science-using-Python-LAB-)

## 📝 License

This project is for educational purposes as part of the Data Science using Python Laboratory course.

## 📧 Contact

For any queries or suggestions, feel free to reach out through GitHub issues or contact the repository owner.

---

⭐ **If you find this repository helpful, please consider giving it a star!** ⭐

---

*Last Updated: February 2026*
