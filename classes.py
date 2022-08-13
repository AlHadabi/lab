class Television:
    """
    A class representing the Television modification
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        """
        Constructor to create initial states for the TV
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__TV_status == False

    def power(self):
        """
        method that used to turn the TV on/off
        :return: TV status
        """
        if self.__TV_status == False:
            self.__TV_status == True
        elif self.__TV_status == True:
            self.__TV_status == False

    def channel_up(self):
        """
        method that used to adjust the TV channel by decrementing its value
        :return: number
        """
        if self.__TV_status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        method that used to adjust the TV channel by decrementing its value
        :return: number
        """
        if self.__TV_status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def volume_up(self):
        """
        method used to adjust the TV volume by decrementing its value
        :return: number
        """
        if self.__TV_status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
        else:
            self.__volume = Television.MIN_VOLUME

    def volume_down(self):
        """
        method used to adjust the TV volume by decrementing its value
        :return: number
        """
        if self.__TV_status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
        else:
            self.__volume = Television.MIN_VOLUME

    def __str__(self):
        """
        method used to return the TV status
        :return: TV status
        """
        return f"TV status: Is on ={self.__TV_status == True}, channel = {self.__channel}, Volume = {self.__volume}"
