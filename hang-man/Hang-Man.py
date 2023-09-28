from tkinter import *
import random
from PIL import Image
import moviepy.editor


video = moviepy.editor.VideoFileClip("AAA.mp4")

video.preview()



print("      welcome                welcome                welcome        welcome          welcome           welcome      welcome      welcome         welcome        welcome                                       ")

friuts = []
jobs = []
foods = []
animalls = []
numbers = []
computer_parts = []
clothes = []
colors= []
cars = []
home_parts = []
bodys = []
friut = open("python/fruit.txt","rt")
job = open("python/jobs.txt","rt")
food = open("python/food.txt","rt")
animall = open("python/animall.txt","rt")
color = open("python/colors.txt","rt")
number = open("python/numbers.txt","rt")
computer_part = open("python/computer.txt","rt")
clothe = open("python/clothes.txt","rt")
car = open("python/cars.txt","rt")
home_part = open("python/homes.txt","rt")
body = open("python/bodys.txt","rt")

for f in friut:
    friuts.append(f)
for j in job:
    jobs.append(j)
for fo in food:
    foods.append(fo)
for a in animall:
    animalls.append(a)
for co in color:
    colors.append(co)
for n in number:
    numbers.append(n)
for cp in computer_part:
    computer_parts.append(cp)
for c in clothe:
    clothes.append(c)
for ca in car:
    cars.append(ca)
for h in home_part:
    home_parts.append(h)
for b in body:
    bodys.append(b)


print("Welcome to Hangman!")

while True:

    print("Please choose a topic for the game.")
    start = int(input("(*1*friuts,*2*jobs,*3*foods,*4*animalls,*5*numbers,*6*computer_parts,*7*cloths,*8*colors,*9*cars,*10*home,*11*bodys)="))
    A = ['_ ']

    if start==1:
        word = random.choice(friuts)
        A = ['_ '] * (len(word)-1)
    elif start==2:
        word = random.choice(jobs)
        A = ['_ '] * (len(word)-1)
    elif start==3:
        word = random.choice(foods)
        A = ['_ '] * (len(word)-1)
    elif start==4:
        word = random.choice(animalls)
        A = ['_ '] * (len(word)-1)
    elif start==5:
        word = random.choice(numbers)
        A = ['_ '] * (len(word)-1)
    elif start==6:
        word = random.choice(computer_parts)
        A = ['_ '] * (len(word)-1)
    elif start==7:
        word = random.choice(clothes)
        A = ['_ '] * (len(word)-1)
    elif start==8:
        word = random.choice(colors)
        A = ['_ '] * (len(word)-1)
    elif start==9:
        word = random.choice(cars)
        A = ['_ '] * (len(word)-1)
    elif start==10:
        word = random.choice(home_parts)
        A = ['_ '] * (len(word)-1)
    elif start==11:
        word = random.choice(bodys)
        A = ['_ '] * (len(word)-1)


    print(A)
    attempts = len(word)+3
    points = 0


    while attempts > 0 and '_ ' in A:
        voorodi = input("Please enter a letter: ")

        if voorodi in word or chr(ord(voorodi)-32) in word or chr(ord(voorodi)+32) in word:
            for i in range(len(word)):
                if word[i] == voorodi:
                    A[i] = voorodi
                    print("The letter you entered is in the word!")
                    points+=30
                    print("Your points=",points)
                elif word[i] == chr(ord(voorodi)-32):
                    A[i] = chr(ord(voorodi)-32)
                    points+=30
                    print("Your points=",points)
                    print("The letter you entered is in the word!")
                elif word[i] == chr(ord(voorodi)+32):
                    A[i] = chr(ord(voorodi)+32)
                    points+=30
                    print("Your points=",points)
                    print("The letter you entered is in the word!")   
            print(" ".join(A))
        else:
            print(" ".join(A))
            print("The letter you entered is not in the word")
            print("you have",attempts,"attemps!!!!!!!!!!!!")
            print("Your points=",points)
            attempts-=1
            
        if attempts <=3:
            print("!woring!    !woring!    !woring!    !woring!    !woring!    !woring!    !woring!    !woring!    !woring!    !woring!    !woring!   !woring!    !woring!    !woring!")
            print("you have",attempts,"attemps!!!!!!!!!!!!")
        if  attempts ==3 and points >=20:
            print("I have a good suggestion for you.")
            print("I can subtract 30 from the points you have and give you 1 chance.")
            s = int(input("If you agree, press the 1 key and if you do not agree, press the 0 key."))
            if s==1:
                attempts+=1
                points-=30
                print("Remaining points=",points)
                continue
            elif s==0:
                continue
        


    if attempts==0:
        image1 = Image.open('lost.jpg')

        image1.show()
        for i in range (100):
            print("you lost!!   you lost!!    you lost!!   you lost!!    you lost!!       you lost!!      you lost!!        you lost!!        you lost!!")
    else:
        image2 = Image.open('win.jpg')

        image2.show()
        for i in range (100):
            print("you win!!   you win!!    you win!!   you win!!    you win!!       you win!!      you win!!        you win!!        you win!!")
            
    print("\n\n\n\nthe word is",word)



    An=input("*********************if you like to continue press 1,if he don't want to continue the game press  2*******************************\n\n\n\n")




    if An=='1':
        continue
    elif An=='2':
        break
