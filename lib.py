from rich.console import Console

shell = Console()

def passed(msg:str, num:int=1):
    shell.print(f'[reverse green] PASSED [/reverse green]: {msg}')

def failed(msg:str):
    shell.print(f'[reverse red] FAILED [/reverse red]: {msg}')

import functools, threading

def runTests(code, fileName):
    functions = []
    decoratorName='test'
    linha_anterior = ''
    for i, line in enumerate(code.split('\n')):
        if linha_anterior.startswith(f'@{decoratorName}'):
            functions.append(line.split('def')[1].split('()')[0].strip())
        linha_anterior = line

    threads = []
    for i in functions:
        #Execute the function
        exec(f'from {fileName} import {i}')
        thread = threading.Thread(target=eval(i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()



def test(expected:str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if result == expected:
                    passed(func.__name__)
                else:
                    failed(f'{func.__name__} | Expected {expected}, got {result}')
            except Exception as e:
                result = e
                failed(f'{func.__name__} | {e}')
            return result
        return wrapper
    return decorator
