# Canophea: A Programmatic Approach to Security Control Engineering

## **Overview**
**Canophea** is a **Streamlit application** designed to assist engineers in considering system design aspects for computer systems. It provides an interactive interface to explore, analyze, and manipulate database structures.

---

## **Features**

### 1. **Explore Database**
- **View Tables**: Get a list of all tables in the connected database.
- **View Table Schema**: Inspect metadata and column information (column names, types, constraints) for any table.
- **Preview Data**:
  - View rows of data from the table.
  - Paginate through data with customizable rows per page.
- **Advanced Actions**:
  - **Filtering**: Apply dynamic filters to table data based on specific column values.
  - **Sorting**: Sort table rows by a selected column in ascending or descending order.
- **Data Insights**:
  - Basic statistics (mean, median, mode, etc.) for numerical columns.
  - Column information such as data types.

### 2. **Interactive Interface**
- **Streamlit-based** web application for easy access and exploration.
- **Responsive design** for a seamless experience across devices.

### 3. **Data Manipulation**
- Edit and modify data directly within the application.
- Perform bulk operations on selected data sets.

### 4. **Customization**
- **Personalizable dashboard** for tailored viewing preferences.
- Configurable data display settings.

---

## **Getting Started**

### **Clone the repository**:
```bash
git clone https://github.com/username/canophea.git
```

### **Create a Virtual Environment**:
Run the provided setup script:
```bash
python setup_venv.py
```

### **Activate the Environment**:
For macOS/Linux:
```bash
source venv/bin/activate
```
For Windows:
```bash
venv\Scripts\activate
```

### **Install dependencies**:
```bash
pip install -r requirements.txt
```

### **Run the application**:
```bash
python main.py
```

Visit the local URL displayed (e.g., `http://localhost:8501`) in your browser to start using the app.

---

## **Contributing**
Contributions are welcome! Please feel free to:
1. Fork this repository.
2. Create a feature branch.
3. Submit a Pull Request.

---

## **License**
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## **Acknowledgments**
- [**Streamlit**](https://streamlit.io) for the app framework.
- [**Pandas**](https://pandas.pydata.org) for data manipulation.
- [**NumPy**](https://numpy.org) for numerical computation.

---

## **Contact**
- **Rye** - [Mastodon Profile](https://ioc.exchange/@rye)

**Project Link**: [https://github.com/green-dino/canophea](https://github.com/green-dino/canophea)