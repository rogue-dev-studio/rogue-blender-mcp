"""
@Author: rogue-dev-studio
@Date: 2026-09-20 14:10:00
@Last Modified by: rogue-dev-studio
@Last Modified time: 2026-09-20 14:10:00
"""
from __future__ import annotations

import os
import shutil
import sys


LAB_MCP_SPEC = (
    "git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp"
)


def main() -> None:
    host = os.environ.get("BLENDER_MCP_HOST", "localhost")
    port = os.environ.get("BLENDER_MCP_PORT", "9876")
    os.environ.setdefault("BLENDER_MCP_HOST", host)
    os.environ.setdefault("BLENDER_MCP_PORT", port)

    uvx = shutil.which("uvx")
    if not uvx:
        print(
            "rogue-blender-mcp: uvx not found. Install uv "
            "(https://github.com/astral-sh/uv) and retry.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    args = [
        uvx,
        "--from",
        LAB_MCP_SPEC,
        "blender-mcp",
    ]
    os.execv(uvx, args)


if __name__ == "__main__":
    main()
