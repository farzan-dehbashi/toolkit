class OldPrinter:
    def print_text(self, text):
        print(f"[OldPrinter]: {text}")


class NewPrinterInterface:
    def print(self, text):
        raise NotImplementedError


class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self._old_printer = old_printer

    def print(self, text):
        self._old_printer.print_text(text)


if __name__ == "__main__":
    old = OldPrinter()
    adapter = PrinterAdapter(old)
    adapter.print("Hello from adapter!")
