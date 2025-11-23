#!/usr/bin/env python3

def main():
    """Simple entry point for MCP server."""
    import sys
    import warnings
    
    # Suppress all warnings to keep stdout clean
    warnings.filterwarnings('ignore')
    
    try:
        from server import main as server_main
        server_main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
