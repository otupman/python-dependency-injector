"""`di.Factory` providers with method injections example."""

import dependency_injector as di


class User(object):
    """Example class User."""

    def __init__(self):
        """Initializer."""
        self.main_photo = None
        self.credit_card = None

    def set_main_photo(self, photo):
        """Set user's main photo."""
        self.main_photo = photo

    def set_credit_card(self, credit_card):
        """Set user's credit card."""
        self.credit_card = credit_card


class Photo(object):
    """Example class Photo."""


class CreditCard(object):
    """Example class CreditCard."""

# User, Photo and CreditCard factories:
credit_cards_factory = di.Factory(CreditCard)
photos_factory = di.Factory(Photo)
users_factory = di.Factory(User,
                           di.Method('set_main_photo', photos_factory),
                           di.Method('set_credit_card', credit_cards_factory))

# Creating several User objects:
user1 = users_factory()
# Same as: user1 = User()
#          user1.set_main_photo(Photo())
#          user1.set_credit_card(CreditCard())
user2 = users_factory()
# Same as: user2 = User()
#          user2.set_main_photo(Photo())
#          user2.set_credit_card(CreditCard())

# Making some asserts:
assert user1 is not user2

assert isinstance(user1.main_photo, Photo)
assert isinstance(user1.credit_card, CreditCard)

assert isinstance(user2.main_photo, Photo)
assert isinstance(user2.credit_card, CreditCard)

assert user1.main_photo is not user2.main_photo
assert user1.credit_card is not user2.credit_card
