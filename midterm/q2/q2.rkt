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
  (check-equal? (sixes-and-sevens '()) '())
  (check-equal? (sixes-and-sevens '(6 7 12 14 18 21)) '(6 7 12 14 18 21))
  (check-equal? (sixes-and-sevens '(14 12 1 0)) '(14 12 0)))