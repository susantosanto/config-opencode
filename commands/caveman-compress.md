---
description: Compress a memory file (CLAUDE.md, todos, notes) into caveman format to save input tokens
---
Compress file: $ARGUMENTS

Run: python3 -m scripts <absolute_filepath>
(scripts/ lives next to this command file's parent skill directory)

The CLI detects file type, calls Claude to compress, validates output.
Original backed up as FILE.original.md. Compressed overwrites original.

Rules: drop articles/filler/pleasantries. Preserve code, URLs, paths, commands, technical terms exactly. Fragments OK.
