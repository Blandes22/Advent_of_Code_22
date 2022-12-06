class SignalDecoder:
    def __init__(self, signal: str):
        self.signal = signal
        self.length_of_signal = len(self.signal)

    def find_position_after_unique_string_of_length_n(self, n):
        for i in range(self.length_of_signal):
            temp = list(self.signal[i:i+n])
            check = len(set(temp))
            if len(temp) == check:
                break
        return i + n