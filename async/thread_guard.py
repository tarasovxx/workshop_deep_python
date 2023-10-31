import threading

class ThreadGuard:
    def __init__(self, thread):
        self.thread = thread

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.thread.is_alive():
            self.thread.join()

# Пример использования
def my_function():
    print("Thread started")
    # Какой-то код выполнения в потоке

my_thread = threading.Thread(target=my_function)
my_thread.start()

with ThreadGuard(my_thread):
    # Другой код, выполняемый в главном потоке
    pass

# Когда блок выходит из контекста, поток автоматически завершается
