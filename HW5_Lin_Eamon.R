# Question 1
a = matrix(c(7,2,9,4,12,13), ncol=3, nrow=2)
a
b = matrix(c(1:3,7:9,12:14,19:21), ncol=4, nrow=3)
b
a%*%b

# Question 2
# part a
Data_Frame <- data.frame(
  id = c(1,2,3,4,5),
  name = c("Peter", "Amy", "Ryan", "Gary", "Michelle"),
  salary = c(623.30,515.20,611.00,729.00,843.25)
)
Data_Frame

# part b
Data_Frame_2 <- cbind(Data_Frame, department = c("economics", "finance", "psychology", "mathematics", "biology"))
Data_Frame_2

# part c
Data_Frame_2[c(1,3,5),c(2,3)]

# part d
Data_Frame_2 <- cbind(Data_Frame, department = c("economics", "finance", "psychology", "mathematics", "biology"))
Data_Frame_2
plotdata <- Data_Frame_2[c(1,4,5),c(3)]
plotdata
barplot(plotdata, main="salary distribution", names.arg=Data_Frame_2[c(1,4,5),c(2)])

# part e
max <- max(Data_Frame_2$salary)
min <- min(Data_Frame_2$salary)
median <- median(Data_Frame_2$salary)

aax <- which.max(Data_Frame_2$salary)
iin <- which.min(Data_Frame_2$salary)
label <- c("Michelle", "Amy", "Peter")

pie(c(max,min,median), main = "Salary Benchmark", labels = label)

