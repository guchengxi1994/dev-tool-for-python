class ImageStr:
    def __init__(self,img,s:str) -> None:
        self.img = img
        self.s = s
        self.shape = img.shape
    
    def trans(self):
        """translation
        """
        ...
    
    @property
    def imgW(self):
        return self.shape[1]
    
    @property
    def imgH(self):
        return self.shape[0]

class FakeArgs:
    ...