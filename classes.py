class Television:
    """
    A class representing details for a television object
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """""
        Constructor to create intial state of a TV object.
        :param Television.MIN_CHANNEL: Television's starting channel.
        :param Television.MIN_VOLUME: Television's starting volume.      
        """""
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        Method to turn the television on or off
        :return: Television's power status
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self):
        """""
        Method to go up a television channel 
        :return: Television's channel
        """""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to go down a television channel
        :return: Television's channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increase a television's volume
        :return: Television's volume
        """
        if self.__status and self.__volume != Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        """
        Method to decrease a television's volume
        :return: Television's volume
        """
        if self.__status and self.__volume != Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self):
        """
        Method to print the power status, channel, and volume
        :return: Television's volume
        """
        return f'TV status: Is on = {self.__status}, ' \
               f'Channel = {self.__channel}, Volume = {self.__volume}'

