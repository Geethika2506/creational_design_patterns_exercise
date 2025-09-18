class GlobalBudget:
    _instance = None

    def __new__(cls, initial_amount=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._amount = initial_amount if initial_amount is not None else 0.0
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def allocate(self, amount):
        if amount <= 0:
            raise ValueError("Cannot allocate non-positive budget.")
        if self._amount < amount:
            raise ValueError("Insufficient budget.")
        self._amount -= amount
      

    def remaining(self) -> float:
        return self._amount

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._amount}>"
