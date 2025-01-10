# Gen AI

## Python (local)

### Install

```bash
sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
pip3 install orq-ai-sdk requests python-dotenv
```

### Update

```bash
pip3 install orq-ai-sdk --upgrade
```

### Use

```bash
source venv/bin/activate
# Add PDF files in pdf folder.
python3 summarize.py3
```

## Prompt

```
Analyze the provided PDF file. 

# Steps
Extract all the text from this PDF as markdown
Extract the creation date
Extract the author
Extract the source
Extract the organisations
Make a list of key figures
Describe each chart
Describe each maps
Describe all images
Extract all data in the tables in a markdown format, make sure to include all table cells
Make an alphabetical list of countries
Make an alphabetical list of cities and a their country
Condense the analyzed information into a clear and concise summary, using your own words. Aim for a summary that is 10-20% of the original report's length.

Return a verbose structured markdown response containing a header for each step
```
