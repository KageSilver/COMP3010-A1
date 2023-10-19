summarySingle <- read.table("C:/Users/taral/Desktop/School/Fourth year/Fall/Comp 3010/Assignments/A1/COMP3010-A1/summarySingle.csv", quote="\"", comment.char="")
colnames(summarySingle) <- c("Single-Threaded")
summaryMulti <- read.table("C:/Users/taral/Desktop/School/Fourth year/Fall/Comp 3010/Assignments/A1/COMP3010-A1/summaryMulti.csv", quote="\"", comment.char="")
colnames(summaryMulti) <- c("Multi-Threaded")

data = cbind(summarySingle,summaryMulti)

png(file="comparisonPlot.png",width=1658,height=500)

boxplot (data,beside=T, main="1000 Time Comparisons for Single- vs. Multi-Threaded Servers",
         ylab="Single- vs. Multi-Threaded Server", xlab="Average Time for 100 Requests",
         outlier.shape=NA, horizontal=T)
dev.off()