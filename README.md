# CSV to XML Converter for Premiere Pro

This Python script allows users to convert CSV files containing markers into XML files that can be imported into Premiere Pro. The XML files will include markers with their respective names, start frames, and end frames, facilitating a seamless transition between CSV lists and Premiere Pro timelines.

## Features

- Convert CSV files to Premiere Pro compatible XML format.
- Automatically calculates frame numbers based on the provided FPS.
- Appends the current date to the output XML filename in the format `DDMMYY`.

## Requirements

- Python 3.x
- pandas library (for CSV reading and manipulation)

## Installation

1. Clone this repository:

```bash
git clone <[https://github.com/folyaev/TIMETOMARK])>
```

2. Navigate to the repository directory:

```bash
cd <repository_directory>
```

3. Install the required Python libraries:

```bash
pip install pandas
```

## Usage

1. Run the script:

```bash
python csv_to_xml_converter_updated.py
```

2. Follow the on-screen prompts to provide:
   - Path to the CSV file.
   - Desired output XML file name (without extension).
   - Desired frames per second (e.g., `25` or `29.97`).

3. The script will generate an XML file with the current date appended to the filename. You can then import this XML file into Premiere Pro.

## CSV Format

The CSV file should contain markers with the following columns:

- `Тайминг`: The timing in the format `hh:mm:ss-hh:mm:ss`
- `О чём`: Marker name or description

**Note**: The script assumes that the first row of the CSV file is a header and skips it.

## Future Features (Planned)

- GUI for easier usage and interaction.
- Batch processing for converting multiple CSV files at once.
- Error handling and reporting for incorrect CSV formats.
- Support for additional CSV and XML formats.
  
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

You can copy the content above and save it as `README.md` in your GitHub repository. Make sure to adjust the placeholders (`<repository_url>` and `<repository_directory>`) as needed.
