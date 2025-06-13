from flask import Flask, render_template, request
import requests


app = Flask(__name__)


class ArtikelAPI:
    def __init__(self):     
        """
        Inisialisasi API dengan sheet_id dan gid yang akan digunakan untuk semua request.
        
        Args:
            sheet_id (str): ID sheet Google Spreadsheet
            gid (str): ID worksheet
        """
        self._sheet_id = ''
        self._gid = ''
        self.base_url = "https://backend-sheet-opensource.vercel.app/"

    def sheet_id(self, value):
        """Setter untuk sheet_id"""
        self._sheet_id = value
    
    def gid(self, value):
        """Setter untuk gid"""
        self._gid = value

    def get_articles(self, page=1, limit=10):
        """
        Mengambil daftar artikel dari Google Spreadsheet.
        
        Args:
            page (int, optional): Nomor halaman. Defaults to 1.
            limit (int, optional): Jumlah artikel per halaman. Defaults to 10.
        
        Returns:
            dict: Response dari API dengan format:
                {
                    "payload": [...],
                    "status": "success",
                    "message": "Data berhasil diambil"
                }
        """
        endpoint = f"{self.base_url}/artikel"
        
        params = {
            "sheet_id": self._sheet_id,
            "gid": self._gid,
            "page": page,
            "limit": limit
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "payload": None,
                "status": "error",
                "message": f"Error saat mengambil artikel: {str(e)}"
            }

    def get_articles_by_category(self, category, page=1, limit=10):
        """
        Mengambil daftar artikel berdasarkan kategori tertentu.
        
        Args:
            category (str): Kategori artikel yang dicari
            page (int, optional): Nomor halaman. Defaults to 1.
            limit (int, optional): Jumlah artikel per halaman. Defaults to 10.
        
        Returns:
            dict: Response dari API
        """
        endpoint = f"{self.base_url}/artikel/category"
        
        params = {
            "sheet_id": self._sheet_id,
            "gid": self._gid,
            "category": category,
            "page": page,
            "limit": limit
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "payload": None,
                "status": "error",
                "message": f"Error saat mengambil artikel: {str(e)}"
            }

    def get_article_detail(self, slug):
        """
        Mengambil detail artikel berdasarkan slug.
        
        Args:
            slug (str): Slug artikel yang dicari
        
        Returns:
            dict: Response dari API
        """
        endpoint = f"{self.base_url}/artikel/detail"
        
        params = {
            "slug": slug
        }
        
        data = {
            "sheet_id": self._sheet_id,
            "gid": self._gid
        }
        
        try:
            response = requests.get(endpoint, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "payload": None,
                "status": "error",
                "message": f"Error saat mengambil detail artikel: {str(e)}"
            }


config_artikel = ArtikelAPI()
config_artikel.sheet_id('17-WZdi-S27wCUdxuAtvR3j2564WIbx9Nwz45EbmxCyM')
config_artikel.gid('710523043')


@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    artikel = config_artikel.get_articles(page=page)
    data = {
        'title': f'Informasi Berita Halaman {page}' if page > 1 else 'Informasi Berita',
        'metadeskripsi': 'Puing Berita terpercaya dengan informasi terkini dan akurat. Temukan berita terbaru seputar politik, ekonomi, '\
            'teknologi, dan olahraga. Update setiap hari dengan konten berkualitas.'
    }
    return render_template('home.html', artikel=artikel, title=data['title'], metadeskripsi=data['metadeskripsi'])


@app.route('/artikel/<slug>')
def artikel(slug):
    # TODO: Fetch article data based on slug from database
    # For now, return template with dummy data
    artikel = config_artikel.get_article_detail(slug)    
    return render_template('artikel.html',artikel=artikel)


@app.route('/category/<category>')
def cataogory(category):
    # TODO: Fetch article data based on slug from database
    # For now, return template with dummy data
    page = request.args.get('page', 1, type=int)
    artikel = config_artikel.get_articles_by_category(category, page=page)
    data = {
        'title': f'Kategori: {category.capitalize()}',
        'metadeskripsi': f'Puing Berita terpercaya dengan informasi terkini dan akurat dalam kategori {category}. Temukan berita terbaru seputar {category} dan topik lainnya. Update setiap hari dengan konten berkualitas.'
    }
    return render_template('category.html', artikel=artikel, title=data['title'], metadeskripsi=data['metadeskripsi'])


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
