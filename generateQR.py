"""
Author: PHAN HONG SON
Univ: SungKuynKwan University
"""
import qrcode
# import pyqrcode

def generateQR():
    image = qrcode.make('https://kimson.ninhbinh.gov.vn/')
    image.save('QR6.png')

def main():
    print('========> Starting Generate <==========')
    link = 'https://kimson.ninhbinh.gov.vn/'
    generateQR()

if __name__ == '__main__':
    main()
