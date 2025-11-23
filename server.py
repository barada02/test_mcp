#!/usr/bin/env python3
"""
Custom Calculation MCP Server

A Model Context Protocol server that provides various calculation tools
including basic math, statistical calculations, unit conversions, and more.
"""

import asyncio
import math
import statistics
from typing import List, Union, Optional
from datetime import datetime, timedelta

from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Custom Calculator Server")


@mcp.tool()
def basic_calculator(expression: str) -> dict:
    """
    Evaluate basic mathematical expressions safely.
    
    Args:
        expression: Mathematical expression to evaluate (e.g., "2 + 3 * 4")
    
    Returns:
        Dictionary with result and expression
    """
    try:
        # Only allow safe mathematical operations
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        allowed_names.update({
            "abs": abs, "round": round, "min": min, "max": max,
            "sum": sum, "pow": pow
        })
        
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        
        return {
            "expression": expression,
            "result": result,
            "success": True
        }
    except Exception as e:
        return {
            "expression": expression,
            "error": str(e),
            "success": False
        }


@mcp.tool()
def statistical_calculator(numbers: List[float], operation: str = "all") -> dict:
    """
    Perform statistical calculations on a list of numbers.
    
    Args:
        numbers: List of numbers to analyze
        operation: Type of calculation ("mean", "median", "mode", "std", "variance", "all")
    
    Returns:
        Dictionary with statistical results
    """
    if not numbers:
        return {"error": "Empty list provided", "success": False}
    
    try:
        results = {}
        
        if operation in ["mean", "all"]:
            results["mean"] = statistics.mean(numbers)
            
        if operation in ["median", "all"]:
            results["median"] = statistics.median(numbers)
            
        if operation in ["mode", "all"]:
            try:
                results["mode"] = statistics.mode(numbers)
            except statistics.StatisticsError:
                results["mode"] = "No unique mode found"
                
        if operation in ["std", "all"] and len(numbers) > 1:
            results["standard_deviation"] = statistics.stdev(numbers)
            
        if operation in ["variance", "all"] and len(numbers) > 1:
            results["variance"] = statistics.variance(numbers)
            
        if operation == "all":
            results["count"] = len(numbers)
            results["sum"] = sum(numbers)
            results["min"] = min(numbers)
            results["max"] = max(numbers)
            results["range"] = max(numbers) - min(numbers)
        
        return {
            "numbers": numbers,
            "operation": operation,
            "results": results,
            "success": True
        }
    except Exception as e:
        return {
            "numbers": numbers,
            "operation": operation,
            "error": str(e),
            "success": False
        }


@mcp.tool()
def unit_converter(value: float, from_unit: str, to_unit: str, unit_type: str) -> dict:
    """
    Convert between different units of measurement.
    
    Args:
        value: The numeric value to convert
        from_unit: Source unit
        to_unit: Target unit
        unit_type: Type of unit ("length", "weight", "temperature", "volume")
    
    Returns:
        Dictionary with conversion result
    """
    try:
        # Unit conversion factors (to base unit)
        conversions = {
            "length": {
                "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                "inch": 0.0254, "ft": 0.3048, "yard": 0.9144, "mile": 1609.34
            },
            "weight": {
                "mg": 0.001, "g": 1, "kg": 1000, "lb": 453.592, "oz": 28.3495
            },
            "volume": {
                "ml": 0.001, "l": 1, "gal": 3.78541, "qt": 0.946353, "cup": 0.236588
            }
        }
        
        if unit_type == "temperature":
            # Special handling for temperature
            if from_unit == "celsius":
                if to_unit == "fahrenheit":
                    result = (value * 9/5) + 32
                elif to_unit == "kelvin":
                    result = value + 273.15
                else:
                    result = value
            elif from_unit == "fahrenheit":
                if to_unit == "celsius":
                    result = (value - 32) * 5/9
                elif to_unit == "kelvin":
                    result = (value - 32) * 5/9 + 273.15
                else:
                    result = value
            elif from_unit == "kelvin":
                if to_unit == "celsius":
                    result = value - 273.15
                elif to_unit == "fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value
            else:
                raise ValueError(f"Unknown temperature unit: {from_unit}")
        else:
            # Standard unit conversion
            if unit_type not in conversions:
                raise ValueError(f"Unknown unit type: {unit_type}")
            
            units = conversions[unit_type]
            if from_unit not in units or to_unit not in units:
                raise ValueError(f"Unknown unit for {unit_type}: {from_unit} or {to_unit}")
            
            # Convert to base unit, then to target unit
            base_value = value * units[from_unit]
            result = base_value / units[to_unit]
        
        return {
            "original_value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "unit_type": unit_type,
            "converted_value": result,
            "success": True
        }
    except Exception as e:
        return {
            "original_value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "unit_type": unit_type,
            "error": str(e),
            "success": False
        }


