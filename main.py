#!/usr/bin/env python3
"""
Entry point for the Custom Calculator MCP Server
"""

def main():
    """Main entry point for the MCP server"""
    try:
        from server import mcp
        mcp.run()
    except ImportError:
        print("Error: Could not import server module. Make sure fastmcp is installed.")
        print("Install with: pip install fastmcp")
        exit(1)
    except Exception as e:
        print(f"Error starting MCP server: {e}")
        exit(1)


if __name__ == "__main__":
    main()
