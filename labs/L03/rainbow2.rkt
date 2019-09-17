#lang slideshow
(define (rainbow p)
  (map (lambda (color)
         (colorize p color))
       (list "red" "orange" "yellow" "green" "blue" "purple")))

(define (rainbow2 p)
  (define (color-mapper p color-list)
    (cond
      [(empty? color-list) empty]
      [else (cons (colorize p (first color-list))
            (color-mapper p (rest color-list)))]))
  (color-mapper p  (list "red" "orange" "yellow" "green" "blue" "purple")))