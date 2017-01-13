"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    '''Shared properties of domestic and international orders'''

    def __init__(self, species, qty, order_type, tax, country_code=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas melon":
            base_price = 7.5
        else:
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Properties of AbstractMelonOrder plus International orders"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", .08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Properties of AbstractMelonOrder plus International orders"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", .17, country_code)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total
