# Results from testing single- vs multi-threaded server

These are the boxplots that I received from putting the results of the tests into R.
#
![Boxplot Comparison](./comparisonPlot.png?raw=true)
#
As seen in the above (albeit small) boxplots above, you can see that the mutli-threaded server results are on top while the single-threaded server results are on the bottom. 
- With the multi-threaded server, it can be observed that, on average, it would take about 0.2 seconds less time to run 100 requests than it would for the single-threaded server. This makes sense as there are multiple threads running at one time, therefore ensuring that it will complete its requests quicker than the single-threaded server.
- For the single-threaded server, it can be observed that there are more extreme outliers and that it also has a greater average time than the multi-threaded server. This is caused by the fact that it sends each request one at a time and waits for that request to complete before creating another thread, thus taking more time.

<br>
As the tests took about less than a second for 100 of them, it can be inferred that the outliers are caused by variability in network speeds. With my home internet (I live in the country and use Starlink), we get highly variable network speeds, and it is possible that there were some drops in the testing process where the dish was searching for the satelite.

<br>

### Notes:

Please note that the boxplot titles are quite small due to the size of the image itself. I have made it that size to account for the ability to see the boxes themselves. If I went much smaller, then it would simply look like a jumbled mass of lines and outlier circles.<br>

Also note that I included the original .png file in the folder along with the code that produced it. The two .csv files of the testing results are also included in the folder.