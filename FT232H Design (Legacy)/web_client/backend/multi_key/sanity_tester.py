from bitbang_mcp import BitBangMCP
import time

# Change address if needed
mcp = BitBangMCP(address=0x27)

try:
    print("Setting GPIOA (0x00) to OUTPUT mode...")
    mcp.write_register(0x00, 0x00)  # IODIRA = all outputs

    for i in range(5):
        print("GPIOA HIGH")
        mcp.write_register(0x12, 0xFF)  # All PA pins HIGH
        time.sleep(0.5)

        print("GPIOA LOW")
        mcp.write_register(0x12, 0x00)  # All PA pins LOW
        time.sleep(0.5)

    print("Test complete.")

finally:
    mcp.write_register(0x12, 0x00)  # Leave pins LOW
    mcp.close()
