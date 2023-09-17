import pandas as pd
import xml.etree.ElementTree as ET
import datetime

def full_time_to_frames(time_str, fps=25):
    parts = list(map(int, time_str.split(":")))
    if len(parts) == 2:  # mm:ss format
        hours, minutes, seconds, frames = 0, parts[0], parts[1], 0
    elif len(parts) == 3:  # hh:mm:ss format
        hours, minutes, seconds, frames = parts[0], parts[1], parts[2], 0
    else:
        return None
    return (hours * 3600 + minutes * 60 + seconds) * fps + frames

def csv_to_xml_with_date(csv_path, output_xml_base_path, fps=25):
    csv_data = pd.read_csv(csv_path, skiprows=1)
    csv_data["Start Frame"] = csv_data["Тайминг"].str.split('-').str[0].apply(lambda x: full_time_to_frames(x, fps))
    csv_data["End Frame"] = csv_data["Тайминг"].str.split('-').str[1].apply(lambda x: full_time_to_frames(x, fps))
    
    root = ET.Element("xmeml", version="5")
    sequence = ET.SubElement(root, "sequence")
    ET.SubElement(sequence, "uuid").text = '15a8696a-7d3b-4350-8e01-af758bef5656'
    ET.SubElement(sequence, "duration").text = '0'
    ET.SubElement(sequence, "name").text = 'DP_100500 COLOR'

    rate_elem = ET.SubElement(sequence, "rate")
    ET.SubElement(rate_elem, "timebase").text = str(fps)
    ET.SubElement(rate_elem, "ntsc").text = 'FALSE'

    media_elem = ET.SubElement(sequence, "media")
    ET.SubElement(media_elem, "video")
    ET.SubElement(media_elem, "audio")

    timecode_elem = ET.SubElement(sequence, "timecode")
    rate_sub_elem = ET.SubElement(timecode_elem, "rate")
    ET.SubElement(rate_sub_elem, "timebase").text = str(fps)
    ET.SubElement(rate_sub_elem, "ntsc").text = 'FALSE'
    ET.SubElement(timecode_elem, "string").text = '00:00:00:00'
    ET.SubElement(timecode_elem, "frame").text = '0'
    ET.SubElement(timecode_elem, "displayformat").text = 'NDF'

    labels_elem = ET.SubElement(sequence, "labels")
    ET.SubElement(labels_elem, "label2").text = 'Forest'

    logginginfo_elem = ET.SubElement(sequence, "logginginfo")
    for sub_elem_tag in ["description", "scene", "shottake", "lognote", "good", "originalvideofilename", "originalaudiofilename"]:
        ET.SubElement(logginginfo_elem, sub_elem_tag)
    
    for _, row in csv_data.iterrows():
        marker = ET.SubElement(sequence, "marker")
        ET.SubElement(marker, "name").text = row["О чём"]
        ET.SubElement(marker, "in").text = str(row["Start Frame"])
        ET.SubElement(marker, "out").text = str(row["End Frame"])
    
    current_date = datetime.datetime.now().strftime("%d%m%y")
    output_xml_path = f"{output_xml_base_path}_{current_date}.xml"
    tree = ET.ElementTree(root)
    tree.write(output_xml_path)
    
    return output_xml_path

if __name__ == "__main__":
    csv_path = input("Enter the path to the CSV file: ")
    output_xml_base_path = input("Enter the base path for the output XML file (without extension): ")
    fps = float(input("Enter the desired frames per second (e.g. 25 or 29.97): "))
    saved_path = csv_to_xml_with_date(csv_path, output_xml_base_path, fps)
    print(f"XML file saved to {saved_path}")
