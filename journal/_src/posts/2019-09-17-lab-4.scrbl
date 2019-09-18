#lang scribble/manual
@(define (hello) "hello")
@(define (greet person)
(string-append "hello " person))
@(define (todo hdr . lst)
(list (bold hdr) (apply itemlist (map item lst))))

Title: Lab 4
Date: 2019-09-17T12:57:36
Tags: all
Authors: Edgar Cobos

At the beginning of Lab 4, we discussed the similarities and differences between racket and Java. First, we looked at #lang racket and #lang slideshow which are the equivalent to import statements in Java. We also looked at (+ 1 2) which calls the function + and passes it two numbers to be added together. In Java, you don't need to make a funciton call to add and rather just add like so: 1 + 2. As we moved on to (rectangle 10 10), which in Java would be something like new Rectangle(10 10), we were able to identify a difference between racket and java, which is that racket allows printing picure values while Java does not. Next, (define r 10) is very similar to "int r = 10' with the main difference being that in racket we don't need to specify what type of variable r is. The function (define (square x) (rectangle x x)) can be compared to having a Rectangle class and a Square class, whose constructor method initializes a Rectangle of same sides by passing the specified length as both arguments. The colorize function used as in (colorize (square 10) "red") would have no effect in Java as picture values don't exist but again the concept of calling a function with two parameters is the same. Lastly, the binding (let* ([x 10] [y (+ x 10)]) (* x y)) would be equivalent to writing 'int x = 10; int y = x + 10; return x*y;' in Java, with no major difference. Afterwards, I learned about the build-list function, which basically creates a list of elements of a specified length and applies a specified procedure to them. Then, we practiced some more recursion and I noticed that it took me less time to solve the excercises than previously. Also, I followed along the Scribble Demo and created a new blog entry, implemented racket definitions for hello, greet and todo and their invocations can be found at the bottom of this post. Finally, we further explored modules, submodules, require, and provide by creating a module- with a test submodule and a main submodule- that acted as a library through require and provide.

<!-- more -->

@hello{}
@greet{cookie monster}

@(todo "mondays" "eat" "kill bugs" "repeat")

