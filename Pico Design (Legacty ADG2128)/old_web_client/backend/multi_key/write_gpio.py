from bitbang_mcp import BitBangMCP
import time

mcp = BitBangMCP(address=0x27)

# Set IODIRB (0x01) to all outputs
mcp.write_register(0x01, 0x00)

# Switch 1
mcp.write_register(0x13, BitBangMCP.PB2)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PB0)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PB1)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PB3)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)

# Switch 2
mcp.write_register(0x13, BitBangMCP.PB4)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PB6)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PB7)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PB5)
time.sleep(0.1)
mcp.write_register(0x13, BitBangMCP.PBLOW)
time.sleep(0.1)

# Switch 3
mcp.write_register(0x12, BitBangMCP.PA7)
time.sleep(0.1)
mcp.write_register(0x12, BitBangMCP.PALOW)
time.sleep(0.1)
# mcp.write_register(0x12, BitBangMCP.PA5)
# time.sleep(0.1)
# mcp.write_register(0x12, BitBangMCP.PALOW)
# time.sleep(0.1)
# mcp.write_register(0x12, BitBangMCP.PA6)
# time.sleep(0.1)
# mcp.write_register(0x12, BitBangMCP.PALOW)
# time.sleep(0.1)

mcp.close()

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26