@mcp.tool()
def compound_interest_calculator(
    principal: float, 
    rate: float, 
    time: float, 
    compound_frequency: int = 1
) -> dict:
    """
    Calculate compound interest.
    
    Args:
        principal: Initial amount (principal)
        rate: Annual interest rate (as percentage, e.g., 5 for 5%)
        time: Time period in years
        compound_frequency: How many times interest is compounded per year (default: 1)
    
    Returns:
        Dictionary with compound interest calculations
    """
    try:
        # Convert percentage to decimal
        r = rate / 100
        
        # Compound interest formula: A = P(1 + r/n)^(nt)
        amount = principal * (1 + r/compound_frequency) ** (compound_frequency * time)
        interest_earned = amount - principal
        
        return {
            "principal": principal,
            "annual_rate_percent": rate,
            "time_years": time,
            "compound_frequency": compound_frequency,
            "final_amount": round(amount, 2),
            "interest_earned": round(interest_earned, 2),
            "total_return_percent": round((interest_earned / principal) * 100, 2),
            "success": True
        }
    except Exception as e:
        return {
            "principal": principal,
            "annual_rate_percent": rate,
            "time_years": time,
            "compound_frequency": compound_frequency,
            "error": str(e),
            "success": False
        }


@mcp.tool()
def geometry_calculator(
    shape: str, 
    radius: Optional[float] = None,
    length: Optional[float] = None,
    width: Optional[float] = None,
    height: Optional[float] = None,
    base: Optional[float] = None,
    side: Optional[float] = None
) -> dict:
    """
    Calculate area, perimeter, and volume for various geometric shapes.
    
    Args:
        shape: Shape type ("circle", "rectangle", "triangle", "sphere", "cylinder", "cube")
        radius: Radius for circles, spheres, cylinders
        length: Length for rectangles
        width: Width for rectangles
        height: Height for triangles, cylinders
        base: Base for triangles
        side: Side length for cubes
    
    Returns:
        Dictionary with geometric calculations
    """
    try:
        dimensions = {k: v for k, v in locals().items() if k != 'shape' and v is not None}
        results = {"shape": shape, "dimensions": dimensions}
        
        if shape == "circle":
            if radius is None:
                raise ValueError("Circle requires 'radius' parameter")
            results["area"] = math.pi * radius ** 2
            results["circumference"] = 2 * math.pi * radius
            
        elif shape == "rectangle":
            if length is None or width is None:
                raise ValueError("Rectangle requires 'length' and 'width' parameters")
            results["area"] = length * width
            results["perimeter"] = 2 * (length + width)
            
        elif shape == "triangle":
            if base is None or height is None:
                raise ValueError("Triangle requires 'base' and 'height' parameters")
            results["area"] = 0.5 * base * height
            
        elif shape == "sphere":
            if radius is None:
                raise ValueError("Sphere requires 'radius' parameter")
            results["volume"] = (4/3) * math.pi * radius ** 3
            results["surface_area"] = 4 * math.pi * radius ** 2
            
        elif shape == "cylinder":
            if radius is None or height is None:
                raise ValueError("Cylinder requires 'radius' and 'height' parameters")
            results["volume"] = math.pi * radius ** 2 * height
            results["surface_area"] = 2 * math.pi * radius * (radius + height)
            
        elif shape == "cube":
            if side is None:
                raise ValueError("Cube requires 'side' parameter")
            results["volume"] = side ** 3
            results["surface_area"] = 6 * side ** 2
            
        else:
            raise ValueError(f"Unknown shape: {shape}")
        
        results["success"] = True
        return results
        
    except Exception as e:
        return {
            "shape": shape,
            "dimensions": {k: v for k, v in locals().items() if k != 'shape' and v is not None},
            "error": str(e),
            "success": False
        }


@mcp.tool()
def date_calculator(start_date: str, operation: str, value: int, unit: str = "days") -> dict:
    """
    Perform date calculations (add/subtract time periods).
    
    Args:
        start_date: Starting date in YYYY-MM-DD format
        operation: "add" or "subtract"
        value: Number of units to add/subtract
        unit: Time unit ("days", "weeks", "months", "years")
    
    Returns:
        Dictionary with date calculation results
    """
    try:
        # Parse the start date
        start = datetime.strptime(start_date, "%Y-%m-%d")
        
        # Calculate the time delta
        if unit == "days":
            delta = timedelta(days=value)
        elif unit == "weeks":
            delta = timedelta(weeks=value)
        elif unit == "months":
            # Approximate months as 30 days
            delta = timedelta(days=value * 30)
        elif unit == "years":
            # Approximate years as 365 days
            delta = timedelta(days=value * 365)
        else:
            raise ValueError(f"Unknown unit: {unit}")
        
        # Apply the operation
        if operation == "add":
            result_date = start + delta
        elif operation == "subtract":
            result_date = start - delta
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        # Calculate the difference in days
        days_difference = (result_date - start).days
        
        return {
            "start_date": start_date,
            "operation": operation,
            "value": value,
            "unit": unit,
            "result_date": result_date.strftime("%Y-%m-%d"),
            "days_difference": days_difference,
            "success": True
        }
    except Exception as e:
        return {
            "start_date": start_date,
            "operation": operation,
            "value": value,
            "unit": unit,
            "error": str(e),
            "success": False
        }


def main():
    """Main function for running the MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()
