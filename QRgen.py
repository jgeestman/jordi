import os
import qrcode

"""
Generate QR codes from web0-files.
Each code gives all needed information about an apartment.
Verd = verdieping
bwnr = bouwnummer
Data = volledige website title van document
"""


class QRread:

    def __init__(self, verd =0, bwnr =0, data =""):
        self.verd = verd
        self.bwnr = bwnr
        self.data = data
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=5,)
    
        qr.add_data(data)
        qr.make(fit=True)

        path1 = "C:\\Users\\jordi\\OneDrive\\Documenten\\downloads"
        os.chdir(path1)
        mapx = """QR-code, verdieping {}, bwnr {}""".format(int(self.verd), (self.bwnr))
        os.makedirs(mapx)
        
        path2 = path1 + "\\" + mapx
        os.chdir(path2)
        img = qr.make_image(fill_color="white", back_color="black")
        img.save("""QR-code,verdieping {}, bwnr {}.png""".format(int(self.verd), (self.bwnr)))
