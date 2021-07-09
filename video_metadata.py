import os
import glob
import subprocess
import pandas as pd


def run_exiftool(property, video):
    value = subprocess.run(
        ["exiftool", property, "-s", "-s", "-s", video], capture_output=True, text=True).stdout.strip("\n")
    return value


dir = input('Copy and past the directory: ')
ext = input('Enter the desired file types: ')

videos = glob.glob(os.path.join(dir, f"*.{ext}"))

metadata = {
    "CatID": [],
    "File_Title": [],
    "Record_Date": [],
    "Description": [],
    "File_Format": [],
    "Atlas_Name": [],
    "File_Path": [],
    "Digitization_Date": [],
    "File_Type": [],
    "File_Size": [],
    "Duration": [],
    "Video_Bit_Rate": [],
    "Video_Frame_Rate": [],
    "Video_Resolution": [],
    "Video_Aspect_Ratio": [],
    "Video_Codec": [],
    "Video_Bit_Depth": [],
    "Audio_Codec": [],
    "Audio_Bit_Rate": [],
    "Audio_Bit_Depth": [],
    "Audio_Sample_Rate": []
}

for v in videos:
    basename = os.path.basename(v)
    print(f"Now examining: {basename}")

    metadata["CatID"].append("XXXX")
    metadata["File_Title"].append("XXXX")
    metadata["Record_Date"].append("XXXX")
    metadata["Description"].append("XXXX")
    metadata["File_Format"].append(run_exiftool("-*FileTypeExtension*", v))

    metadata["Atlas_Name"].append(basename)
    metadata["File_Path"].append(v)

    metadata["Digitization_Date"].append("2019")
    metadata["File_Type"].append(run_exiftool("-*MIMEType*", v))

    try:
        bytes = int(run_exiftool("-*MediaDataSize*", v))
        mb = bytes/1024/1024
        file_size = str(round(mb, 2))
        metadata["File_Size"].append(file_size)
    except ValueError:
        metadata["File_Size"].append("ValueError")
    except:
        metadata["File_Size"].append("CalcError")

    time = run_exiftool("-*Duration*", v)
    metadata["Duration"].append(time[0:7])

    metadata["Video_Bit_Rate"].append(run_exiftool("-*BitDepth*", v))
    metadata["Video_Frame_Rate"].append(run_exiftool("-*VideoFrameRate*", v))

    x = run_exiftool("-*SourceImageWidth*", v)
    y = run_exiftool("-*SourceImageHeight*", v)
    metadata["Video_Resolution"].append(f"{x} x {y}")

    metadata["Video_Aspect_Ratio"].append(
        run_exiftool("-*PixelAspectRatio*", v))
    metadata["Video_Codec"].append(run_exiftool("-*CompressorID*", v))
    metadata["Video_Bit_Depth"].append(run_exiftool("-*BitDepth*", v))

    metadata["Audio_Codec"].append(run_exiftool("-*AudioFormat*", v))
    metadata["Audio_Bit_Rate"].append(run_exiftool("-*AvgBitrate*", v))
    metadata["Audio_Bit_Depth"].append(
        run_exiftool("-*AudioBitsPerSample*", v))
    metadata["Audio_Sample_Rate"].append(run_exiftool("-*AudioSampleRate*", v))


df = pd.DataFrame(metadata)
csv_path = os.path.join(dir, "video_metadata.csv")
df.to_csv(csv_path, index=False, encoding='utf-8-sig')
print(df)
