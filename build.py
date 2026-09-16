#!/usr/bin/env python3
"""Inline vendor libs (gzip + base64) into src.html -> index.html."""
import base64, gzip, pathlib

VENDORS = {
    "v-pdf": "dist/pdf.mjs",
    "v-pdf-worker": "dist/pdf.worker.mjs",
    "v-zxing": "dist/zxing-wasm.index.js",
    "v-zxing-wasm": "dist/zxing-reader.wasm",
}
tags = "\n".join(
    f'<script type="application/octet-stream" id="{k}">{base64.b64encode(gzip.compress(open(p, 'rb').read(), 9, mtime=0)).decode()}</script>'
    for k, p in VENDORS.items()
)
src = pathlib.Path("src.html").read_text()
pathlib.Path("index.html").write_text(src.replace("<!--VENDOR-->", tags))
