import qrcode

# from ShortURL import ShortURL as surl

class QRCode:
    def __init__(self, text='', filename='qr', ext='png', is_link=True, redirect=''):
        self._filename = filename
        self._ext = ext
        self._is_link = is_link
        self._redirect = redirect
        self._text = text
        self._qr = qrcode.QRCode()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value

    @property
    def is_link(self):
        return self._is_link

    @is_link.setter
    def is_link(self, value):
        self._is_link = value

    @property
    def redirect(self):
        return self._redirect

    @redirect.setter
    def redirect(self, value):
        self._redirect = value

    def create(self):
        # if _redirect != '':
            # _text = surl.generate_redirect(_text)

        link_prefix = 'https://'
        value = link_prefix + self._text if self._is_link else self._text

        self._qr.add_data(value)
        self._qr.make(fit=True)

    def generate(self):
        self.create()

        full_path = self._filename + '.' + self._ext

        img = self._qr.make_image()
        img.save(full_path)

        # TODO: Testing valid qr was generated

        return full_path
