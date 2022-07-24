# my_stopwatch
Time how long it takes for a given function to run.

1. Import the **"my_stopwatch"** module into your desired module.  
    example:     
            _from_ my_stopwatch _import_ stopwatch
2. Decorate the function you would like to time:
    example:  
      
     ``` 
      @stopwatch  
      def adding_stuff_2(*num):  
              lc1 = [x * 3 for x in num]  
              return lc1```
