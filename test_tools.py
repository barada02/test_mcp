#!/usr/bin/env python3
"""
Simple test to verify MCP tools work correctly
"""

def test_mcp_tools():
    """Test that all MCP tool functions work correctly"""
    print("Testing MCP Calculator Tools...")
    
    # Import the server module
    try:
        import server
        print("✓ Server module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import server: {e}")
        return False
    
    # Test each tool function directly (bypassing MCP wrapper)
    tests_passed = 0
    total_tests = 6
    
    # Test 1: Basic Calculator
    try:
        # Get the actual function from the tool wrapper
        basic_calc_func = server.basic_calculator._fn if hasattr(server.basic_calculator, '_fn') else server.basic_calculator
        if callable(basic_calc_func):
            result = basic_calc_func("2 + 3 * 4")
            if result.get("result") == 14 and result.get("success"):
                print("✓ Basic calculator works")
                tests_passed += 1
            else:
                print(f"✗ Basic calculator failed: {result}")
        else:
            print("✗ Basic calculator is not callable")
    except Exception as e:
        print(f"✗ Basic calculator error: {e}")
    
    # Test 2: Statistical Calculator
    try:
        stats_calc_func = server.statistical_calculator._fn if hasattr(server.statistical_calculator, '_fn') else server.statistical_calculator
        if callable(stats_calc_func):
            result = stats_calc_func([1, 2, 3, 4, 5], "mean")
            if result.get("results", {}).get("mean") == 3.0 and result.get("success"):
                print("✓ Statistical calculator works")
                tests_passed += 1
            else:
                print(f"✗ Statistical calculator failed: {result}")
        else:
            print("✗ Statistical calculator is not callable")
    except Exception as e:
        print(f"✗ Statistical calculator error: {e}")
    
    # Test 3: Unit Converter
    try:
        unit_conv_func = server.unit_converter._fn if hasattr(server.unit_converter, '_fn') else server.unit_converter
        if callable(unit_conv_func):
            result = unit_conv_func(1000, "m", "km", "length")
            if result.get("converted_value") == 1.0 and result.get("success"):
                print("✓ Unit converter works")
                tests_passed += 1
            else:
                print(f"✗ Unit converter failed: {result}")
        else:
            print("✗ Unit converter is not callable")
    except Exception as e:
        print(f"✗ Unit converter error: {e}")
    
    # Test 4: Compound Interest Calculator
    try:
        compound_func = server.compound_interest_calculator._fn if hasattr(server.compound_interest_calculator, '_fn') else server.compound_interest_calculator
        if callable(compound_func):
            result = compound_func(1000, 5, 1)
            if result.get("final_amount") == 1050.0 and result.get("success"):
                print("✓ Compound interest calculator works")
                tests_passed += 1
            else:
                print(f"✗ Compound interest calculator failed: {result}")
        else:
            print("✗ Compound interest calculator is not callable")
    except Exception as e:
        print(f"✗ Compound interest calculator error: {e}")
    
    # Test 5: Geometry Calculator
    try:
        geometry_func = server.geometry_calculator._fn if hasattr(server.geometry_calculator, '_fn') else server.geometry_calculator
        if callable(geometry_func):
            result = geometry_func("circle", radius=5.0)
            expected_area = 3.14159 * 25  # π * r²
            if abs(result.get("area", 0) - expected_area) < 0.1 and result.get("success"):
                print("✓ Geometry calculator works")
                tests_passed += 1
            else:
                print(f"✗ Geometry calculator failed: {result}")
        else:
            print("✗ Geometry calculator is not callable")
    except Exception as e:
        print(f"✗ Geometry calculator error: {e}")
    
    # Test 6: Date Calculator
    try:
        date_func = server.date_calculator._fn if hasattr(server.date_calculator, '_fn') else server.date_calculator
        if callable(date_func):
            result = date_func("2024-01-01", "add", 30, "days")
            if result.get("result_date") == "2024-01-31" and result.get("success"):
                print("✓ Date calculator works")
                tests_passed += 1
            else:
                print(f"✗ Date calculator failed: {result}")
        else:
            print("✗ Date calculator is not callable")
    except Exception as e:
        print(f"✗ Date calculator error: {e}")
    
    print(f"\\nTest Results: {tests_passed}/{total_tests} tools working correctly")
    
    if tests_passed == total_tests:
        print("🎉 All MCP calculator tools are working!")
        print("✅ Ready for deployment to IBM Watson Orchestrate")
        return True
    else:
        print("❌ Some tools need fixing before deployment")
        return False

if __name__ == "__main__":
    test_mcp_tools()