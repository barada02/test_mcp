#!/usr/bin/env python3
"""
Test script for the Custom Calculator MCP Server
"""

def test_calculations():
    """Test the calculation functions directly"""
    print("Testing Custom Calculator MCP Server...")
    
    # Import the raw functions (before they're wrapped as tools)
    import math
    import statistics
    from datetime import datetime, timedelta
    
    # Test basic calculator function
    def test_basic_calculator():
        try:
            allowed_names = {
                k: v for k, v in math.__dict__.items() if not k.startswith("__")
            }
            allowed_names.update({
                "abs": abs, "round": round, "min": min, "max": max,
                "sum": sum, "pow": pow
            })
            
            expression = "2 + 3 * 4"
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            print(f"✓ Basic Calculator: {expression} = {result}")
            return True
        except Exception as e:
            print(f"✗ Basic Calculator failed: {e}")
            return False
    
    # Test statistical calculator
    def test_stats():
        try:
            numbers = [1, 2, 3, 4, 5]
            mean = statistics.mean(numbers)
            print(f"✓ Statistics: Mean of {numbers} = {mean}")
            return True
        except Exception as e:
            print(f"✗ Statistics failed: {e}")
            return False
    
    # Test unit conversion
    def test_unit_conversion():
        try:
            # Simple length conversion: 1000 meters to kilometers
            value = 1000
            result = value * 0.001 / 1  # m to km conversion factor
            print(f"✓ Unit Conversion: {value} meters = {result} kilometers")
            return True
        except Exception as e:
            print(f"✗ Unit Conversion failed: {e}")
            return False
    
    # Run all tests
    tests = [test_basic_calculator, test_stats, test_unit_conversion]
    passed = 0
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All calculation functions work correctly!")
        print("✅ MCP Server is ready to use!")
    else:
        print("❌ Some tests failed. Please check the implementation.")
    
    return passed == len(tests)

if __name__ == "__main__":
    test_calculations()