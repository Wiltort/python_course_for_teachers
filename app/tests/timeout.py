import threading

def run_with_timeout(func, timeout, *args, **kwargs):
    """
    Запускает функцию с ограничением по времени.

    :param func: Функция, которую нужно выполнить.
    :param timeout: Время в секундах, в течение которого функция должна завершиться.
    :return: Результат выполнения функции или None, если время истекло.
    """
    result = [None]  # Используем список для хранения результата
    finished = threading.Event()

    def wrapper():
        try:
            result[0] = func(*args, **kwargs)
        finally:
            finished.set()

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)
    
    if finished.is_set():
        return result[0]
    else:
        print("Время выполнения функции превышено!")
        return None
