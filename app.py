from fastmcp import FastMCP

app=FastMCP("My MCP Server")

@app.tool

def add(n1:int, n2:int)->int:
    """
    將兩個數字相加
    """
    return n1+n2