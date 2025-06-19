class BankAccount:
    """
    A class to represent a bank account with basic banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The initial balance of the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self._account_balance = int(initial_balance)  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._account_balance += int(amount)
        # The prompt implies printing 'Deposited: $X' in main.py, so this print is for internal clarity.
        # It can be removed if main.py is solely responsible for output.

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self._account_balance >= amount:
            self._account_balance -= int(amount)
            # Similar to deposit, this print can be adjusted based on main.py's responsibility.
            return True
        else:
            return False

    def display_balance(self):
        """
        Returns the current account balance.
        (Changed to return for main.py to handle printing, aligning with provided sample outputs)
        """
        return self._account_balance