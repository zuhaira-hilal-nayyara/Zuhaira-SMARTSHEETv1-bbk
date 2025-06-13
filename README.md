# Puingberita
> Minimalist blog powered by Flask + Google Spreadsheet  
> 📺 **Demo Video & Installation** [Watch on YouTube](https://www.youtube.com/watch?v=4qbDS9GEoF8)

[![Demo Video](https://img.youtube.com/vi/4qbDS9GEoF8/0.jpg)](https://www.youtube.com/watch?v=4qbDS9GEoF8)

Puingberita is simple blog build from Flask + Google Spreadsheet. This project support deploy using Vercel.

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally
- It is recommended to set up a virtual environment locally
- Activate your virtualenv `source venv/bin/activate`
- Install Python dependencies using the following command: `pip install -r requirements.txt`
- Run dev `python api/index.py`. The app will run on port `http://localhost:5000`

Another way to run the development server using Vercel
- Make sure you have a Vercel account
- Then, run the following commands:
```bash
npm i -g vercel
vercel dev
```
Your Flask application is now available at `http://localhost:3000`.

### Change your Google Spreadsheet Credential
- Open `api/index.py`
- Replace this part with your credentials
```
config_artikel = ArtikelAPI()
config_artikel.sheet_id('your-sheet-id')
config_artikel.gid('your-google-spreadsheet-gid')
```

### Spreadsheet Template
Make sure your spreadsheet follows this template: [here](https://docs.google.com/spreadsheets/d/17-WZdi-S27wCUdxuAtvR3j2564WIbx9Nwz45EbmxCyM/edit?gid=71052)

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
