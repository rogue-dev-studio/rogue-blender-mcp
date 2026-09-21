"""
@Author: rogue-dev-studio
@Date: 2026-09-20 14:10:00
@Last Modified by: rogue-dev-studio
@Last Modified time: 2026-09-21 12:25:00
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys


LAB_MCP_SPEC = (
    "git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp"
)


def _resolve_uv() -> str:
    for name in ("uv", "uv.exe"):
        found = shutil.which(name)
        if found:
            return found
    uvx = shutil.which("uvx") or shutil.which("uvx.exe")
    if uvx:
        return uvx
    print(
        "rogue-blender-mcp: uv not found. Install uv "
        "(https://github.com/astral-sh/uv) and retry.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def main() -> None:
    host = os.environ.get("BLENDER_MCP_HOST", "localhost")
    port = os.environ.get("BLENDER_MCP_PORT", "9876")
    os.environ.setdefault("BLENDER_MCP_HOST", host)
    os.environ.setdefault("BLENDER_MCP_PORT", port)

    uv = _resolve_uv()
    base = os.path.basename(uv).lower()
    if base.startswith("uvx"):
        cmd = [uv, "--from", LAB_MCP_SPEC, "blender-mcp"]
    else:
        cmd = [uv, "tool", "run", "--from", LAB_MCP_SPEC, "blender-mcp"]

    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
