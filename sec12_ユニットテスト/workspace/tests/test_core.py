import pathlib
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=iLrrDwAAQBAJ&printsec=frontcover&'
    'img=1&zoom=5&edge=curl&source=gbs_api'
)

class SaveThumbnailsTest(unittest.TestCase):
    # テストケース実行前に都度実行
    def setUp(self):
        # 一時ディレクトリを作成
        self.tmp = TemporaryDirectory()

    # テストケース実行前に都度実行
    def tearDown(self):
        # 一時ディレクトリを全削除
        self.tmp.cleanup()

    # save_thumbnailsの中で利用する参照名を指定する
    @patch('booksearch.core.get_data')
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book

        data_path = pathlib.Path(__file__).with_name('data')
        mock_get_data.return_value = (
            data_path / 'iLrrDwAAQBAJ_thumbnail.jpeg'
        ).read_bytes()

        book = Book({
            'id': '',
            'volumeInfo': {
                'imageLinks':{'thumbnail': THUMBNAIL_URL}
            }
        })
        filename = book.save_thumbnails(self.tmp.name)[0]
        mock_get_data.assert_called_with(THUMBNAIL_URL)

        data = pathlib.Path(data_path / 'iLrrDwAAQBAJ_smallThumbnail.jpeg').read_bytes()

        self.assertEqual(data, filename.read_bytes())