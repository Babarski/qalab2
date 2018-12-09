'''
Phone class realization
'''


class Phone:
    '''
    Class phone realization
    '''

    name = ''   # model name
    price = 0   # price

    def __init__(self, phone_name, phone_price):
        # self.set_id()
        self.set_name(phone_name)
        self.set_price(phone_price)

    def get_name(self):
        '''
        Return Object name
        :return: phone name
        '''
        return self.name

    def set_name(self, name):
        '''
        Set phone object name
        :param name: string
        :return: None
        '''
        self.name = name

    def get_price(self):
        '''
        Get price
        :return: None
        '''
        return self.price

    def set_price(self, price):
        '''
        Set price
        :param price: Integet
        :return: None
        '''

        self.price = price
