#lang racket

(define (drop-divisible i list)
  (define (drop num)
    (cond
      [(equal? num i) #f]
      [(zero? (remainder num i)) #t]
      [else #f]))
  (remv* (filter drop list) list))

(module+ test
  (require rackunit)
  (check-equal? (drop-divisible 3 (list 2 3 4 5 6 7 8 9 10)) (list 2 3 4 5 7 8 10)))