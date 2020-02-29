library('HilbertVis')
path = "./hilbert/"
files = c('hr','rr','spo','sys', 'dia')
for(i in files){
    data = read.csv(paste(path,i,".csv", sep=""), header = FALSE)
    print(dim(data))
    print(class(data))
    hmat<-hilbertImage(data[,1], level=4, mode="mean")
    write.csv(hmat, file = paste(path,i,"_hilbert.csv", sep=""),row.names=FALSE)
}
