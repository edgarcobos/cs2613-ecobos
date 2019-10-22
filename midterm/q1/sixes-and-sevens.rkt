#lang racket

(define (sixes-and-sevens list)
  (define (helper lst acc)
    (cond
      [(empty? lst) acc]
      [(zero? (remainder (first lst) 6)) (helper (rest lst) (cons (first lst) acc))]
      [(zero? (remainder (first lst) 7)) (helper (rest lst) (cons (first lst) acc))]
      [else (helper (rest lst) acc)]))
  (reverse (helper list '())))

(module+ test
  (require rackunit)
  (check-equal? (sixes-and-sevens '(1 6 7 12)) '(6 7 12)))