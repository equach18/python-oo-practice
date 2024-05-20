"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create a serial number from given start"""
        self.start = start
        self.next = start

    def __repr__(self):
        """Show serial representation"""
  
        return f"SerialGenerator start = {self.start}, next = {self.next}"
    
    def generate(self):
        """Generates a serial number"""
        self.next = self.next + 1
        return self.next - 1
    
    def reset(self):
        """Resets the serial number back to the given starting point"""
        self.next = self.start




