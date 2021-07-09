# VideoMetadata
prepares metadata for videos in aclu collection.

requires exiftool = https://exiftool.org/ or through homebrew, scoop, etc.

ERRORS:
<br>
Now examining: 10157_P_ACLU_News_Robert-Mueller-911_2003_14799.mp4
Traceback (most recent call last):
  File "C:\Users\intern_admf_esilb\Desktop\scripts\video_metadata.py", line 58, in <module>
    bytes = int(run_exiftool("-*MediaDataSize*", v))
ValueError: invalid literal for int() with base 10: ''
PS C:\Users\intern_admf_esilb\Desktop\scripts>
