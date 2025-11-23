# Custom Calculator MCP Server

A Model Context Protocol (MCP) server that provides various calculation tools including basic math, statistics, unit conversions, geometry, financial calculations, and date operations.

## Features

This MCP server provides the following calculation tools:

### 🧮 Basic Calculator
- **`basic_calculator`**: Safely evaluate mathematical expressions
- Supports all standard math operations and functions from Python's `math` module
- Example: `"2 + 3 * sqrt(16)"` → `14.0`

### 📊 Statistical Calculator  
- **`statistical_calculator`**: Perform statistical analysis on number lists
- Calculate mean, median, mode, standard deviation, variance
- Get summary statistics including min, max, range, count, sum
- Example: `[1, 2, 3, 4, 5]` → mean: 3.0, median: 3, std: 1.58...

### 🔄 Unit Converter
- **`unit_converter`**: Convert between different units of measurement
- Supports length, weight, volume, and temperature conversions
- Length: mm, cm, m, km, inch, ft, yard, mile
- Weight: mg, g, kg, lb, oz
- Volume: ml, l, gal, qt, cup
- Temperature: celsius, fahrenheit, kelvin

### 💰 Compound Interest Calculator
- **`compound_interest_calculator`**: Calculate compound interest and investment growth
- Supports different compounding frequencies
- Returns final amount, interest earned, and total return percentage

### 📐 Geometry Calculator
- **`geometry_calculator`**: Calculate area, perimeter, and volume for shapes
- Supported shapes: circle, rectangle, triangle, sphere, cylinder, cube
- Automatically calculates relevant measurements (area, perimeter, volume, surface area)

### 📅 Date Calculator
- **`date_calculator`**: Perform date arithmetic
- Add or subtract days, weeks, months, or years from a given date
- Returns the result date and the difference in days

## Installation

### Option 1: Install from Git Repository (Recommended)

You can install this MCP server directly from a Git repository using pip:

```bash
pip install git+https://github.com/yourusername/custom-calculator-mcp.git
```

### Option 2: Local Development Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install in development mode:

```bash
pip install -e .
```

## Usage

### Running the Server

After installation, you can run the MCP server:

```bash
python server.py
```

Or if you installed it as a package:

```bash
custom-calculator-mcp
```

### Example Tool Calls

#### Basic Calculator
```python
# Evaluate: 2 + 3 * sqrt(16)
{
    "expression": "2 + 3 * sqrt(16)",
    "result": 14.0,
    "success": true
}
```

#### Statistical Analysis
```python
# Analyze numbers: [10, 20, 30, 40, 50]
{
    "numbers": [10, 20, 30, 40, 50],
    "operation": "all",
    "results": {
        "mean": 30.0,
        "median": 30.0,
        "standard_deviation": 15.811,
        "count": 5,
        "min": 10,
        "max": 50,
        "range": 40
    },
    "success": true
}
```

#### Unit Conversion
```python
# Convert 100 kilometers to miles
{
    "original_value": 100,
    "from_unit": "km",
    "to_unit": "mile", 
    "unit_type": "length",
    "converted_value": 62.137,
    "success": true
}
```

#### Compound Interest
```python
# $1000 at 5% for 10 years, compounded annually
{
    "principal": 1000,
    "annual_rate_percent": 5,
    "time_years": 10,
    "final_amount": 1628.89,
    "interest_earned": 628.89,
    "total_return_percent": 62.89,
    "success": true
}
```

## Configuration

The server uses FastMCP and runs on the default MCP transport. No additional configuration is required for basic usage.

## Requirements

- Python 3.10 or higher
- FastMCP 2.13.1 or higher

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
- Create an issue on GitHub
- Check the FastMCP documentation: https://github.com/jlowin/fastmcp