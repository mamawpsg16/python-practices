import time
def log_execution_time(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@log_execution_time
def my_function():
    time.sleep(1)  # Simulate a long-running function

def main():
    my_function()

if __name__ == "__main__":
    main()