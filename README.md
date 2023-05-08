# ytembeds - a YouTube Video Embed Generator

This simple Python script allows you to search YouTube for video URLs and generate the corresponding embed codes using the YouTube Data API v3. You can enter search terms one at a time, and the script will output the video URL and embed code for each term.

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/muddylemon/ytembeds.git
```

2. Change to the project directory:

```bash
cd ytembeds
```

3. Set up a virtual environment (optional but recommended):

```bash
python -m venv yt
source yt/bin/activate  # On Windows, use `yt\Scripts\activate`
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project directory and add your YouTube API key:

```bash
cp example.env .env
```

```
APIKEY=your_api_key
```

Replace `your_api_key` with your actual YouTube API key.

## Usage

1. Run the script:

```bash
python make_embeds.py
```

2. Enter search terms one at a time, pressing Enter after each term. To finish entering search terms, press Enter on a blank line.

3. The script will display the video URL and embed code for each search term. You can copy the output from the terminal or pipe the output to a text file:

```bash
python make_embeds.py > output.txt
```
