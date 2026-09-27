# Processed data archive parts

The processed-data ZIP is distributed as **11 binary parts**. Each part is at
most 20,000,000 bytes (20 MB). The original archive is unchanged.

Upload all `.part001` through `.part011` files, `parts_manifest.json`,
`merge_parts.py`, and this README together. Keep filenames unchanged.
These parts are **not independent ZIP archives** and cannot be extracted
separately. Do not rename a part to `.zip`.

## Restore the archive

1. Download all 11 parts and the two supporting files into one directory.
   Download the actual file contents, not a saved GitHub HTML preview page.
2. Install Python 3 if necessary. No third-party packages are required.
3. Open a terminal in that directory and run:

   ```text
   python merge_parts.py
   ```

   On Windows, `py -3 merge_parts.py` is an alternative if Python is available
   through the Python launcher.

4. The script checks each part's size and SHA-256 hash, joins the parts in the
   recorded order, and verifies the full archive hash. It produces
   `11_Processed_Data_TriCal5.zip` in the same directory and leaves the parts
   unchanged. It refuses to overwrite an existing output archive.
5. Extract the restored ZIP with a normal ZIP extraction tool. Use a folder
   named `11_Processed_Data_TriCal5` beside the reproducibility package, as
   described in the reproducibility README.

Allow at least 420 MB of additional free space for archive reconstruction,
plus the space required to extract the data. The restored archive is
206,678,059 bytes. Exact part sizes and hashes are in `parts_manifest.json`.

If verification fails, download the named part again before retrying. Do not
skip a missing part or combine files from different releases. If a failed
write leaves an incomplete output ZIP, move it aside before rerunning.

This is a transport copy of the processed evidence package, not a new
experiment or a replacement for the original image dataset. Historical and
superseded evidence retains its existing labels inside the archive.
