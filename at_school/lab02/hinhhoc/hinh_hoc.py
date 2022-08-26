from abc import abstractmethod, ABC


class HinhHoc(ABC):
    def __init__(self, canh):
        self.canh = canh

    @abstractmethod
    def tinhDienTich(self) -> float:
        pass

    @abstractmethod
    def xuat(self) -> None:
        pass
