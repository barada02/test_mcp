#!/usr/bin/env python3
"""
Entry point for the Custom Calculator MCP Server
"""

import sys
import os

def main():
    """Main entry point for the MCP server"""
    # Suppress any potential import warnings or verbose output during startup
    # This is critical for MCP - only JSON-RPC messages should go to stdout
    
    # Redirect stderr temporarily during import to avoid contaminating stdout
    original_stderr = sys.stderr
    try:
        # Suppress stderr only during imports, not during actual MCP operation
        with open(os.devnull, 'w') as devnull:
            sys.stderr = devnull
            from server import mcp
        
        # Restore stderr before running MCP server
        sys.stderr = original_stderr
        
        # Run the MCP server - this must have clean stdout for JSON-RPC
        mcp.run()
        
    except ImportError as e:
        # Restore stderr for error reporting
        sys.stderr = original_stderr
        # Write errors to stderr, never stdout (stdout is for MCP JSON-RPC only)
        sys.stderr.write(f"Error: Could not import server module: {e}\n")
        sys.stderr.write("Make sure fastmcp is installed.\n")
        sys.exit(1)
    except Exception as e:
        # Restore stderr for error reporting
        sys.stderr = original_stderr
        sys.stderr.write(f"Error starting MCP server: {e}\n")
        sys.exit(1)
    finally:
        # Ensure stderr is always restored
        if sys.stderr != original_stderr:
            sys.stderr = original_stderr


if __name__ == "__main__":
    main()
