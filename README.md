# Rogue Blender MCP

**Rogue Development** MCP bridge for Blender 5.1+ — modeling, sculpting, mesh ops, and full scene control through your AI host (Cursor, Claude Code, and compatible clients).

- Asset Store: https://rogue-dev-studio.github.io/rogue-asset-store/
- Repo: https://github.com/rogue-dev-studio/rogue-blender-mcp

## Requirements

1. **Blender 5.1+** (5.2 recommended)
2. Blender **MCP** extension enabled, server **listening** (Preferences → Extensions → MCP → Start MCP Server)
3. [uv](https://github.com/astral-sh/uv) (`uvx` on PATH)

Default socket: `localhost:9876`.

## Install (no clone)

Requires [uv](https://github.com/astral-sh/uv) on PATH (`uvx`).

### Cursor MCP config

Paste into `~/.cursor/mcp.json` (or merge under `mcpServers`), then restart Cursor:

```json
{
  "mcpServers": {
    "rogue-blender": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/rogue-dev-studio/rogue-blender-mcp.git",
        "rogue-blender-mcp"
      ],
      "env": {
        "BLENDER_MCP_HOST": "localhost",
        "BLENDER_MCP_PORT": "9876"
      }
    }
  }
}
```

Or copy `cursor.mcp.fragment.json` from this repo.

One-liner check (downloads from GitHub, no clone):

```bash
uvx --from git+https://github.com/rogue-dev-studio/rogue-blender-mcp.git rogue-blender-mcp
```

### Local editable install

```bash
uv pip install -e .
rogue-blender-mcp
```

## Workflow

1. Open Blender and start the MCP server in the extension preferences.
2. Restart Cursor so `rogue-blender` tools appear.
3. Ask the agent to model, sculpt, inspect, or render — including organic forms via Sculpt Mode and mesh editing via `bpy`.

## Capabilities

Through the live Blender session the agent can:

- Create and edit mesh geometry (extrude, bevel, boolean, modifiers)
- Enter sculpt workflows and apply mesh filters / remesh paths
- Manage materials, lights, cameras, and collections
- Execute precise Blender Python (`bpy` / `bmesh`) for advanced modeling
- Capture viewport / render output for iterative refine loops

## Contact

- Contact: https://rogue-dev-studio.github.io/contact/
- Studio: https://rogue-dev-studio.github.io/

## License

MIT — Rogue Development. See `LICENSE` and `NOTICE`.
