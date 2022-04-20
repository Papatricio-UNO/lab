from classes import *


class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2

    def test_power(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 1'
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 2'

    def test_volume_down(self):
        pass
