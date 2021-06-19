import pandas as pd
import datetime as dt
data=pd.read_csv(r'C:\Users\Shruti Ghoradkar\PycharmProjects\my project\7. Udemy Courses.csv')

#1.What is the different subjects for which udemy is offering courses
one=data.subject.unique()
print(one,end=' ')

#2.Which subject has the maximum number of courses
two=data.subject.value_counts()
print(max(two))

# 3.Show all the courses which are free of cost
three=data[data.is_paid==False]
print(three)

#.4Show all the courses which are paid of cost
four=data[data.is_paid==True]
print(four)

#5.Which are top selling courses
six=data.sort_values('num_subscribers',ascending=False)
print(six.head(4))

#6.Which are the least selling courses
s=data.sort_values('num_subscribers',ascending=True)
print(s.head(4))

#7.Show the all courses of graphic design where price is below 100
d=data[(data.subject=='Graphic Design')&(data.price>'100')]
print(d)

#8 List all the cources that are related with python
p=len(data[data.course_title.str.contains('Python')])
print(p)


#9 what are the courses that published in year 2015
data['published_timestamp']=pd.to_datetime(data.published_timestamp)
print(data.dtypes)
data['year']=  data['published_timestamp'].dt.year
b=data[data.year==2015]
print(b)

#10 What are the maximum number of suscriber for each level of courses
data.level.unique()
b=data.groupby('level')['num_subscribers'].max()
print(b)
