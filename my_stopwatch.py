import time

def stopwatch(func):
    """This stopwatch function will time how long it takes for a given function to run once used as a decorator.
        It will also add an additional feature to your fuction by giving it the ability to accept multple arguments if it 
        accepts one by default.
    """
    def timer_wrapper(*arg):
        try:
            t1 = time.time()
            print(f"Time Started")
            function_results = func(arg)
            t2 = round(time.time() - t1,2)
            print(f"Function {func.__name__} finished running in {t2} seconds.")
        except BaseException as err:
            print(f"{err}")
        return function_results       
    return timer_wrapper

@stopwatch
def tester():
    time.sleep(5)
    print('testerFunction')
    return

if __name__ == "__main__":
    tester()
